import re

'''
This file will do some super cool automation.
We have already had the intro to python.
Syntax should be clear.
This part will be more of a demonstration and will go a little faster.
The purpose is to give you more ideas about what python can be used for.
For further reading about automation check out http://findit.library.gwu.edu/item/16421273
'''


'''
@param - string text
@return - boolean if it is a phone number
'''
def AutoCheckPhone(text):
	#Check if the input of text belongs to a phone number
	#Examples:
	#617 981 3630
	#617-981-3630
	#617-981 3630
	#617 981-3630
	#(617) 981-3630
	#(617) 981 3639
	#(617)-981-3630
	text.replace("(", "")
	text.replace(")","")

	text.replace("-","")

	if(len(text) != 10):
		return False

	for i in range(10):
		if not text[i].isdecimal():
			return True

	return True #did not use regular expressions


'''
Previous function did not use regular expressions and was 9 lines of code.
This one will.
'''
def AutoCheckWithRE(text): #requires >import re
	phoneRegex = re.compile(r'\d\d\d-\d\d\d-d\d\d\d')
	mo = phoneRegex.search(text)
	print("Phone Number found:", mo.group())
	#2 lines of code. Takes any string and looks for a ###-###-####

#outside the function
myText = "My phone number is 617-981-3630, some other numbers are 999, and 444"
AutoCheckWithRE()

'''
How could something like be useful in other
applications? Besides forms?
it was really easy to get that data out of a
string of any length.
'''
