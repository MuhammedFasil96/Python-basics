###

#q2
# age = int(input("enter the age of the person:"))

# if age>=18:
#     print("Eligible")
# else:
#     print("Not Eligible")

# #q3

# num = int(input("enter the number:"))

# if num%5 == 0:
#     print("Divisible by 5")
# else:
#     print("Not Divisible by 5")


#q5

# temp = int(input("enter the temperature:"))

# if temp>32:
#     print("Hot")
# else:
#     print("cool")
    
# #q5

# num1 = int(input("enter the number 1:"))
# num2 = int(input("enter the number 2:"))

# if num1>num2:
#     print("Largest number is" , num1)
# else:
#     print(num2)


#q12

# password = "pwd123"

# pwd = input("enter the password:")

# if password == pwd:
#     print("Login successful")
# else:
#     print("Login not successful")

# #q14
# import sys
# hr = int(input("enter the current hour in 24 hr format:"))

# if(hr<0 or hr>24):
#     print("Invalid entry")
#     sys.exit(1)

# if 9<hr<18:
#     print("shop is open")
# else:
#     print("shop is not open")

# #q16

# marks = int(input("enter the mark:"))

# if 90<=marks<=100:
#     print("A")
# elif 75<=marks<90:
#     print("B")
# elif 60<=marks<75:
#     print("C")
# elif 40<=marks<59:
#     print("D")
# else:
#     print("Failed")



#q17

# age = int(input("enter the age:"))

# if age<5:
#     print("Ticket is free")
# elif 5<=age<=12:
#     print("Pay 10 rs")
# elif 13<=age<=59:
#     print("Pay 20 rs")
# else:
#     print("pay 12 rs")

#q23

# amount = int(input("Enter the total price: "))

# if amount>=5000:
#     discount = (amount *20)/100
#     amount -= discount
#     print("price after discount, Pay", amount)
# elif 2000<=amount<5000:
#     discount = (amount *10)/100
#     amount -= discount
#     print("price after discount, Pay", amount)
# else:
#     print("No discount! Pay: ", amount)
    

#q25

# salary = int(input("Enter the employee salary: "))

# if salary>=50000:
#     bonus = (salary *20)/100
#     salary += bonus
#     print("Bonus: ", bonus , "Total salary", salary)
# elif 20000<=salary<50000:
#     bonus = (salary *10)/100
#     salary += bonus
#     print("Bonus: ", bonus , "Total salary", salary)
# else:
#     bonus = (salary *5)/100
#     salary += bonus
#     print("Bonus: ", bonus , "Total salary", salary)

#q24

inp = input("Enter the character:")

if 'A' <= inp <= 'Z':  
    print("Uppercase")
elif('a' <= inp <= 'z'):
    print("Lowercase")
elif('0' <= inp <='9'):
    print("digit")
else:
    print("special character")
    
    

