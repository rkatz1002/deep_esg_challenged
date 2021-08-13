class GeneralLederDTO:

    account_number:str
    value:float
    number_of_levels:int
    levels:list

    def __init__(self, account_number:str, value:float) -> None:
        self.account_number = account_number
        self.value = value
        self.number_of_levels = account_number.count(".") + 1
        self.levels = [s.lstrip("0") for s in account_number.split(".")]