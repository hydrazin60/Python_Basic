str1 = "jiban pandey"
# str2 =  "web developer"
# # concatenation
# print(str1 + str2) 
# # length
# print(len(str1 + str2 + " "))
# # indexing of string in python
# print(str1[0])
# print(str2[9])
# # we acces the index of character in string but we can not change it

#             #slici
# # //  Accessing parts of a string
# # sentex => str[stating_index : ending_index]
# print(str2[0 : 14])
# print(str2[4 : ])
# print(str2[: 4])
# print(str2[ : ])
# # backward counter
# print(str2[ :-1])
# print(str2[1 :-9])
# print(len(str2[ 1 :-9]))

# # string Function 


 
# # 1 str.endswhite("er.")  #return true if string ends with "er."
# print(str1.endswith("pandey"))  
# # ans   => true
# print(str1.endswith("shr")) 
# # ans   => false


# # 2 str.capitalize()   #capitalise the first  character
# print(str1.capitalize())
# # ans => Jiban pandey  ## this function not change own orginal string 
# # if we awant to change the orginal string then we can use  
# str1 = str1.capitalize()
# print(str1)
# # ans => Jiban pandey /# always use this function to change the orginal string



# # 3 str.replace("old", "new")  # replace old with new  
# print(str1.replace("pandey", "shrivastava"))
# # ans => jiban shrivastava       ## this function not change own orginal string 
# # if we awant to change the orginal string then we can use  
# str1 = str1.replace("pandey", "shrivastava")
# print(str1)
# #  its change permanently pandey to shrivastava



# # 4 str.find("i")   # return 1st index of 1st occurrer
# print(str1.find("a"))
# # ans => 1
# # if i am search for not present character then it will return -1
# print(str1.find("x"))
# # ans => -1


# # 5 str.count("i)   # return number of occurrer
# print(str1.count("j"))
# # ans => 2


# # Q) print length of your name ?
# name = input("enter your name : ")
# print("length of your name is : ", len(name))

# # Q) print the number of $ in the string
# str = "Hi , $I am the $ symbol $99 $"
# print(str.count('$'))
