#  CONDITIONAL STATEMENTS

# 1 if statement
# 2 if-else statement
# 3 if-elif-else statement
# 4 nested if statement
# 5 ternary operator

## if statement
# if(condition) : statement1
# else : statement2

age = int(input("Enter your age: "))  
if 18 <= age < 60:
    print("Eligible for driving license")
elif age < 18:
    print("Not eligible for driving license")
elif age >= 60:
    print("Senior citizen eligible for driving license")
else:
    print("Not eligible")

