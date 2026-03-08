# def greet(name):
#     print("Hello:",name)

# greet("Mithun")

# def sum(a, b):
   
#     return a+b

# x = sum(10,20)
# print(x)


# text = "hello"
# i = len(text)-1
# rev = ""

# while i >= 0:
#     rev += text[i]
#     i -= 1



# print(rev)


# nums = [10, 20, 30, 40, 50]

# def second_largest(nums):
#     largest = float('-inf')
#     second = float('-inf')

#     for n in nums:
#         if n > largest:
#             second = largest
#             largest = n
#         elif n  > second and n != largest:
#             second = n

#     return second


# second_largest(nums)

# name = "Mithun"
# def reverse(name):
#     rev = ""
#     i = len(name)

# name = "Ram"
# print(type(name))

# age = 25
# print("your age is"+str(age))

# password = "123abkkjbuibb"
# print(len(password))

# if len(password) < 8 :
#     print("Yours is too short")

# text = """Python is very easy when you learn python in right way Python"""

# print(text.count("Python"))

# date = "2026/02/01"
# print(date.replace("/","-"))

# num = "+49 (176) 123-4567"
# print(num.replace("+","").replace(" ","").replace("(",""))

# name  = "Mithun"
# age  = 22
# height  = 5.6
# Genius  = True

# print(f"My name is {name}, I am {age} years old and {height}. I am {{Genius}} is {Genius}.")
# text = "Python"
# print(len(text))

# print(text[1])

# date = "2026-09-20"

# print(date[-2:])


# text = "   Engineering   "


# nr_of_Space = len(text)-len(text.strip())
# is_clean = len(text) == len(text.strip())
# print("number of white spaces is ",nr_of_Space)
# print("Is the data clean:", is_clean)


# text = "968-Maria, ( Data Engineer ) ;; 27y ".strip()

# # print(text.replace("968-","name:").replace(" ", " | ").replace(",(","role:").replace(",","").replace("(","role:"))

# print(text.replace("968-","name: ").replace("@","a").replace(" ( "," | role: ").replace(" ) ;;"," | age:").replace("y","").replace(",","").lower())

# url = "https://api.company.com/v1/data"

# url = "https://api.company.com/v1/data"

# print("/api" in url)

# phone2 = +895-4643134-15454313
# phone = +35435543435-544345456-5454
# print(phone1[phone1.find("-")+1:])

# print(phone1.find("-"))

# country = "India1"
# print(country.isalpha())
# phone1 = "32355643511515131"

# print(phone1.isnumeric())

# x = 5
# y = 5.5
# z = 2 + 3J

# # print(type(x))

# # #absolute value
# # print(abs(2-8))

# import math
# price  = 55.345345465
# print(math.floor(price))
# print(math.ceil(price))
# print(round(price))


# import random
# print(random.random())
# print(random.randint(1,5))

# x = 7.1
# print(type(x))

# y = 7
# print(type(y))
# import random
# number = random.randint(1,100)
# print(number)
# if number % 2 == 0:
#     print("Even number")
# else:
#     print("Odd")

# a = 10
# b = 3
# print(a // b)

# email = ""
# phone = 46464
# username = ""

# print(any([email, phone, username]))

# print(isinstance(123,int))

# print(3 > 1 and 5 > 1 )

# cpu_usage = 80
# memory_usage = 90

# print(not not not 3 > 2 )

# score = 100
# if score <= 50:
#     print("A")
# elif score >=50:
#     print("No")
# else:
#     print("B")

# email = "vefrever@gmail.com"
# email = email.strip()
# if email == "":
#     print("Email cannot be empty")

# if not("." and "@" in email):
#     print("Email must contain . and @")

# if email.count("@") != 1:
#     print("Email must contain only one @")

# if not email.endswith((".com", ".org", ".net")):
#     print("Email must end with .com, .org or .net")

# if len(email) > 254:
#     print("Email cannot be more than 254 characters")

# if not (email[0].isalnum() and email[-1].isalnum()):
#     print("Email must start and end with a letter or digit")

# else:
#     print("Email is valid")

# password = "ram12345678 "

# password = password.strip()

# if password == "":
#     print("Password cannot be empty")

# if len(password) <= 8:
#     print("Password must be atleast 8 characters")

# if password == email:
#     print("Email and Password cannot be same")

