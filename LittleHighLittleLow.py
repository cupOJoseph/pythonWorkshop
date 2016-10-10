'''
LittleHighLittleLow
Take X numbers from the user
Use a for loop
Sort the list
Decide and print the largest and the smallest number
'''

times = input("Enter a number: ")
times = int(times)
numList = {}

for i in range(times):
	#what goes here? hint: INPUT from user
	print("Enter the", i, "th number, between 0 and 100")
	num = input("")
	num = int(num)
	numList[i] = num

print(numList)

minVal = 101
maxVal = -1

for j in numList:
	#what do we want to check here?
	if(numList[j] < minVal):
		minVal = numList[j] #numList[j] becomes each element in the list
	elif(numList[j] > maxVal):
		maxVal = numList[j]


#minVal and MaxVal have been set
#spit out what they are
print("Max is:",maxVal)
print("Min is:",minVal)
