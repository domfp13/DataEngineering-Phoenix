import os
import itertools
import csv
from io import StringIO
from google.cloud import storage

def generateExcelColumns(counterbegin = 0, sizeOfColumns = 1):
    '''
    This function returns a dictionary {'A':0, 'B':1 ..... 'AA':26 .... 'ZZ'}
    @counterbegin default number is 0 so the dictionary returned starts a 0 = {'A': 0}
    @sizeOfColumns default number is 2 so the dictionary returned is from A-Z if a more columsn need set it to 3 {'A-ZZ':}
    '''
    counter = counterbegin
    # This creates the permutations like Repeating letters like excel columns
    columnsUpTo2Letters = list(itertools.chain(*[itertools.product(map(chr, range(65,91)), repeat=i) for i in range(1, sizeOfColumns+1)]))
    columsdic = {}

    for element in columnsUpTo2Letters:
        if len(element) == 1:
            columsdic[element[0]] = counter
        else:
            columsdic[element[0]+element[1]] = counter
        counter += 1
    
    # Force to clean the memory 
    columnsUpTo2Letters = None

    return columsdic

def getDataFromTLKPOrderClientData(dictionary):
    '''
    This function get the T_LKP_ORDER_CLIENT_DATA.csv
    dictionary {'name':'t_lkp_order_client_data/T_LKP_ORDER_CLIENT_DATA.csv', 'bucket':'dw_file_export'}
    Return List
    '''
    table = []
    
    try:
        storage_client = storage.Client()
        with StringIO(storage_client.bucket(dictionary['bucket']).get_blob(dictionary['name']).download_as_string().decode('utf-8')) as file:
            
            csvreader = csv.reader(file)

            # This skips the first row of the CSV file.
            # csvreader.next() also works in Python 2.
            next(csvreader)
            
            for row in csvreader:
                table.append(row)
    except Exception as e:
        print(e)
        return table
    else:
        return table

def sortingList(list):
    return sorted(list, key = lambda element: list[0])

def customerNameLinearSearch(customerName, list):
    value = ''
    for element in list:
        if element[0].replace(" ","") in customerName.replace(" ",""):
            value = element[1]
    return value

def decoratorGetPath(function):
    def wrapper(file_name:str):
        from pathlib import Path
        return Path('/tmp',file_name)
    return wrapper
@decoratorGetPath
def getPath(file_name:str):
    """Decorator, returns the path depending if testing is local or in the cloud

    Args:
        file_name (str): file_name based name
    
    Returns:
        Path: object Path depending if decorator has been turned on
    """
    from os import getcwd
    from pathlib import Path
    return Path(getcwd(), file_name)