# if " " in password:
#     print("Password cannot contain whitespaces") 
# if not any(c.isupper() for c in password):
#     print("Password should contain one upper case letter")
# if not password[0].isalnum() and password[-1]:
#     print("Password must begin and end with a letter or digit")

# score = 100

# if score >= 90 :
#     print("A")
# else:
#     print("B")

# print("S" if score >= 90 else "C")

# country = "United State"

# if country == "India":
#     print("In")
# elif country == "United States":
#     print("US")
# elif country == "China":
#     print("Ch")
# else:
#     print("Unkknown Country")

# match country:
#     case "United States":
#         print("US")
#     case "India":
#         print("In")
#     case "China":
#         print("Ch")
#     case _:
#         print("Unkknown Country")


# for i in range(2,10,2):
#     print(f"hi: {i}")

# scores = [80,50,50,68,55,5521]
# total = 0

# for score in scores:
#     total += score
#     print("Current Score:",total)
# print("Final Score:", total)

# files = ['Report.csv '," Orders.csv", " Sales.txt "]

# for file in files:
#     file = file.strip().lower().replace('.txt', '.csv')
#     print(f"Processing {file}")
# x = 7
# answer = 0

# for i in range(1,10):
#     answer = x * i
#     print(f"{x} X {i} = {answer} ")

# for i in range(1,11):
#     print(f"7 x {i} = {7 * i}")
# numbers = [7,6,5,4,3,2,1]
# for number in numbers:
#     print(f"{"*" * number}")

# names = ["Kariya","Manja","Bladu","Koyya","kencha","","Seena"]
# for name in names:
#     if name == "":
#         print("Invalid name fouund in the list")
#         break
#     print(name)

# names = ["Kariya","Manja","Bladu","Koyya","kencha","","Seena"]
# for name in names:
#     if name == "":
#         # print("Invalid name found in the list")
#         continue
#     print(name)

# names = ["Kariya","Manja","Bladu","Koyya","kencha","","Seena"]
# for name in names:
#     if name == "":
#         # print("Invalid name found in the list")
#         pass
#         name = name.replace("","Unknown")
#     print(name)

# days  = ["Sun", "Mon","Tue","Wed","thu","Fri","Sat"]
# weekend_days = ["Sat", "Sun"]
# for day in days:
#     if day in weekend_days:
#         continue
#     print("Day is:",{day})

# emails = ["Select TABLE USERS;","Get TABLE USERS;","DROP TABLE USERS;","data@gmail.com","DROP TABLE USERS;","gowda@gmail.com","mithun@gmai.com","report@mail.com"]
# for mail in emails:
#     if ";" or "Drop" or "Get" or "Select" in mail:
#         print("SQL Injection: Hacker Attack",mail)
#         break
#     if not "gmail.com" in mail:
#         continue
#     print(mail)

# items = [1,2,3,4,5,6,7]

# for item in items:
#     if item % 2 == 0:
#         break
#     print(item)
# else:
#     print("Loop executed successfully")

# files = ["orders.csv","sales.csv","traffic.txt","reports.csv"]

# for file in files:
#     if  not file.endswith('.csv'):
#         print("Invalid file format:", file)
#         break
# else:
#     print("All files are valid")

# files = ['report.csv','data.xlsx','summary.docx','report.csv','data.csv']
# seen = []
# for file in files:
#     if len(file) != len(set(file)):
#         print("Duplicate File Found",file)
#         break
#     else:
#         print("No Duplicates Found")

# for file in files:
#     if file in seen:
#         print("Duplicate File Found",file)
#         break
#     seen.append(file)
# else:
#     print("All files are unique")

# for x in range(3):
#     for y in range(2):
#         print(f"{x},{y}")

# colors  = ['red','blue','green']
# sizes = ['S','M','L']
# for color in colors:
#     for size in sizes:
#         print(f"{color} : {size}" )

# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# answer = ""
# while answer != "yes":
#     answer = input("Do you agree!")
# print("Thank You")

# list[]
# tuple()
# set{}
# dict{}

# empty = []
# letters = ['a','b','c','d']
# print(empty)
# print(type(empty))

# empty = list()
# print(empty)

# person = ['Maria','Data Engineer',29,'india']
# # name,role, age,  country = person
# name,*details, country = person

