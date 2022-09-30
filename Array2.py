

#Find the minimum (or maximum) element of an array

# array = [786,623,534,722,298,765,8644,685,355,9866,5777]

#Find Minimum of the Array


array = [786,623,534,722,298,765,8644,685,355,9866,5777]

#Q-2 Remove duplicates from sorted array

#Input: nums = [1,1,2]
#Output: 2, nums = [1,2]

# Count Number of even and Odd Elements

aarray1 = [18,22,25,11,3,17,18,28,77,67,78,11,9,77,12,88]

#
# evenCount = 0
# oddCount = 0
#
# for i in range(0, len(aarray)):
#     if aarray[i] % 2 == 0:
#         evenCount = evenCount + 1
#     else:
#         oddCount = oddCount +1
#
# print("Even Count = " + str(evenCount)  +  "  and odd Count = " + str(oddCount))


# Print the even element array and Odd element array

aarray = [18,22,25,11,3,17,18,28,77,67,78,11,9,77,12,88]

evenNumbers = []
oddNumbers = []


for i in range(0, len(aarray)):
    if aarray[i] % 2 == 0:
        evenNumbers.append(aarray[i])
    else:
        oddNumbers.append(aarray[i])

print("The Even Numbers are = " + str(evenNumbers) + "and Odd Numbers are = " +  str(oddNumbers))
