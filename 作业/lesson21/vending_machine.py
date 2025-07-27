class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'Please add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'Please add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self, product, price):
        """Set the product and its price, as well as other instance attributes."""
        self.product=product
        self.price=price
        self.remain=0
        self.balance=0

    def restock(self, n):
        """Add n to the stock and return a message about the updated stock level.

        E.g., Current candy stock: 3
        """
        self.remain+=n
        print("Current "+self.product+" stock: "+str(self.remain))

    def add_funds(self, n):
        """If the machine is out of stock, return a message informing the user to restock
        (and return their n dollars).

        E.g., Nothing left to vend. Please restock. Here is your $4.

        Otherwise, add n to the balance and return a message about the updated balance.

        E.g., Current balance: $4
        """
        if self.remain==0:
            print("Nothing left to vend. Please restock. Here is your $"+str(n))
        else:
            self.balance+=n
            print("Current balance: $"+str(self.balance))


    def vend(self):
        """Dispense the product if there is sufficient stock and funds and
        return a message. Update the stock and balance accordingly.

        E.g., Here is your candy and $2 change.

        If not, return a message suggesting how to correct the problem.

        E.g., Nothing left to vend. Please restock.
              Please add $3 more funds.
        """
        if self.remain<=0:
            print("Nothing left to vend. Please restock.")
        elif self.balance==self.price:
            self.remain-=1
            self.balance-=self.price
            print("Here is your "+str(self.product)+".")
        elif self.balance>self.price:
            self.remain-=1
            self.balance-=self.price
            print("Here is your "+str(self.product)+" and $"+str(self.balance)+" change.")
            self.balance=0
        elif self.balance<self.price:
            print("Please add $"+str(self.price-self.balance)+" more funds.")