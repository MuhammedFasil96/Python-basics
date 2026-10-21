# def area(a,b):
#     print(a*b)
# length = int(input("Enter the length: "))
# width = int(input("Enter the width: "))
# area(length,width)

# def noofcharacters(string):
#         print(len(string))
        
# str = input("Enter the string: ")
# noofcharacters(str)

#Write a function find_max(numbers) that returns the largest number from a list.

# def find_max(list = []):
#     print(max(list))
    

# list1 = [1,6,33,44,2,99]
# find_max(list1)

#Write a function count_vowels(text) that counts the number of vowels in a string.

# def count_vowels(text):
#     count = 0
#     for i in text:
#         if i in "aeiou":
#             count+=1
#     print(count)

# str = input("Enter the string : ")  
# count_vowels(str)

#Write a function reverse_string(text) that returns the reversed string.

# def reverseString(str):
#     result = ""
#     for i in str:
#         result = i + result
#     return result
# str1 = input("Enter the string : ")  
# print(reverseString(str1))

#Write a function factorial(n) that calculates the factorial of a number.

# def factorial(num):
    
#     if num<0:
#         return -1
#     if num == 0:
#         return 1 
#     factorial = 1
#     for i in range(1, num+1):
#         factorial *= i
#     return factorial
# number = int(input("Enter the number: "))
# print(factorial(number))

#Write a function check_password(password) that checks whether a password has at least 8 characters.

# def check_password(password):
#     count = 0
#     for i in password:
#         count+=1
#     if(count<8):
#         print("Not permitted!! less number of characters")
#     else:
#         print("OK Case")
        
# check_password(input("Enter the password: "))


#  Triangle Validator
# Input three side lengths. Check validity. If valid, print Equilateral, Isosceles or Scalene

# def checkTraingaleDimension(a,b,c):
#     if a < 0 or b < 0 or c < 0:
#         print("Invalid length")
#     else:
#         if(a==b==c):
#             print("Equilateral")
#         elif(a==b or b==c or a==c):
#             print("Isosceles")
#         else:
#             print("Scalene")

# a = int(input("Enter side 1: "))
# b = int(input("Enter side 1: "))
# c = int(input("Enter side 1: "))
# checkTraingaleDimension(a,b,c)

# ATM Simulation
# Balance starts at n10000. Menu: Deposit, Withdraw, Check Balance, Exit. Prevent over-withdrawal.

# def atmsimulation(balance):
#     while True:
#         print("\n--- ATM Menu ---")
#         print("1. Deposit")
#         print("2. Withdraw")
#         print("3. Check Balance")
#         print("4. Exit")
#         choice = input("Enter your option (1-4): ")
#         match choice:
#             case "1":
#                 deposit = int(input("Enter the amount to deposit"))
#                 if(deposit<0):
#                     print("Invalid entry")
#                 else:
#                     balance += deposit
#             case "2":
#                 withdraw = int(input("Enter the amount to withdraw"))
#                 if(withdraw<0):
#                     print("Invalid entry")
#                 else:
#                     balance -= withdraw
#             case "3":
#                 print(f"Balance amount is: {balance}")
#             case "4":
#                 break
        
# balance = 10000
# atmsimulation(balance)

#Print all prime numbers from 1 to 100.

# def prime():
#     for num in range(2, 101):
#         is_prime = True

#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break

#         if is_prime:
#             print(num, end=" ")

# prime()

#Print first N Fibonacci numbers using a for loop.

# def fibonacci(n):
#     if n <= 0:
#         print([])
#         return
#     numbers = [0, 1]

#     for i in range(2, n):
#         next_num = numbers[i - 1] + numbers[i - 2]
#         numbers.append(next_num)

#     print(numbers)

# n = int(input("Enter the number n: "))
# fibonacci(n)


#Print: 1 / 22 / 333 / 4444 / 55555

# def printPattern():
#     for i in range(1,6):
#         for j in range(i):
#             print(i, end = "")
#         print()
    
# printPattern()

#Implement add, subtract, multiply, divide.


# def calculator():
#     number1 = int(input("Enter the first number: "))
#     number2 = int(input("Enter the second number: "))

#     while True:
#         print("\n1. Add")
#         print("2. Subtract")
#         print("3. Multiply")
#         print("4. Divide")
#         print("5. Exit")

#         choice = int(input("Enter your choice: "))

#         match choice:
#             case 1:
#                 result = number1 + number2
#                 print("Result:", result)

#             case 2:
#                 result = number1 - number2
#                 print("Result:", result)

#             case 3:
#                 result = number1 * number2
#                 print("Result:", result)

#             case 4:
#                 if number2 == 0:
#                     print("Cannot divide by zero")
#                 else:
#                     result = number1 / number2
#                     print("Result:", result)

#             case 5:
#                 print("Exiting calculator...")
#                 break
#             case _:
#                 print("Invalid")

# calculator()

#is_palindrome

def palindrome():
    str = input("Enter the string: ")
    result = ""
    for i in str:
        result = i + result
        
    if(str == result):
        print("Palindrome")
    else:
        print("Not palindrome")

palindrome()