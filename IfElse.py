# Q-1 : Program checks if the number is positive or negative (9/10)

# num = input("Enter a Number")
#
# if int(num) > 0:
#     print("Positive Number")
# elif int(num) == 0:
#     print("Zero")
# else:
#     print("Negative Number")

# if ,else
# if > elif > elIf> else

# Q-2: Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye" (10/10).

# number = int(input("Enter a Number"))
#
# if number % 5 == 0:
#     print("Hello")
# else:
#     print("Bye")



# Q-3 :Write a program to display the last digit of a number.

# number = int(input("Enter the Number"))
#
# last_digit = number % 10
#
# print(last_digit)


# Q4. Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
# Cost price (in Rs)                                       Tax
# > 100000                                                  15 %
# > 50000 and <= 100000                          10%
# <= 50000                                                  5%

#
# price = int(input("Enter the Cost Price of Bike"))
#
# tax = 0
#
# if price > 100000:
#     tax = (15/100)*price
# elif price > 50000 and price <=100000:
#     tax = (10/100)*price
# else:
#     tax = (5/100)*price
#
# print("The Final Tax on the Cost Price = " + str(tax))


# Calculate Electric Bill
# First 100 unit charge =0 , 100-200 ( 5 * unit) ,
# 350 (100 - 100-200 , <200)
# 350-100 =
# 350  (100 =0  , 100 *5 =500 , 150*10 =1500  =2000

# 225
# 0-100 = 0 , 100-200 , 25*10
# 250 (0-100 =0 , 100-200 (*5) , 50 (*10)

# bill = int(input("Enter the Bill Unit"))
#
# charge = 0
#
# if bill <=100:
#     charge = 0
# elif bill > 100 and bill <= 200:
#     charge =(bill-100) * 5
# else:
#     charge = 500 + (bill-200) * 10
# print("The Bill Amount is " + str(charge))

#Print Grade  ( > 90 - A , >80 and <=90 -B , >=60 and <=80 -C <60 -D

marks = int(input("Enter Marks"))

if marks >90:
    print("Grade A")
elif marks > 80 and marks<= 90:
    print("Grade B")
elif marks >=60 and marks <=80:
    print("Grade C")
else:
    print("Grade D")


print(x)




