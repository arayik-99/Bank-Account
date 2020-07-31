class Customer:

    """
    A class used to represent the customer.
    """
    
    def __init__(self,first_name,last_name,cust_password,cash,balance=0):
        """
        Parameters
        ----------
        first_name: str

            The name of the customer

        last_name: str

            The surname of the customer

        cust_password: int

            Customer's bank PIN 

        cash: int

            Cash money, which the customer currently has

        balance: int (def. is set to 0)
        
            The customer's account balance



        """
        self.first_name = first_name
        self.last_name = last_name       
        self.cash = cash      
        self.balance = balance
        self.cust_password = cust_password
       
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    


class Account:

    

    def __init__(self,acc_name,acc_balance,acc_cash):
        self.acc_name = acc_name
        self.acc_balance = acc_balance
        self.acc_cash = acc_cash        

        


    def bank_password(self,m_password):
        self.main_password = m_password
        self.password = ' '
        self.err_count = 0
        self.tries = 3   
        self.not_blocked = True
        while self.not_blocked and self.password != self.main_password:              
            self.password = int(input("Write your PIN: "))
            self.err_count+=1
            self.tries-=1
            if self.password != self.main_password:
                print(f"You have {self.tries} tries left")                
                if self.err_count == 3 and self.tries == 0:
                    print("You bank account has been suspended. Please contact your bank for support.")
                    self.not_blocked = False


            elif self.password == self.main_password:
                self.bank_main()        

    def bank_main(self):
        print('\n')        
        print(f"Welcome {self.acc_name} \n")
        print(f"Account balance: {self.acc_balance} $ \n")
        print("Withdrawal: 1 \n")
        print("Deposit: 2 \n")
        print("Exit : 0")
        self.choose_dep_with()
        
    def choose_dep_with(self):
        self.choice =  ' '
        while self.choice not in ['0','1','2']:
            self.choice = input()
            if self.choice not in ['0','1','2']:
                print("Please choose Withdrawal or Deposit")       
        
        if self.choice == '1':
            self.withdraw()
                
        elif self.choice == '2':
            self.deposit()
        else:
            exit()       
                    

    def withdraw(self):
        print(f"Your current balance : {self.acc_balance}")
        self.wtd_amm = int(input("Please write the ammount of money you want to withdraw: "))
        if self.wtd_amm > self.acc_balance:
            print("Withdrawal refused. Funds not available.")
            print("Please take your card.")
            exit()
        elif self.wtd_amm <=self.acc_balance:
            self.acc_balance-=self.wtd_amm
            self.acc_cash+=self.wtd_amm
            print(f"Your current balance: {self.acc_balance}")

    def deposit(self):
        self.dep_amt = int(input("Write the amount of money you want to deposit: "))
        if self.dep_amt>self.acc_cash:
            print("Deposit refused. Funds not available.")
            print("Please take your card.")
        elif self.dep_amt <= self.acc_cash:
            self.acc_cash-=self.dep_amt
            self.acc_balance+=self.dep_amt

    def current_cash(self):
        
        return self.acc_cash

    def current_balance(self):

        return self.acc_balance
    




                    #name    surname   PIN    cash    balance
person_1 = Customer("Name", "Surname", 5516,   110,     200)
acc= Account(person_1,person_1.balance,person_1.cash)
acc.bank_password(person_1.cust_password)
person_1.balance = acc.current_balance()
person_1.cash = acc.current_cash()
print(f"Current balance : {person_1.balance}")
print(f"Current cash : {person_1.cash}")