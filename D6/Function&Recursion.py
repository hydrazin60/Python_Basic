######### Function in Python ############
### A function is a block of statements that perform a specific task

#### function sentex
## def function_Name(param1 , param2 , ...) :
##     some work
##     return value

#####function call
## function_Name(param1 , param2 , ...)

##EX1
# def sumFunction(a, b): ## a,b are parameters
#     sum = a + b
#     print(sum)
#     return sum

# sumFunction(5, 6) ## 5,6 are  arguments

##EX2
# def Prin_Hello():
#     print("Hello")

# Prin_Hello()
# Prin_Hello()    

##EX3

# def calculate_AVG(a,b):
#     sum = a+b
#     AVG = sum/2
#     return AVG

# print(calculate_AVG(5,6))

######## function in python
## in phthon have 2 types of function 
## i) Built-in Function :- print() , len() , type() , range() ....
## ii) User-defined Function

## EX3
# def cal_Product (a,b=1): ## we can define default value and default value is placed at the end not start
#     product = a*b
#     return product

# print(cal_Product(5,6))

################### LET's Practice ################
##Q1) WAF to print the length of a list.(list is the parameter)

cities = ["kathmandu", "lalitpur", "bhaktapur", "pokhara", "chitwane"]
heros = ["ironMan", "hulk", "thor", "spiderman", "captainAmerica"]

# def print_len(list):
#     print(len(list))
 
# print_len(cities)
# print_len(heros)

# Q2) waf to print the elements of a list in a single line.(list is the parameter)
# def print_List(list):
#  for item in list:
#      print(item, end=" ")

# print_List(cities)