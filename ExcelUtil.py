
import pandas as pd
import openpyxl
import numpy as np

import os

from GeneralLedgerDTO import GeneralLederDTO
from settings import *


class ExcelUtil:

    def add_value_in_excel(self, value_to_add, row_index, column_index):
        
        srcfile = openpyxl.load_workbook(answ_xlsx, read_only=False)
        df = pd.read_excel(answ_xlsx)
        already_existing_value = 0 if np.isnan(df.loc[row_index-2]['value']) else df.loc[row_index-2]['value']
        value = already_existing_value + value_to_add
        sheetname = srcfile.get_sheet_by_name('Exc_PC')#get sheetname from the file
        sheetname.cell(row=row_index,column=column_index).value = value
        srcfile.save(answ_xlsx)
    
    def read_from(self, filename:str):
        """
            args:
                -filename (str)
            returns pd data frame of file
        """

        return pd.read_excel(filename, engine='openpyxl')