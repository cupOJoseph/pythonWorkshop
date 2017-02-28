'''
LittleHighLittleLow
Take X numbers from the user
Use a for loop
Sort the list
Decide and print the largest and the smallest number
'''

#setup data structures
times = input("Enter a number: ")
times = int(times)
numList = {}

#get a list of numbers from the user
for i in range(times):
	#what goes here? hint: INPUT from user


print("Printing out numbers in list:")
print(numList)

minVal = 101
maxVal = -1


#decide what the smallest and largest numbers are
for j in numList:
	#what do we want to check here?
	if(        ):
		minVal = numList[j] #numList[j] becomes each element in the list
	elif(      ):
		maxVal = numList[j]


#minVal and MaxVal have been set
#spit out what they are
print("Max is:",maxVal)
print("Min is:",minVal)
