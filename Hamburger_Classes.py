# Trevor Schoeny, Austin Caprio, Braden Terry, Bradford Paul
# This program defines the Order, Person, and Customer classes.

import random

class Order() :

    # Defines burger_count and assigns it a random number between 1 and 20
    def __init__(self) :
        self.burger_count = self.randomBurgers()
    
    # Returns a random number between 1 and 20
    def randomBurgers(self) :
        return random.randint(1, 20)
    
class Person() :
    
    # Gives the cutomer a random name
    def __init__(self) :
        self.customer_name = self.randomName()
    
    # Returns a random name
    def randomName(self) :
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(asCustomers)

class Customer(Person) :

    # Gives Customer a name and an Order
    def __init__(self) :
        super().__init__()
        self.order = Order()