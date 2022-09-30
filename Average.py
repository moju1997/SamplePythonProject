n = int(input("Enter number"))
# a = [1,2,3,4,5,6,7,8,9,10]
sum = 0
# loop from 1 to n
for num in range(1, n + 1, 2):
    sum = sum + num
print("Sum of first ", n, "numbers is: ", sum)
average = sum / n
print("Average of ", n, "numbers is: ", average)


