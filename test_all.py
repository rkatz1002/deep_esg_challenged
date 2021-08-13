import pytest

import settings

from GeneralLedgerDTO import GeneralLederDTO
from ExcelUtil import ExcelUtil


def test_if_gets_correct_values_of_children():
    settings.answ_xlsx = "chart_of_accounts_test.xlsx"
    settings.general_ledgers_xlsx = "general_ledger_test.xlsx"
    from DBReader import DBReader
    db_reader = DBReader()
    children = db_reader.get_children_values('1')
    assert children == [ 7, 8, 1, 2, 10, 6, 2, 4, 1, 6, 9, 10, 8, 9, 1, 4, 7, 7, 10, 9]

def test_if_gets_correct_values_from_account_number():
    settings.answ_xlsx = "chart_of_accounts_test.xlsx"
    settings.general_ledgers_xlsx = "general_ledger_test.xlsx"
    from DBReader import DBReader
    db_reader = DBReader()
    values = db_reader.get_values_from_account_number('1.3.1.3')
    correct_values = [10.0, 6.0, 6.0, 10.0, 9.0, 7.0]
    assert values == correct_values

def test_if_account_are_distinct():
    settings.answ_xlsx = "chart_of_accounts_test.xlsx"
    settings.general_ledgers_xlsx = "general_ledger_test.xlsx"
    from DBReader import DBReader
    db_reader = DBReader()
    accounts = db_reader.get_distinct_accounts()
    accounts_set = list(set(accounts))
    assert len(accounts)==len(accounts_set)
