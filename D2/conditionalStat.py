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
  
## Example:3
marks =  int(input("Enter your marks: "))
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"

print(f"The grade is {grade}")
