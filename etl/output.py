import csv
import os
from io import StringIO
#from pathlib import Path
from etl.functions import getPath
from google.cloud import storage

# to_csv('ingram_daily.csv', data, Ingram.keys())

# storage_client.get_bucket(dictionary['bucketName']).blob(dictionary['destination_blob_name']).upload_from_filename(dictionary['source_file_name'])

def to_gcs_bucket(filename):
    """
    Writes a string to a gcs bucket.
    :param output: the string
    :param filename: the name of the file to write
    :return: none
    """

    dictionary = {'bucketName': 'app-script-data-extraction-output',
                  'destination_blob_name': f'distribution/{filename}',
                  'source_file_name': getPath(filename)}
    storage_client = storage.Client()
    storage_client.get_bucket(dictionary['bucketName']).blob(dictionary['destination_blob_name'])\
        .upload_from_filename(dictionary['source_file_name'])

def to_csv(filename, data, fields):
    """
    Writes a dictionary object to a csv file in gcs storage
    :param filename: the name of the file to create
    :param data: an ordered dictionary object
    :param fields: a list of fields.
    :return: none
    """

    #with open(filename, 'w') as csvfile:
        # writer = csv.DictWriter(csvfile, fieldnames=fields, dialect='dblquote')
        # writer.writeheader()
        # writer.writerows(data)

    # path = Path(f'/tmp/{file_name}')
    # with path.open('wb+') as file:
        # client.bucket(event['bucket']).get_blob(event['name']).download_to_file(file)

    csv.register_dialect('dblquote',
                         delimiter=',',
                         lineterminator='\n',
                         quotechar='"',
                         quoting=csv.QUOTE_ALL,
                         skipinitialspace=True)

    path = getPath(filename)

    with path.open('w', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields, dialect='dblquote')
        writer.writeheader()
        writer.writerows(data)
    
    to_gcs_bucket(filename)

