class Wallet():

    # first thing to run when we make a new class
    # outline required user-provided input values here 
    # parameters with default values assigned are optional
    def __init__(self, initial_amount=0):
        # save the user provided initial amount as an attribute
        # self refers to whatever obkect I'm working with
        self.balance = initial_amount
    
    # spend cash METHOD

    def spend_cash(self, amount):
        # if self.balance <= amount:
        # this upper comment was a purposefully made error in the code
        if self.balance < amount:            
            return 'Not enough money'
        else:
            self.balance = self.balance - amount
            return f'Remaining balance: ${self.balance}'
    
    # add cash METHOD 

    def add_cash(self, amount):
        self.balance = self.balance + amount
        return f'New balance of: ${self.balance}'

    # __repr__ method
    # changes how the 'object' looks when it is printed out

    def __repr__(self) -> str:
        return f'Wallet with balance of ${self.balance}'



if __name__ == '__main__':
    wallet1 = Wallet(100)
    # print(wallet1.spend_cash(120))
    # print(wallet1.spend_cash(60))
    # print(wallet1.balance)
    # print(wallet1.add_cash(60))
    # print(wallet1.spend_cash(180))
    # print(wallet1.spend_cash(120))
    # print(wallet1.balance)
    # print(wallet1)
    wallet2 = Wallet(50)
    wallet3 = Wallet(300)
    # print(wallet1)
    # print(wallet2)
    # print(wallet3)
    wallet4 = Wallet()
    # print(wallet4)