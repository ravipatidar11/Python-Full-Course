#Others3.py<------Program<--Data Abstraction

from Account3 import Account

ac=Account() # Object Creation
ac.get_acc_det() # Can't Calling Instance Method bcoz it is Encapsulated
print("-"*50)
print("Account Number:",ac.acno)
print("Account Holder Name:",ac.cname)
print("Account Balance:",ac.bal)
print("Account PIN:",ac.pin)
print("Account Branch Name:",ac.bname)
print("-"*50)
