import re
import openpyxl

'''
Let's mash up some CSV and Excel files
Mock Data from https://www.mockaroo.com/
'''

def mashXLSX():
	#id,first_name,last_name,BitcoinAddress,Credit_card_number,Money,Hex_Color,Catch_Phrase
	wbook = openpyxl.load_workbook('Mock_user_data.xlsx')

	sheets = wbook.get_sheet_names()#work books are broken into sheets
	print("Sheets:", sheets)

	#data = wbook.get_sheet_by_name('WHAT IS THIS?')

	# find all people who's name starts with J account balance

	#write this to a new file

	#do this instead of CMD+F and then copy pasting all the infomation
mashXLSX()

'''
Read the docs for OpenPyXL:
https://openpyxl.readthedocs.io/en/default/

How long would it take you to manually do this?
How long would it take to do it with built in Excel functions?
	- probably not too long, but this can easily changed for other purposes too!
'''
