
import pandas as pd
import openpyxl
import numpy as np


from GeneralLedgerDTO import GeneralLederDTO
from ExcelUtil import ExcelUtil
import settings

class DBWriter:

    excel_util = ExcelUtil()

    def save_ledger_value(self, general_ledger_dto:GeneralLederDTO):

        """
            args:
                - general_ledger_dto (GeneralLederDTO)
            save ledger value into the excel spreadsheet chart_of_accounts.xlsx
            
            If value is not in chart_of_accounts raises error. If value already exists in chart of accounts, it 
            is added to the previous value.
        """

        df = pd.read_excel(settings.answ_xlsx)

        row_index    = int(np.flatnonzero(df['account'] == general_ledger_dto.account_number)[0])+2
        column_index = 2

        self.excel_util.add_value_in_excel(
            general_ledger_dto.value,
            row_index,
            column_index
        )