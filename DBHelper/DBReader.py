import pandas as pd
import numpy as np

from .BaseDBHelper import BaseDBHelper

from utils.ExcelUtil import ExcelUtil
import settings

class DBReader(BaseDBHelper):

    excel_util = ExcelUtil()

    def get_distinct_accounts(self)->list:
        
        """
            Get all distinct account and subaccount numbers, wihtout order
        """

        distinct_accounts = list(self.excel_util.read_from(settings.answ_xlsx)['account'].values.tolist())
        return distinct_accounts


    def get_values_from_account_number(self, account_number:str):
        
        """
            args:
                -account_number (str): the number of the account

            Will get all the values of a certain account number. This function considers that accounts with
            leading zeroes are different. 
        """

        df = self.excel_util.read_from(settings.general_ledgers_xlsx)
        return df['value'][df['account']==account_number].values.tolist()

    def get_children_values(self, account_number):
        
        """
            args:
                -account_number (str): the number of the account

            Will get all the values of the children (subaccounts) 
            of a certain account number. This function considers that accounts with
            leading zeroes are different. 
        """

        df = self.excel_util.read_from(settings.general_ledgers_xlsx)
        return_val = []
        values = list(df.loc[df['account'].str.startswith(account_number, na=False)]['value'].values)
        for value in values:
            if np.isnan(value):
                return_val.append(0)
            else:
                return_val.append(value)
                
        return return_val
        