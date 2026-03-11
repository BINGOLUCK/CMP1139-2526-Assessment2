""" medication.py
contains the medication class 
"""


class Medication():
    def __init__(self, name, amount_in_stock):
        """
        Medication __init__
        
        :param self
        :param name (string): the name of the medication
        :param amount_in_stock: how much of this medication is in stock
        """
        self.name = name
        self.amountInStock = amount_in_stock

        # Observer pattern 
        self.observers = []
        
    def add_observer(self, prescription):
        self.observers.append(prescription)
                              
    def remove_observer(self, prescription): 
        if prescription in self.observers:
           self.observers.remove(prescription) 

    def notifiy_observers(self):
        for observer in self.observers:
            observer.update(self.stock)


    def restock(self, amount):
        """        
        :param self
        :param amount (int): The amount to increase the stock by
        """
        self.amountInStock += amount
        self.notifiy_observers() 

    
    def reduce_stock(self, amount):
        self.amountInStock -= amount


    def has_enough_stock(self, dosage):        
        """ Checks if there is enough stock for the given dosage.   
        :param self
        :param dosage (int): The dosage to be checked.
        :returns True or False
        """
        return self.amountInStock >= dosage
    
    

          
                                                                           