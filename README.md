# DEEP ESG - Data Challenge - Solution


#### Idea Behind the Solution

For the problem to be solved, it is important that we make sure that minimal data of the *general_ledger.xlsx* file is stored in-memory. With this in mind, we can keep the values of *chart_of_account.xlsx*  in-memory since its size is somewhat constant and is not considerable.

Thus, we procured a solution that would use minmal in-memory data possible.

#### Algorithm

To run the program, we use the following algorithm:

1. Get all possible accounts (and sub-accounts) in order
   1. must be in reversed order
   2. Must not have repetition
   3. these values will be stored in-memory
   4. Leading zeros in accounts are considered as different
2. for each account
   1. check if has sub-accounts (children)
   2. if has children
      1. sum values of children
      2. put sum in table
   3. else if not have children
      1. sum all accounts
      2. put sum in table

Notice that, we only store momentarily any data received from the *general_ledger.xlsx* file.

#### Architecture

- The *main.py* file is an entry point to the project - and thus can be disconsidered.
- *DBReader.py* and *DBWriter.py* are the files that handle reading and writing in the database. If the program ever migrates to SQL databases or others they will be the only ones that need to be edited.
- *test_all.py* stores all tests. Since there aren't a lot of functions to test, it may only be simple functions - yet if the project extends it will need to be changed in seperate test modules
- *settings.py* has basic test settings, with *DEBUG* variable and file names of input and output
- *GeneralLedgerDTO.py* is a basic data transfer object to enhance readability

#### Possible Flaws

* The algorithm considers that inputs with a different quantity of leading zeros distinguish two accounts - yet that may not be the case. If such, query searches should compare without leading zeros, thus only needing modifications in *DBWriter.py*
* the number of accounts is considered to be storable in memory - this solution would have to change if the number of accounts grows considerably. If such happens, it is important to implement this solution in an sql database and use the column already accounted for (see next section).

#### Implemting a SQL Database

For this, there will only be two tables needed - ChartOfAccounts and GeneralLedgers. They can be defined as:

###### ChartOfAccounts

* account number (str)
* value (int)

###### GenerealLedgers

* account number (str)
* value (int)
* already accounted for(bool)

Notice that the table account number and value are redundant - but useful to update the speed of our program, since to get these value from the table GeneralLedgers is time consuming. 

The boolean already accounted for is useful to filter our table of GeneralLedgers if we ever want to update the table ChartOfAccounts.

The value fields should be the respective value times 100, so there are no floating point arithmetic rounding errors.
