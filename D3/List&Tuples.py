#### Lists in Python
## string => inmutable in python(unchangeable)  [in string we can read and access the index(value) BUT we can not change the value]
## list => mutable in python (changeable) [in list we can read and access the index(value) AND we can change the value]
marks1 = 95.3
marks2 = 85.6
marks3 = 75.9
marks4 = 65.4
marks5 = 55.9
marks6 = 45.2

marks = [95.3, 85.6, 75.9, 65.4, 55.9, 45.2]
studentNams = ["jiban", "pandey", "khem", "karuna", "nisan", "samir"]
# print(studentNams[0], ":",  marks[2])
# # we can change the value i List
# marks[0] = 100
# studentNams[1] = "Pralhad giri"
# print(studentNams[1] , marks[0]) 
# ## slicing of list @@  List_name[starting index : ending index]  @@ List_name[starting index : ending index : step size]
# print(marks[0:3]) ## from 0 to 2
# print(marks[:4]) ## from 0 to 5  @@start:stop
 
# ##### List Methods
# #list.append(4)  # add 4 at the end  [we can  pass one element at a time and this function add this element at the end of the list]
# marks.append(80)
# print(marks) ## print =>  [95.3, 85.6, 75.9, 65.4, 55.9, 45.2, 80]

#  # list.sort()  # sort the list [ two type of sort function 1. is asscending order 2. is descending order ]
# marks.sort() ## this function change in orginal list
# print(marks) ## print => [45.2, 55.9, 65.4, 75.9, 85.6, 95.3] [ it will sort the list in increse order]
#  #list.sort(reverse = True)  # sort the list in reverse order
# marks.sort(reverse=True) ## this function change in orginal list
# print(marks) ## print => [95.3, 85.6, 75.9, 65.4, 55.9, 45.2]

# # list.remove() 
# marks.reverse() ## this function change in orginal list
# print(marks)
# ## list.remove(4)  # remove the 4 from the list
# marks.remove(55.9)
# print(marks)
# ## list.pop(3)  ##  remove the 3 index from the list
# marks.pop(2)     ## this function change in orginal list
# print(marks)