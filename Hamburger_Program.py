# Trevor Schoeny, Austin Caprio, Braden Terry, Bradford Paul

# This program defines a queue of customers in line and a dictionary of how many burgers each customer eats.
# It then tracks exactly how many hamburgers each customer eats over the course of a number of orders.

from Hamburger_Classes import Order, Person, Customer

queCustomers = []

dictCustomers = {}

iNumCust = input("How many customers would you like to add? ")

# for iCount in range(0, iNumCust) :

sCustomer = input("Enter the customer name: ").upper()
iBurgers = input("Enter the number of burgers: ")

if sCustomer in dictCustomers :
    dictCustomers[sCustomer].burger_count += iBurgers

