###### Loops in Python ########
### while loop
### for loop

## while loop
# count = 0
# while count < 5:
#  print("hello", count)
#  count = count + 1

## Q1) Print numbers from 1 to 100
# count =1 
# while count<=100:
#     print(count)
#     count = count + 1

## Q2) Print the multiples table of 'n' 
# n = int(input("Enter the number : "))
# count = 1
# while count <= 10:
#     print(n ,"*", count ,"=",n*count)
#     count = count + 1 

## Q3) Print the numbers from 1 to 100 which are divisible by 'n'
# n = int(input("Enter the number : "))
# count = 1
# while count <= 100:
#    count = count + 1
#    if(count % n == 0):
#        print(count)
## Q4) Print the elements of the following list using a loop:
##[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# n = 1
# while n <= 10:
#     print(n*n)
#     n = n + 1

##Q5) Search for a number x in this tuple using loop: [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# num = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# n = int(input("Enter the number : "))
# i = 0
# while i <len(num):
#     if( num[i] == n):
#         print( n , "Found at index",i)
#     i = i + 1
# else:
#     print("Not Found")

#########  Break & continue  ############ in loops
##### Break
# num = [1, 4, 9, 16, 25, 36, 49,  16 ,64, 4 , 9 ,  1]
# x = 16
# i = 0
# while i <len(num):
#     if( num[i] == x):
#         print( x , "Found at index",i)
#         break
#     i = i + 1
# else:
#     print("Not Found")

##### Continue
### Example 1
# num = [1, 4, 9, 16, 25, 36, 49, 16, 64, 4, 9, 1]
# i = 0
# n = 1

# while i < len(num):
#     if i == n:
#         i += 1
#         continue
#     print(num[i])
#     i += 1
# else:
#     print("Not Found")
### Example 2
# i = 0
# while i <= 5:
#     if(i == 3):
#         i = i + 1
#         continue
#     print(i)
#     i = i + 1


############### For loops ########
# # for el in list  
#work
# lest = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# for i in lest:
#     print(i)

### for(let i =0 ; i < val.length; i++){
###    console.log(val[i]);          @JS
### }


#### for loop with else
## for el in list :
## some WOrk
## else :
## some work