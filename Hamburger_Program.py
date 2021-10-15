# Trevor Schoeny, Austin Caprio, Braden Terry, Bradford Paul

# This program defines a queue of customers in line and a dictionary of how many burgers each customer eats.
# It then tracks exactly how many hamburgers each customer eats over the course of a number of orders.

from Hamburger_Classes import Order, Person, Customer

queueCustomers = []
for iCount in range(0, 100) :
    oCustomer = Customer()
    queueCustomers.append(oCustomer)
 
dctCustomers = {}