# print(person)
# list = [True]
# first,*rest = list
# print(first)
# print(rest)
 
# numbers = [1,4,2,5,67,7]
# # print(max(numbers))
# numbers.append("x")
# print(numbers)

# numbers.insert(0,"g")
# print(numbers[0])
# print(numbers)

# matrix =  ['a','b','c','d']
# # matrix.remove('a')
# matrix.pop(0)

# print(matrix)

# numbers = [[1,4,2,5,67,7], [6,8,35,7,55] ]

# numbers.remove([1,4,2,5,67,7])
# print(numbers)

# pop to remove a specific position item from from a list
# .remove() to to remove an item

# numbers = [2,3,5,6,7,8,4,78,9,45,79]
# numbers.sort(reverse = True)
# print(numbers)
# new_list = sorted(numbers, reverse = True)
# print(new_list)

# name = ["Mithun","Gowda"]
# name.reverse()
# print(name)

# letters = ['a','b','c','d']
# numbers = [1,4,56,7,8,9]
# comb = letters + numbers
# # comb = [letters, numbers]
# # print(comb)


# # numbers.extend(letters)
# # print(numbers)
 
# comb = list(zip(letters, numbers))
# print(comb)

# ids = [101,102,103,1044,1055]

# employees = ['Alice','John',"Rock",'Peter','Michael']

# res = print(list(zip(ids,employees)))

# print(list(map(str.upper, letters)))
# letters = ['s','f','g','p']

# multiple = lambda x: x*2
# print(multiple(2))

# add = lambda x,y: x+y
# print(add(1,2))

# prices = ['$12.5','$34.56','$1.00']
# print(list(map(lambda p: float(p.replace("$","")), prices)))
# p = '$12.50'
# print(float(p.replace("$","")))

# prices = [120,235,46,30,45,60]
# print(list(filter(lambda p: p>=100, prices)))

# students = [
#     ["Maria",80],
#     ["Kumar",34],
#     ["flke",69]
# ]
# print(list(filter(lambda row: row[1] > 70, students)))
# print(students[0][1]>70)
# print(list(filter(lambda row: row[0].startswith("M"),students)))
# print(students[0][0].startswith("M"))

# employees = ['Alice','John',"Rock",'Peter','Michael']

# print(list(map(str.lower,employees)))

# domains = ['google.com','openai.com','localhost']

# cleaned = [
#     d.lower() #data tranformation
#     for d in domains #loop
#     if  not '.com' in d #filter
# ]
# print(cleaned)

# myList = [10,20,30,10]
# print(myList)

# myList[0] = 50
# print(myList)

# Lists are ordered, allows duplicates, indexed, mutable

# my_list = (50,20,30)
# # my_list[0] = 50
# print(my_list)
# # Tuples are ordered, allows duplicates, indexed, immmutable
# print(sorted(my_list))

# ids = [10,12,23,45,6,10,22,12,23,45]
# unique_ids = []
# for id in ids:
#     if id not in unique_ids:
#         unique_ids.append(id)


# print(unique_ids)

# my_list = {10,20,40,30}
# my_list.remove(10)
# print(my_list)

#lists are unordered, not indexed, no duplicates,mutable


# a = my_list
# a.add(100)
# print(a)

# my_list.update({1,2})
# print(my_list)

# a = {1,2,3,.45,57,78,5,6,90}
# b = {45,57,78,89,90,23,34,90}
# c = {"a","b","c"}

# print(a.union(b))
# print(a | b,"\n")

# print(a.intersection(b))
# print(a & b,"\n")

# print(a.symmetric_difference(b))
# print(a ^ b,"\n")

# print(a.difference(b))
# print(b - a,"\n")

# print(a.issubset(b))
# print(a.issuperset(b))
# print(a.isdisjoint(b))

#dictionaries - key value pairs

# my_dict = {
#     'a' : 10,
#     'b' : 20,
#     'c' : 30,
# }
# print(my_dict)

#dict are ordered
#keys are unique but values can be duplicates
#not indexed but keyed
#values are mutable

# user = {
#     "id" : 1,
#     "name" : "Mithun",
#     "place" : "Earth",
#     "score" : 10,
# }

# user_str = {
#     k : v.upper()
#     for k, v in user.items()
#     if isinstance(v, str)  
# }
# print(user_str)

# dictionary : collection of multiple & related information

