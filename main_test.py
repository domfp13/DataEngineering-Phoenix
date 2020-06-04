import main 
from etl.functions import getPath

def test():
    """
    simulates how the cloud function is triggered.
    :return:
    {
        "name": "global/SynnexCUCLenovoForecastRIORecap.xls",
        "bucket": "app-script-data-extraction"
    }
    """
    main.process_vendor_excel_files({'name':'global/DBI_LOAD_0003.xlsx',
             'bucket':'app-script-data-extraction'}, 'context')

test()