
#Program for checking a number is even or not


# x = int(input("Enter Value"))
#
# if x%2 == 0:
#     print( str(x) +  " is" + "Even Number")
# else:
#     print(str(x) + " is"+ "Not Even Number")



#If  - Else

#Write a python to print if a person is having age greater than 18 and less than 60 than he is elgible for driving otherwise he is not eligible for driving

# 18-60 (driving) 0-18 and greater than 60 not eligible
#
# age = int(input("Enter the Age"))
#
# if (age >= 18 or age <=60):
#     print("He is eligible for driving")
# else:
#     print("He is not eligible for driving")
# tax = 0
# pr=int(input("Enter the price of bike"))
# if pr > 100000:
#      tax = 15/100*pr
# elif pr >50000 and pr <=100000:
#      tax = 10/100*pr
# else:
#      tax = 5/100*pr
# print("Tax to be paid ",tax)


# number = int(input("Enter The numner?"))
#
# if number%2 == 0:
#     print("It is an even Number")
# else:
#     print("It is an Odd Number")

#
#
# number = int(input("Enter the Number"))
#
# if number%3 ==0:
#     print("It is Divisible by 3")
# else:
#     print("It si not Divisible by 3")


list = [1,2,3,9]

temp = list[0]
list[0] = list[len(list)-1]
list[len(list)-1] = temp

print(list)






