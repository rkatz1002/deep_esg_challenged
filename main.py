import tqdm as tqdm

from GeneralLedgerDTO import GeneralLederDTO

from DBWriter import DBWriter
from DBReader import DBReader

if __name__ == "__main__":

    db_reader = DBReader()
    db_writer = DBWriter()

    ##########################################
    # get distinct acounts in reversed order #
    ##########################################

    # if accounts where not in reversed order, it is possible that the sum ocurres two times

    distinct_accounts = list(reversed(sorted(db_reader.get_distinct_accounts(), key=len)))

    distinct_account:str

    for distinct_account in tqdm.tqdm(distinct_accounts):

        value:float

        # get subaccounts (children) of a certain account
        children     = db_reader.get_children_values(distinct_account) 
        has_children = children != []
        
        if has_children:
            value = sum(children)
        else:
            value = sum(db_reader.get_values_from_account_number(distinct_account))
        
        general_ledger_dto = GeneralLederDTO(
            account_number=distinct_account,
            value=value
        )

        db_writer.save_ledger_value(general_ledger_dto)



