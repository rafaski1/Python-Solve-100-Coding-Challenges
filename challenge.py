# # STRINGS LEV 1
# # 2
# a=["","H","Hello","Amazing"]
#
# for x in a:
#     print(len(x))
#
# # 4
# a=["Hello", "Pizza", "", "World"]
# i=[2,4,3,15]
#
# for x,y in zip(a,i):
#     if len(x) == 0:
#         print("Empty String")
#     elif len(x) < y:
#         print("i is out of range")
#     else:
#         print(x[y])
#
# # 6
# list=["Hello", "Wo", ""]
# for x in list:
#     print(x[::-1])
#
# # 8
# list=["Blue", "Wonderful", "Amazing"]
# for x in list:
#     if len(x) <6:
#         print("")
#     else:
#         output1=x[0:3]
#         output2=x[-3:]
#         print(output1+output2)
#
# # 11
# list=["Coding", "Pizza", "Python", "A", ""]
# for x in list:
#     if len(x) <= 1:
#         print(x)
#     else:
#         output=x[1::2]
#         print(output)
#
# # 11v2
# s="Coding"
# new_s=""
# for i in range(len(s)):
#     if i % 2 !=0:
#         new_s+= s[i]
#
# # 13
# list=["Hello", "4567", "Hello59", ""]
# for x in list:
#     print(x.isdecimal())
#
# # 15
# s="Hello"
# n=1
#
# if len(s) == 0 or n >= len(s):
#     print(s)
# else:
#     new_s=""
#     for i in range(len(s)):
#         if i != n:
#             new_s += s[i]
#     print(new_s)
#
# list=["Hello", "World", "Dog", ""]
# n=[1,3,15,2]
# for x,y in zip(list, n):
#     if y >= len(x) or len(x) ==0:
#         print(x)
#     else:
#         new_x = ""
#         for z in range(len(x)):
#             if z !=y:
#                 new_x += x[z]
#         print(new_x)
#
# # 17
# s = "Hello"
# print(s.replace("l","s"))
#
# s = "Hello"
# new_s = ""
#
# curr_char="l"
# new_char="s"
#
# for char in s:
#     if char == curr_char:
#         new_s += new_char
#     else:
#         new_s += char
#
# print(new_s)
#
# # STRINGS LEV 2
# #
# # 1
# s = "Hello, World!"
# print(s.replace(",","."))
#
# new_s = ""
#
# curr_char = ","
# new_char = "."
#
# for char in s:
#     if char == curr_char:
#         new_s += new_char
#     else:
#         new_s += char
# print(new_s)
#
# # 3
# import string
#
# s = "Hello"
# set_s = set(s.lower())
# print(set_s)
# if " " in set_s:
#     set_s.remove(" ")
# print((set_s) == set(string.ascii_lowercase))
#
# # 5
# s = "hekkkk oooo"
# print(s.replace(" ",""))
#
# s = "Helo o o o o, world"
# new_s = ""
# for char in s:
#     if char != " ":
#         new_s += char
# print(new_s)
#
# # 7
# s = "Hello"
# prefix = "He"
#
# print(s[:len(prefix)]==prefix)
# print(s.startswith(prefix))
#
# # 9
# s = "Hello"
# suffix = "li"
#
# print(s[-len(suffix):] == suffix)
# print(s.endswith(suffix))
#
# # 12
# s = "Hello World"
# new_s = ""
#
# list = s.split(" ")
#
# for word in list:
#     reversed_word = word[::-1]
#     swapped_case = reversed_word.swapcase()
#     new_s +=swapped_case + " "
#
# new_s = new_s.rstrip()
# print(new_s)
#
# # 14
# s = "Corporation"
#
# repeated_count = 0
# repeated_chars = []
#
# for char in s:
#     if s.count(char) > 1 and char not in repeated_chars:
#         repeated_count +=1
#         repeated_chars.append(char)
#
# print(repeated_count)
#
# if len(repeated_chars) > 0:
#     for char in sorted(repeated_chars):
#         print(char, end=" ")
# else:
#     print(None)
#
# # 16
# s = "Hello World"
# new_s = ""
#
# words_list = s.split(" ")
#
# for word in words_list:
#     l_word = word.lower()
#     sorted_word = "".join(sorted(l_word))
#     new_s += sorted_word + " "
#
# new_s.rstrip()
# print(new_s)
#
# # LISTS LEVEL 1
#
# # 2
# list=[3,4,5,6]
# factor=2
# new_list=[]
#
# for number in list:
#     output = number*factor
#     new_list += [output]
#
# print(new_list)
#
# list2=["a","b","c"]
# factor2=3
#
# for i, elem in enumerate(list2):
#     list2[i] = elem * factor2
#
# print(list2)
#
# # 4
# List = [3,4,5,6]
#
# for i in List:
#     print(i, end=" ")
# print("\n")
#
# print(*List, sep=" ")
#
# # 6
# my_list = []
#
# # if len(my_list) == 0:
# #     print(None)
# # else:
# #     print(max(my_list),min(my_list),sep=" ")
#
# if my_list:
#     print(max(my_list), min(my_list))
# else:
#     print(None)
#
# # 8
# my_list = [2]
#
# if my_list:
#     print("Not Empty")
# else:
#     print("Empty")
#
# # 11
# my_list = ["a","b","c"]
#
# if my_list:
#     for i,num in enumerate(my_list):
#         print(num, i)
# else:
#     print("Empty List")
#
# for i in range(len(my_list)):
#     print(i,my_list[i])
#
# # 13
# my_list = [1,2,3,4]
# el = 3
#
# if not my_list:
#     print("Empty List")
# elif my_list.count(el) == 0:
#     print("Not Found")
# else:
#     for i in range(my_list.count(el)):
#         my_list.remove(el)
# print(my_list)
#
# # 15
# # my_list = [1, 1, 2, 3, 4, 4]
# # no_duplicates = list(set(my_list))
# # print(no_duplicates)
#
# # 17
# my_list = [1,-1,0,2,2,3]
# count = 0
# for i in my_list:
#     if i > 3:
#         count += 1
# print(count)
#
# count2 = sum(1 for elem in my_list if elem > 3)
# print(count2)
#
# # LISTS LEVEL 2
# #
# # 1
# lista=[1,2,3,4]
# listb=[1,2,3]
#
# difference=[]
#
# for elem in lista:
#     if elem not in listb:
#         difference.append(elem)
#
# print(difference)
#
# # 3
# pointA=[3,4,5]
# pointB=[1,3,5]
#
# distance = ((pointB[0]-pointA[0])**2 + (pointB[1]-pointA[1])**2 + (pointB[2]-pointA[2])**2)**(1/2)
#
# print(round(distance,2))
#
# # 5
# pointA=[1,2,3,4]
# pointB=[1,2]
#
# common=[]
#
# for elem in pointA:
#     if elem in pointB:
#         common.append(elem)
# print(common)
#
# # 7
# lista=[1,2,3,4]
#
# if len(lista) >1:
#     sorted_list = sorted(lista)
#     print(sorted_list[-2])
# else:
#     print(None)
#
# # 10
# my_list = [1,3]
#
# if len(my_list) <= 1:
#     print(None)
# else:
#     sorted_list = sorted(my_list)
# print(sorted_list[1])
#
# # 12
# my_list = ["a","a","b","c","a","b"]
# freq_dict= {}
#
# for elem in my_list:
#     if elem not in freq_dict:
#         freq_dict[elem] = 1
#     else:
#         freq_dict[elem] += 1
#
# print(freq_dict)
#
# # 14
# my_list = [4, 5, [1,2,3],[4,5,6],[7,8,9]]
# flat_list = []
#
# for elem in my_list:
#     if isinstance(elem, list):
#         for nested_elem in elem:
#             flat_list.append(nested_elem)
#     else:
#         flat_list.append(elem)
#
# print(flat_list)
# print(*flat_list)
#
# # 16
# import itertools
#
# my_list=[1,2,3]
#
# new_list = list(itertools.permutations(my_list))
#
# print(new_list)
#
# for i in new_list:
#     print(i)
#
# # DICTIONARIES LEVEL 1
#
# # 2
# my_dict = {"a":4,"b":6}
# key = "a"
#
# print(key in my_dict)
#
# # 4
# init_dict = {"January": 45, "February": 56, "March": 67}
# new_key = "April"
# new_value = 47
#
# if new_key not in init_dict:
#     init_dict[new_key] = new_value
#
# print(init_dict)
#
# # 6
# my_dict1 = {"a":1,"b":2, "c":3}
# my_dict = my_dict1 | my_dict2
#
# # 9
# dit = {"a":4, "b":4, "c":5}
#
# a_set = len(set(dit.values()))
#
# if a_set == 0:
#     print("Empty")
# elif a_set == 1:
#     print(True)
# else:
#     print(False)
#
# # 11
# dict = {"a":4, "b":3, "c":7}
#
# if dict:
#     max_value = max(set(dict.values()))
#     print(max_value)
# else:
#     print(None)
#
# # 13
# dict = {"a":4, "b":3, "c":7}
#
# if dict:
#     min_value = min(set(dict.values()))
#     print(min_value)
# else:
#     print(None)
#
# # DICTIONARIES LEVEL 2
# #
# # 1
# dict = {"a":4, "b":4, "c":2, "d":7, "e":4, "f":2,"g":7,"h":7}
# freq_dict={}
#
# for value in dict.values():
#     if value in freq_dict:
#         freq_dict[value] +=1
#     else:
#         freq_dict[value] = 1
#
# print(freq_dict)

