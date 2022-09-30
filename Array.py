

#An array is a special variable, which can hold more than one value at a time.

# numb = [1,4,7,8,4,7,8,8]
# names= ["Mojahid","Gazelle","Akbar","Mojahid","Nikhat","Shaklain"]
#
# names.append("Hussain")
#
# for name in names:
#     print(name)
#
# x =10
# name = "Mojahid"


#If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:

#However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?

#The solution is an array!

#An array can hold many values under a single name, and you can access the values by referring to an index number.

#The Length of an Array
#Use the len() method to return the length of an array (the number of elements in an array).

##Looping Array Elements
#You can use the for in loop to loop through all the elements of an array.

#Adding Array Elements
#You can use the append() method to add an element to an array.

#Removing Array Elements
#You can use the pop() method to remove an element from the array.cars.pop(1)
#You can also use the remove() method to remove an element from the array.cars.remove("Volvo")

#Array Methods
#append()-Adds an element at the end of the list-
# clear()-Removes all the elements from the list
# copy()Returns a copy of the list
# count()Returns the number of elements with the specified value
# extend()Add the elements of a list (or any iterable), to the end of the current list
# index()Returns the index of the first element with the specified value
# ,insert()Adds an element at the specified position
# ,pop()Removes the element at the specified position
# ,remove()Removes the first item with the specified value
# ,reverse()Reverses the order of the list
# ,sort()Sorts the list


cities = ["Banglore","Delhi","Ranchi","Hydrabad","Jamshedpur","Patna","Patna"]

num = [2,4,6,1,10,5,6]
num.sort()
#
# print(num)



#1. Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes

num = [19,67,65,66,87]

# print(num)
#
# print(num[0])
# print(num[1])
# print(num[2])
# print(num[3])
# print(num[4])












#2.Write a Python program to append a new item to the end of the array.

# bank = ["SBI","BOI","HDFC","RDBI","IDBI"]
#
# bank.append("CBI")
# print(bank)

#3.Write a Python program to reverse the order of the items in the array.

# item = ["Mojahid","Zahid","Shahid","Ghazala"]
#
# item.reverse()
# print(item)

#4.Write a Python program to get the length in bytes of one array item in the internal representation.

#5.Write a Python program to get the number of occurrences of a specified element in an arrayOriginal array: array('i', [1, 3, 5, 3, 7, 9, 3])
#Number of occurrences of the number 3 in the said array: 3 (append)

array = [1, 3, 5, 3, 7, 9, 3,3]

print(array.count(3))