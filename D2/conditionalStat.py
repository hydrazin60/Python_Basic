### CONDITIONAL STATEMENTS

### 1 if statement
### 2 if-else statement
### 3 if-elif-else statement
### 4 nested if statement
### 5 ternary operator

## if statement
## if(condition) : statement1
## else : statement2

#### Example:1
# age = int(input("Enter your age: "))  
# if 18 <= age < 60:
#     print("Eligible for driving license")
# elif age < 18:
#     print("Not eligible for driving license")
# elif age >= 60:
#     print("Senior citizen eligible for driving license")
# else:
#     print("Not eligible")
#### Example:2

# lightColor = "red"
# if(lightColor == "red"): print("stop")
# elif(lightColor == "yellow"): print("slow")
# if(lightColor == "red"): print("stop Now")
# elif(lightColor == "green"): print("go")
# else: print("invalid color")

#### Conditional operator
  
#### Example:3
# marks =  int(input("Enter your marks: "))
# if marks >= 90:
#     grade = "A"
# elif marks >= 80:
#     grade = "B"
# elif marks >= 70:
#     grade = "C"
# else:
#     grade = "D"
# print(f"The grade is {grade}")

#### Nesting if statements

#### Example:4
# age = int(input("Enter your age: "))
# if(age >= 18):
#     if(age >= 60):
#      print("senior citizen")
#     else:
#      print("can drive")
# else:
#     print("can't drive you are child!!")

#### Q1) check whether a number is even or odd
# number = int(input("Enter a number: "))
# if(number % 2 == 0) : print("Even")
# else : print("Odd")

#### Q2)  WAP to find the greatest of 3 numbers  entering by user
# A = int(input("Enter first number A: ")) 
# B = int(input("Enter second number B: "))
# C = int(input("Enter third number C: "))
# if A > B and A > C:
#     print("A is the greatest")
# elif B > A and B > C:
#     print("B is the greatest")
# else:
#     print("C is the greatest")

#### Q3) WAP to check if a number is a multiple of 7 or not

# A = int (input("Enter a number: "))
# if(A % 7 == 0):
#     print("multiple of 7")
# else:
#     print("not a multiple of 7")

#### Q4) WAP to check if a number is a multiple of 7 and 3 or not
# A = int (input("Enter a number: "))
# if(A % 7 == 0 and A % 3==0):
#     print("multiple of 7 and 3")
# elif(A % 7 == 0) : print("multiple of 7 only")
# elif(A % 3 == 0) : print("multiple of 3 only")
# else:
#     print("not a multiple of 7 and 3")