print("hello word");


print("this is input " ,x)
print(10+3)
print(round(10/3))
print(10+3)
print(10-3)
print(10**2)
print(10//2)




# 1 Input and Output

name = input("Enter your name: ")
print("Hello, " + name + "!")

# Output Formatting

age = 25
print("My age is {}".format(age))



# 2Conditional Statements


# If-else statement
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

result = "Even" if x % 2 == 0 else "Odd"
print(result)



#  3Loops
# For loop

for i in range(5):
    print(i)

# While loop
count = 0
while count < 3:
    count += 1
    print("Count:  ",count)





# 4.Lists and Arrays


fruits = ["apple", "banana", "cherry"]
print(fruits[1]) 
fruits.append("orange")  
print(fruits)


# import numpy as np
arr = np.array([1, 2, 3, 4,63,7])
print(arr)



#5Functions


# Function definition
def greet(name):
    return "Hello, " + name + "!"

# Function call
message = greet("Alice")
print(message)


# 6.Dictionaries

person = {"name": "John", "age": 30, "city": "New York"}
print(person["age"])  # Accessing values
person["job"] = "Engineer"  
print(person)  # Accessing values
