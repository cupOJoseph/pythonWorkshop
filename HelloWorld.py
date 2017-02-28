'''
Create a hello world program.
Manipute a string a little bit.
Notice that this is a comment, it doesn't effect the code.
I can comment here because of the three ' s
This is a comment.
'''

s = "Hello World"
num = -1
empty_s = ""

'''
This is a comment that tells us about the following function.
Good documentation is important
This function uses the string s, which we expect to be "Hello World"
to do stuff and things.
@param - None
@return - None
'''
def learnPython():
	# This is just a single line comment
	print("Running hello world program. num = ", num)#anything after a # is a comment
	x = 0

	if(x == 1):
		print("Something went wrong...")
		print('value of x:', x)
	elif(x == 0):#else if()
		print(s)
	else:
		#NOTHING
		return

def CrazyStrings():
	print(s[::2])
	print(s[0:5])


# Now I'm outside the defined functions. Execute the next instruction.
#CrazyStrings()
learnPython() #this tells the program to run learnPython function
'''
run on UNix with $python HelloWorld.py
run on windows with $C:\Python34>Python HelloWorld.py
'''
