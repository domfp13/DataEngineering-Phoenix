# Other libs
import os
#from pathlib import Path
from google.cloud import storage
from etl.functions import getPath
import logging

# Local libs
from etl.extract import (parse_ingram, parse_synnex, parse_techdata, parse_ingramCAD, 
                            parse_CADTechDataOG, parse_CADTechData, parse_Ingram_Micro_BMO)

    
"""
Register processes here:
"""
REGISTRY = {
    # filename : function
    'DBI_LOAD_0001.xls':  parse_CADTechData,
    'DBI_LOAD_0002.xls':  parse_CADTechDataOG,
    'DBI_LOAD_0003.xlsx': parse_Ingram_Micro_BMO,
    'DBI_LOAD_0004.xls':  parse_synnex,
    'DBI_LOAD_0005.xlsx': parse_ingram,
    'DBI_LOAD_0007.xlsx': parse_techdata,
    'DBI_LOAD_0008.xls':  parse_ingramCAD
}

def process_vendor_excel_files(event, context):
    
    """Triggered by a change to a Cloud Storage bucket.
    Args:
        event (dict): Event payload.
        context (google.cloud.functions.Context): Metadata for the event.
    """

    try:
        logging.info('Starting')
        file_name = os.path.basename(event['name'])
        
        if file_name in REGISTRY.keys():
            logging.info(f'Processing: {file_name}')
            client = storage.Client()
            path = getPath(file_name)

            with path.open('wb+') as file:
                client.bucket(event['bucket']).get_blob(event['name']).download_to_file(file)

            REGISTRY[file_name](file.name)
        else:
            raise NotImplementedError 
    except NotImplementedError:
        logging.exception('This file has no implementation method')
    except Exception as e:
        logging.exception(e)