# #3
# my_list = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]
#
# new_dict = {}
#
# for i in my_list:
#     key = i[0]
#     value = i[1]
#     new_dict[key] = value
#
# print(new_dict)

# #5
# my_dict = {
# 	"a": [1, 2, 3],
# 	"b": [4, 0, -4],
# 	"c": [3, 5, 9],
# 	"d": [45, 12, 100]
# }
#
# max_sum = None
#
# for i in my_dict.values():
#     summ = sum(i)
#     print(summ)
#
#     if max_sum is None:
#         max_sum = summ
#     elif max_sum < summ:
#         max_sum = summ
#
# print(max_sum)

# #8
# s = "Hello, World"
# s = s.lower()
#
# mydict = {}
#
# for i in s:
#     if i.isalpha():
#         if i in mydict:
#             mydict[i] +=1
#         else:
#             mydict[i] = 1
# print(mydict)

# #10
# my_dict = {
# 	"a": [4, 3, 2],
# 	"b": [5, 3, 7],
# 	"c": [1, 9, 10],
# 	"d": [3, 4, 1]
# }
#
# for i in my_dict.values():
#     i.sort()
#
# print(my_dict)

# #12
# product_info = {
# 	"description": "shoe",
# 	"price": 4.56,
# 	"colors": ["green", "blue", "red"],
# }
#
# alist = []
#
# for key, value in product_info.items():
#     alist.append([key, value])
#
# print(alist)

