class Bank:
    def __init__(self):
        self.amount=0
        print("The account is created")

    def deposit(self,Amount):
       self.amount += Amount
       print("Amount successfully Deposited")

    def withdraw(self,Amount):
        if (self.amount - Amount >= 500):
            self.amount -= Amount
            print("Amount successfully Withdrawn")
        else:
            print("Insufficient Balance")
        

    def enquiry(self):
        print("Balance in the account is:",self.amount)

a = Bank()
for i in range (0,50):
    print ("""1.Deposit \n  2.Withdraw \n 3.Enquiry \n 4.Exit """)
    p = int(input("Enter your choice:"))
    if(p==1):
        Amount= float(input("Enter amount to be deposited:"))
        a.deposit(Amount)
    elif(p==2):
         Amount= float(input("Enter amount to be withdrawn:"))
         a.withdraw(Amount)
    elif(p==3):
        a.enquiry()
    elif(p==4):
        exit()
    else:
        print("Enter a correct choice")