#snippet 1
#(1)I think this is a zerodivisionError, because it set y as 0 and x/y
x=10
y=10
result=x/y
print("Result:", result)

#snippet 2
#I think this is a indexError, because you cant update your code inside of a print statement
numbers = [1,2,3,4,5]
for i in range(len(numbers)):
    print(numbers[i])
    i+1

#snippet 3
# I think this is a syntaxError, missing a colon for the function 
def calculate_area(radius):
    area= 3.14 * radius **2
    return area

radius = 5
print(calculate_area(radius))

#snippet 4
#it is a syntax error. missing colon for if/else statement
def is_even(number):
    if number % 2==0:
       return True
    else :
       return False
print(is_even(4))
print(is_even(7))

#snippet 5
#syntax error. missing colon
for i in range(5):
     print(i)

#snippet 6
#logic error, no errors for the code but it may do something unexpected 
def greet(name):
    return "Hello "+ name 
print(greet("Alice"))

#snippet 7
#indentation error , the update is not in the loop 
numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total += number
print("Sum of numbers:", total)

#snippet 8
#logic error, code works but doing something unexpected 
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n -1)

print(factorial(5))


#snippet 9
#logic error, doing unexpected things
'''
name = input("Enter your name: ")
if name == "Alice" or  name=="Bob":
    print("Hello, " + name)
else:
    print("Hello, stranger!")
'''
#snippet 10
#zerodivision error and logic error
def divide_numbers(x, y):
    if x==0 or y == 0:
        return "error"
    result = x/y 
    return result

num1 = 10
num2 = 0
print(divide_numbers(num1, num2))