# # CONDITIONALS LEVEL 1
#
# # 2
# i = -22
#
# if i > 0:
#     print("Positive")
# elif i == 0:
#     print("Zero")
# else:
#     print("Negative")

# #4
# s = "Score: 36"
#
# if len(s) == 0:
#     print("Empty String")
# else:
#     for i in s.lower():
#         if i.isalpha():
#             if i in ("a", "e", "i", "o", "u"):
#                 print(f"{i} is a vowel")
#             else:
#                 print(f"{i} is a consonant")
#         else:
#             print(f"{i} is not a letter")

# #6
# a = 5
# b = 3
# c = 4
#
# if (a>=b) and (a>=c):
#     print(a)
# elif (b>=a) and (b>=c):
#     print(b)
# else:
#     print(c)

# #9
# a=1
# b=2
# c=3
#
# print(min(a,b,c))
#
# if (a<=b) and (a<=c):
#     print(a)
# elif (b<a) and (b<c):
#     print(b)
# else:
#     print(c)
#
# #11
# s1 = "Spring"
# s2 = "Summer"
# s3 = "Autumn"
# s4 = "Winter"

# #13
# a = 3
# b = 3
# c = 2
#
# if (a == b) and (b == c):
#     print("Equal")
# else:
#     print("Not equal")
#
# if a == b == c:
#     print("Equal")
# else:
#     print("Not equal")
#
# #CONDITIONALS LEVEL 2

# #1
# month = "February"
#
# months_31 = ("January", "March", "May")
# months_30 = ("April", "June")
#
# if month in months_31:
#     print(f"{month} has 31 days.")
# elif month in months_30:
#     print(f"{month} has 30 days.")
# else:
#     print(f"{month} has 28 days.")

# #3
# a=2
# b=2
# c=3
#
# if a<b<c:
#     print("Increasing Order")
# elif a>b>c:
#     print("Decreasing Order")
# else:
#     print(None)

