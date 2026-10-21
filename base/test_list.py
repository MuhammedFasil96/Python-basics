# list = []

# for i in range(10):
#     list.append(i)

# print(list)
# print(len(list))

# Largest = list[0]
# for i in list:
#     if i>Largest:
#         Largest = i
    
# print(Largest)

# Smallest = list[0]
# for i in list:
#     if i<Smallest:
#         Smallest = i
    
# print(Smallest)


#q2

# list = []

# for i in range(20):
#     list.append(i)
    
# odd = []
# even = []

# for i in range(20):
#     if(i%2):
#         even.append(i)
#     else:
#         odd.append(i)

# print(f"Odd Numbers are {odd} : Even numbers are {even}")

#q3

# list = ["apple", "banana", "orange", "mango", "grapes"]

# list.append("jackfruit")

# list.remove("orange")

# list.sort()

# list.reverse()

# index = 0
# for i in list:
#     if i == "banana":
#         break
#     else:
#         index+=1

# print(index)
# list[index] = "pineapple"

# print(list)

#q4
# numbers = [10, 20, 10, 30, 20, 40, 50, 30]

# unique_list = []

# for i in numbers:
#     if i not in unique_list:
#         unique_list.append(i)

# print(unique_list)


#q5

# list = [10,99 ,44,55,11,54,20, 30, 40, 100,104,50]



# largest = float('-inf')
# second_largest = float('-inf')

# for i in list:
#     if i>largest:
#         second_largest = largest
#         largest = i
#     elif second_largest<i<largest:
#         second_largest = i

# print(second_largest)


#q6

# tuple = (10,33,44,22,77)

# print(max(tuple))

# print(min(tuple))

# sum = 0
# for i in tuple:
#     sum+=i

# print(sum)

# print(len(tuple))

#q7

# tuple1 = (10, 20, 30, 40, 50)

# list = list(tuple1)

# list.append(60)

# tuple1 = tuple(list)
# print(type(tuple1))
# print(tuple1)

#q8

# tuple = (2, 5, 2, 8, 2, 10, 5, 8)

# dict = {}
# for i in tuple:
#     dict[i] = dict.get(i, 0) + 1

# print(dict)

#q9

# details = ["Fasil", 30, "AI/ML", 92]

# name, age , course , mark = details

# print(f"student name {name} age {age} course {course} mark {mark}")

#q10

# tuple1 = (10, 20, 30, 40, 50)
# tuple2 = (30, 40, 50, 60, 70)

# for x in tuple1:
#     for y in tuple2:
#         if x == y:
#             print (x)

#q11

# Create a dictionary containing the names and marks of 5 students.
# Write a program to:
# • Display all students
# • Display all marks
# • Find the student with the highest mark
# • Calculate the average mark
    
# dict = {"Fasil": 66, "Rooby": 55, "Amish": 99}

# print(dict.keys())
# print(dict.values())

# max_mark = float('-inf')

# for i in dict:
#     if dict[i] > max:
#         max = dict[i];
        
# print(max)

# highest_student = max(dict, key=dict.get)
# highest_mark = dict[highest_student]



# print(highest_mark)

# average = 0
# for i in dict:
#     average += dict[i]/len(dict)
# print(average)


#q12

# str = "python is easy and python is powerful"
# dict = {}
# for i in str.split():
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i] = 1

# print(dict)

#q13

# Create a dictionary containing product names and prices.
# Write a program to:
# • Add a product
# • Update a price
# • Delete a product
# • Search for a product
# • Display all products costing more than n500

# product_details = {"polo":10, "i10":8, "i20":11}
# product_details.update({"pajero":15})
# product_details["polo"] = 11.5
# product_details.pop("i10")
# print(product_details["pajero"])
# print(product_details)

# for i in product_details:
#     if product_details[i] > 11:
#         print(i)


    
#q15

# dict1 = {"a": 10, "b": 20, "c": 30}
# dict2 = {"d": 40, "e": 50, "f": 60}

# #dict3 = dict1 | dict2

# dict1.update(dict2)

# print(dict1)

#q16

# A = {10, 20, 30, 40, 50}
# B = {40, 50, 60, 70, 80}
# C = A | B
# print(C)
# # or
# print(A.union(B))

# print(A & B)
# # or
# print(A.intersection(B))

# print(A - B)
# # or
# print(A.difference(B))

# print(A ^ B)
# # or- Returns elements that are in either set, but not in both.
# print(A.symmetric_difference(B))

#q17

# items = ["apple", "banana", "apple", "orange", "banana"]

# result = list(set(items))
# print(result)

#q18

# sentence = input("Enter a sentence")

# words = sentence.lower().split()
# unique_words = set(words)

# print("Unique words:", unique_words)
# print("Number of unique words:", len(unique_words))

#q19

# class_a = {"Arun", "Rahul", "Akhil", "Meera", "Anu"}
# class_b = {"Meera", "Anu", "Vishnu", "Rahul", "Riya"}

# # 1. Students in both classes
# print("Common students:", class_a & class_b)

# # 2. Students only in class A
# print("Only in class A:", class_a - class_b)

# # 3. Students only in class B
# print("Only in class B:", class_b - class_a)

# # 4. All unique students
# print("All unique students:", class_a | class_b)

#q20

sentence = input("Enter a string: ")

vowels = {"a", "e", "i", "o", "u"}

unique_vowels = set(sentence.lower()) & vowels

print("Unique vowels:", unique_vowels)
#print("Number of unique vowels:", len(unique_vowels))
