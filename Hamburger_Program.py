# Trevor Schoeny, Austin Caprio, Braden Terry, Bradford Paul

# This program defines a queue of customers in line and a dictionary of how many burgers each customer eats.
# It then tracks exactly how many hamburgers each customer eats over the course of a number of orders.

# import other pages
from Hamburger_Classes import Order, Person, Customer

# create the dictionary of customer names
dictCustomers = {}
# create QUEUE
queueCustomers = []

# this loop adds 100 customers to the queue
for iCount in range(0, 100) :
    oCust = Customer()

    if oCust.customer_name in dictCustomers:
    # Search the dictionary to see if the customer already has an existing key. 
    # If so, add the burger count from their order to their total burgers value.
        dictCustomers[oCust.customer_name] += oCust.order.burger_count
    # If they don't have an existing key, create one using their name and add
    # their burger count as a start to their total burgers value.
    else : dictCustomers[oCust.customer_name] = oCust.order.burger_count

    # add the customer object with name and number of burgers to the queue
    queueCustomers.append(oCust)