# #5
# a=2
# b=5
# c=-3
#
# delta = b**2 - 4*a*c
#
# if delta < 0:
#     print("complex roots")
# elif delta == 0:
#     r = (-b)/(2*a)
#     print(r)
# else:
#     r1 = (-b - delta**(1/2))/(2*a)
#     r2 = (-b + delta ** (1 / 2)) / (2 * a)
#     print(r1, r2)

# #8
# year = 1836
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# #10
# ADDITION = 1
# SUBTRACTION = 2
# MULTIPLICATION = 3
# DIVISION = 4
# INTEGER_DIVISION = 5
# MODULO = 6
#
# print("=== Welcome to your Interactive Python Calculator ===")
#
# a = int(input("Please enter the first value: "))
# b = int(input("Please enter the second value: "))
#
# print("Great! Now enter the operation.")
# print("These are the available options:")
# print("1 - Addition")
# print("2 - Subtraction")
# print("3 - Multiplication")
# print("4 - Division")
# print("5 - Integer Division")
# print("6 - Modulo")
#
# operation = int(input("--> Enter the corresponding integer: "))
#
# if operation == 1:
#     print(f"{a} + {b} is {a+b}")
# elif operation == 2:
#     print(f"{a} - {b} is {a-b}")
# elif operation == 3:
#     print(f"{a} * {b} is {a*b}")
# elif operation == 4:
#     if b == 0:
#         print("denominator cannot be 0")
#     else:
#         print(f"{a} / {b} is {a / b}")

# # FOR LOOPS LEVEL 1
#
# #2
#
# for i in range(1,16):
#     print(i)

# #4
# n = 6
#
# for i in range(n,0,-1):
#     print(i)

# #6
# total = 0
#
# for i in range(1,101):
#     total += i
#
# print(total)
#
# #8
# n = int(input("Enter the value of n: "))
# for i in range(1,11):
#     r = n*i
#     print(f"{n} x {i} = {r}")

# #11
# for i in range(65,91):
#     print(chr(i))

# #13
# for i in range(2,201,2):
#     print(i)
#
# for i in range(2,201):
#     if i % 2 == 0:
#         print(i)

# #15
# # s = int(input("Enter value: "))
#
# s=3
# fact = 1
#
# for i in range(2, s+1):
#     fact *= i
#
# print(fact)

# #LOOPS LEVEL 2

#1
# num = 4
# is_prime = True
#
# if num == 1:
#      is_prime = False
# else:
#     for i in range(2,num):
#         if num % i == 0:
#             is_prime = False
#             break
#
# if is_prime:
#     print("Prime")
# else:
#     print("Not Prime")

# #3
# n = 9
#
# for i in range(1,n+1):
#     print("*"*i)

# #5
# s = 3456
#
# reverse = str(s)[::-1]
# print(reverse)

# #7
# s = "Hello"
#
# for i in s[::-1]:
#     print(i, end="")

# #10
# n = int(input("Enter the number of rows: "))
#
# k = (2 * n) - 2
#
# for i in range(n):
#
#     for j in range(k):
#         print("", end=" ")
#
#     for j in range(i + 1):
#         print("*", end=" ")
#
#     print("")
#
#     k = k - 2

# #12
# n = 5
# count = 1
#
# for i in range

# #WORKING WITH FILES LEVEL 1
#
# #2
# alist = []
# with open("basic_file.txt", "r") as file:
#     for line in file:
#         alist.append(line)
#
# print(alist)
#
# #4
# n = 2
# with open("basic_file.txt", "r") as file:
#     lines = file.readlines()
#     num_lines = len(lines)
#     print(num_lines)
#
#     if num_lines < n:
#         print(f"Please enter a value for n. The file has {num_lines} lines")
#     else:
#         for i in range(n):
#             print(lines[i].strip("\n"))

# #6
# n = 2
# with open("basic_file.txt", "r") as file:
#     lines = file.readlines()
#     num_lines = len(lines)
#     print(num_lines)
#
#     if num_lines < 4:
#         print(f"Please enter a value for n. The file has {num_lines} lines")
#     else:
#         for i in range(-n,0):
#             print(lines[i].strip("\n"))

# #8
# longest=""
# with open("basic_file.txt", "r") as file:
#     for i in file:
#         if len(i) > len(longest):
#             longest = i
#
# print(longest)

