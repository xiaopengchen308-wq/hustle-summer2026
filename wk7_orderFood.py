# ============================================================
# LAB 7  -  MY OWN ORDERING APP
# Week 7  -  Hack the Hood
# ============================================================
# Name: ___xiaopeng_______________
#
# This is YOUR app. YOU write the code.
# Do the tickets IN ORDER from the Lab 7 sheet.
# Run this file after EVERY ticket to check your work.
#
# My store sells: ___food______________________________________
# ============================================================


# ============================================================
# DAY 1  -  BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint
#   A class for your item. Every item has a name and a price.
#   Write your class below.
class food:
    def __init__(self,name,price):
        self.name=name
        self.price=price



# TICKET 3: The price guard
#   Add a set_price method INSIDE your class above.
#   It should say no to a price below zero.
#   BREAK ON PURPOSE: after you build it, try item1.set_price(-5)
#   PREDICT what happens: ______________
#   Paste the message you see here: ______________
    def set_price(self,amount):
        if amount<0:
            print("price cannot be nagative")
        else:
            self.price= amount

# TICKET 4: A second kind of item
#   A new class that copies (inherits from) your first class.
#   Write it below.
class drinks(food):
    def __init__(self,name,price):
        self.name=name
        self.price=price



# TICKET 5: Each item's own action
#   Give each class its own method (deliver, serve, play...).
#   Same method name, different message.
#   EXPLAIN why the same name can do two things: ______________
    def deliver(self):
        print(f"Delievering your {self.name}!")

    def deliver(self):
        print(f"Delievering your {self.name} drinks!")


# TICKET 2: Make your real items
#   Make 2 or 3 real items with YOUR OWN names and prices.
#   PREDICT what print(item1.name) shows: ______________
item1=food("burger",15)
item2=food("pizza",5)




# ============================================================
# DAY 2  -  BUILD YOUR STORE
# ============================================================

# TICKET 6: My cart
#   A class that holds items in a list and can check out.
#   Write your Cart class below.
class cart:
    def __init__(self):
        self.items=[]
    
    def add(self,item):
        self.items.append(item)
        print(f"{item.name} added")


# TICKET 9: Checkout  (add this method INSIDE your Cart class)
#   Deliver every item and add up the total.
    def checkout(self):
        total = 0
        for item in self.items:
            total += item.price
            print(f"Total: ${total}")

# TICKET 7: My menu and my cart
#   A dictionary that gives each item a number, and one empty cart.
store={
    "1":item1,
    "2":item2
}


# TICKET 8: Let customers shop
#   Use input() and a loop to keep adding picks until "done".
#   PREDICT what happens when you pick 1: ______________

cart=cart()
while True:
    choice = input("Pick 1, 2, or 'done': ")
    if choice == "done":
        break
    elif choice in store:
        cart.add(store[choice])
    else:
        print("Invalid choice.")




# TICKET 10: Test the whole app
#   Run it start to finish. PREDICT the full output first,
#   then check it against what really prints.
'''
first will ask pick 1,2 or done
then once you pick 1 if will print burger added 
if you pick 2 would print pizza added 
if you pick done the code will stop running


'''
# ============================================================
# CHALLENGE: add a THIRD kind of item, or your own feature!
# ============================================================
#lab 7 Extension 
#ticket 1
import random

welcome=["welcome in", "welcome for the shopping with us","hi, hope you had a good day here"]
print(random.choice(welcome))

'''
ticket 2
the set_price method is at ticket 3 for the original lab 7
'''
item1.set_price(100)
item2.set_price(80)
print(item1.name + " - $ " + str(item1.price))

#ticket 3
print("Menu:")

for number, item in store.items():
    print(number + ": " + item.name + " - $" + str(item.price))

#ticket 4
while True:
    choice = input("pick an number to order or type done : ")

    if choice =="done":
        break
    elif choice in store:
        cart.add(store[choice])
    else:
        print("sorry, thats not on the menu")

#ticket 5
print("receipt :")

for item in cart.items:
    print(item.name +" "+ str(item.price))


#ticket 6
print("you bought" +" "+ str(len(cart.items))+" "+ "items")

print(cart.checkout())

