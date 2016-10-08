'''
Create a hello world program.
Manipute a string a little bit.
Notice that this is a comment, it doesn't effect the code.
I can comment here because of the three ' s
'''

s = "Hello World"

'''
This is a comment that tells us about the following function.
Good documentation is important
This function uses the string s, which we expect to be "Hello World"
to do stuff and things.
@param - None
@return - None
'''
def learnPython():
	#This is just a single line comment
	print("Running hello world program")
	x = 0
	if(x == 1):
		print("Something went wrong...")
	elif(x == 0):
		print(s)
	else:
		#NOTHING
	return

learnPython() #this tells the program to run learnPython function
