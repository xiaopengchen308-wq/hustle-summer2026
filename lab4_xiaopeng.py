#xiaopeng | lab 4 | Intro to pyton


#ticket 1
ages = [17,11,25,13,9]
for age in ages:
    if age >=13:
        print("Access granted")
    else:
        print("too young")
# 17, 13 and 25 will run "access granted and 11 and 9 will run too young"
# the age hold one number from the list each time the loop runs


#ticket 2
keep_checking = "yes"

while keep_checking == "yes":
    get_age= int(input("what is your age?"))
        
    if get_age >=13:
        print("access the platform")
    else:
        print("too young")
    keep_checking = input("Chekcing another?")
    

# if you type "no" the code would be an error
# while loop is better because that you don't know how many ages is the user gonna do


#ticket 3
while True:
    age = input("enter and age or type stop")
    if age == "stop":
        break
    age=int(age)
    if age >= 13:
        print("access the platform")
    else: 
        print("too young")
        
# I don't think missing a break is gonna loop forever, I think the code will still work if you type in number but if you type "stop" it won't stop or maybe giving an error 
# the differences between those two is the keyword, for ticket 2 you can type anything to stop the code, and for ticket 3 you have to type "stop" to stop


#ticket 4

def can_access(age):
    if age >= 13:
        return True
    else:
        return False
    
ages = [17,11,25,13,9]
for age in ages:
    if can_access(age):
        print(f"{age} Access granted")
    else:
        print(f"{age} too young")
# the age rule is inside of the can_access function
# is better to putting check inside a function, because if you use function you don't have to rewrite the if/else everytime


#ticket 5

def signup_report(signups):
    approved =0
    for age in signups:
        if can_access(age):
            print(f" age {age} access granted")
            approved=approved+1
        else:
            print(f" age {age} too young")
     
    print(f"Approved: {approved} out of {len(signups)}")

signups= [22, 10, 15, 8, 19, 13]
signup_report(signups)

# is going to be 4 of 6 approved
# I use fof loops, conditions, if/else statement, and function

