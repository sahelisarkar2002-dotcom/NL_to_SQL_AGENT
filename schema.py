DATABASE_SCHEMA = """

DATABASE: loan_db


TABLE: loans

Columns:
- Loan_ID VARCHAR(100) PRIMARY KEY
- LoanAmount INT
- Loan_Amount_Term INT
- Loan_Status VARCHAR
- ApplicationDate DATE


TABLE: customers

Columns:
- custID VARCHAR(100) PRIMARY KEY
- Loan_ID VARCHAR(100)
- Gender TEXT
- Married VARCHAR
- Dependents INT
- Education TEXT
- Self_Employed VARCHAR
- ApplicantIncome INT
- CoapplicantIncome INT
- Credit_History BOOLEAN
- Property_Area TEXT


RELATIONSHIP:

customers.Loan_ID = loans.Loan_ID


TABLE: DepositCustomers

Columns:
- CustID VARCHAR(100) PRIMARY KEY
- DepositAmt INT


RELATIONSHIP:

DepositCustomers.CustID = customers.custID


TABLE: highCreditCardBalanceCustomers

Columns:
- CustID VARCHAR(100) PRIMARY KEY
- CCBalance INT
- Card_Type TEXT


RELATIONSHIP:

highCreditCardBalanceCustomers.CustID = customers.custID

"""