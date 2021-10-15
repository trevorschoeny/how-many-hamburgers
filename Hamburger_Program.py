# Trevor Schoeny, Austin Caprio, Braden Terry, Bradford Paul

# This program defines a queue of customers in line and a dictionary of how many burgers each customer eats.
# It then tracks exactly how many hamburgers each customer eats over the course of a number of orders.

from Hamburger_Classes import Order, Person, Customer


# The following are two dictionary scenarios. Both work and either can be used based on the needs of the project.

#------------------1. Dictionary where all Customer keys are already created----------------------------------------------------------------------


dictCustomers = {"Jefe" : 0, "El Guapo" : 0, "Lucky Day" : 0, "Ned Nederlander" : 0, "Dusty Bottoms" : 0, "Harry Flugleman" : 0, "Carmen" : 0, "Invisible Swoardsman" : 0, "Singing Bush" : 0}

oCust = Customer()

# Add the burger count from their order to their total burgers dictionary value

dictCustomers[oCust.customer_name] += oCust.order.burger_count


#------------------2. Empty Dictionary where Customers need to be added still----------------------------------------------------------------------


dictCustomers = {}

oCust = Customer()

if oCust.customer_name in dictCustomers:

    # Search the dictionary to see if the customer already has an existing key. 
    # If so, add the burger count from their order to their total burgers value.

    dictCustomers[oCust.customer_name] += oCust.order.burger_count

    # If they don't have an existing key, create one using their name and add
    # their burger count as a start to their total burgers value.

else : dictCustomers[oCust.customer_name] = oCust.order.burger_count

# QUEUE
queueCustomers = []
for iCount in range(0, 100) :
    oCustomer = Customer()
    queueCustomers.append(oCustomer)