# #10
# freq_dict = {}
#
# with open("basic_file.txt", "r") as file:
#     for word in file:
#         word = word.strip("\n")
#         if word not in freq_dict:
#             freq_dict[word] = 1
#         else:
#             freq_dict[word] +=1
# print(freq_dict)

# # WORKING WITH FILES LEVEL 2
#
# # 1
# lista = [1, 2, 3, 4, 5]
# with open("basic_file.txt", "w") as file:
#     for elem in lista:
#         file.write(str(elem)+"\n")

# #3
# char = 0
#
# with open("basic_file.txt", "r") as file:
#     for line in file:
#         char += len(line.replace(" ","").strip("\n"))
# print(char)

# #6
# file_path = "basic_file.txt"
# file_path_copy = "basic_file_copy.txt"
#
# with open(file_path, "r") as file, \
#         open(file_path_copy, "w") as copy:
#     for line in file:
#         copy.write(line)

# #8
# import os.path
#
# file = "basic_file.txt"
#
# if os.path.isfile(file):
#     print(f"The file {file} exists")
# else:
#     print(f"The file {file} doesn't exist")
#
# # Miscellaneous and More Challenging Programs (Level 1)
#
# #2
# import datetime
#
# current_time = datetime.datetime.now()
# formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
# print("Current Date and Time:")
# print(formatted_time)

# #4
# seconds = 5400
# minutes = seconds// 60
# hours = round(seconds / 3600, 1)
# print(f"{seconds} is equivalent to:")
# print(f"{minutes} minutes")
# print(f"{hours} minutes")
#
# #6
# import math
#
# d = int(input("Enter diameter: "))
# r = d/2
# area = round(math.pi*(r**2),2)
#
# print(f"The area of a circle with diameter {d} is {area}")
#
# #9
# base = int(input("Enter base: "))
# height = int(input("Enter height: "))
# area = round((base*height)/2, 2)
#
# if base > 0 and height > 0:
#     print(f"The area of a triangle with base of {base} and height of {height} is {area}")
# else:
#     print("Please enter valid values for base and height")

# #11
# degrees_celsius= int(input("Enter Celcius degrees: "))
#
# degrees_fahrenheit = int((degrees_celsius * 9/5) + 32)
#
# print(f"{degrees_celsius} Celsius = {degrees_fahrenheit} Fahrenheit")

# #13
# degrees_fahrenheit= int(input("Enter Fahrenheit degrees: "))
#
# degrees_celsius = int((degrees_fahrenheit - 32) * 5/9)
#
# print(f"{degrees_fahrenheit} Fahrenheit = {degrees_celsius} Celsius")
#
# # Miscellaneous and More Challenging Programs (Level 2)
#
# #1
# height = int(input("Please enter your height in cm: "))
# weight = int(input("Please enter your weight in kg: "))
#
# bmi = round(weight/((height/100)**2), 1)
#
# if bmi < 18.5:
#     print(f"your BMI is {bmi}. Underweight")
# elif 18.5 <= bmi <= 24.9:
#     print(f"your BMI is {bmi}. Normal")
# elif 24.9 < bmi <= 29.9:
#     print(f"your BMI is {bmi}. Overweight")
# else:
#     print(f"your BMI is {bmi}. Obesity")
#
# #3
# import calendar
#
# print("Welcome to your Python Calendar!")
# month = int(input("Please enter a month as value 1-12: "))
# year = int(input("Please enter a year: "))
#
# print(calendar.month(year,month))
#
# #6
# import datetime
#
# date1 = input("Enter the first date (YYYY MM DD): ")
# date2 = input("Enter the second date (YYYY MM DD): ")
#
# date1_list = date1.split(" ")
# year1 = int(date1_list[0])
# month1 = int(date1_list[1])
# day1 = int(date1_list[2])
#
# date1_object = datetime.date(year1,month1,day1)
#
# date2_list = date2.split(" ")
# year2 = int(date2_list[0])
# month2 = int(date2_list[1])
# day2 = int(date2_list[2])
#
# date2_object = datetime.date(year2,month2,day2)
#
# if date2_object < date1_object:
#     print("Enter valid dates.")
# else:
#     difference = (date2_object - date1_object).days
#
# print(f"There are {difference} days between these days.")

#8
import re
regex = "^My[\w\s]+blue$"

s = "My favourite shirt is blue"

if re.search(regex, s):
    print("Match")
else:
    print("No Match")