
# class car:
#     def __init__(self, brand):
#         self.brand = brand
#     def display(self):
#         print(self.brand)

# car1 = car("vw")
# car1.display()
# print(car1.brand)

#Create a program to store a student's name, age, and course and display the student's details.

# class Student:
#     def __init__(self,name,age,course):
#         self.name = name
#         self.age = age
#         self.course = course
#     def display(self):
#         print(f"Student name is {self.name} age {self.age} & course is {self.course}")

# student1 = Student("Fasil",30,"Btech")
# student1.display()

#Create a banking program that allows a user to deposit money, withdraw money, and check the account balance.

# class Bank:
#     def __init__(self,balance):
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance = self.balance + amount
#         print("amount deposited")
#     def withdraw(self, amount):
#         self.balance = self.balance - amount
#         print("amount withdraw completed")
#     def display(self):
#         print(f"Account balance is {self.balance}")

# obj = Bank(5000)
# obj.deposit(350)
# obj.withdraw(200)
# obj.display()

#Create a banking program where the account balance cannot be directly changed by the user.
#Provide operations for deposit, withdrawal, and checking the balance.

class Bank:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print("amount deposited")
    def withdraw(self, amount):
        self.__balance = self.__balance - amount
        print("amount withdraw completed")
    def display(self):
        print(f"Account balance is {self.__balance}")

obj = Bank(5000)
print(obj.__balance)
obj.deposit(250)
obj.display()