#Program for Demonstrating the Need of Local and Global Variables
#LocalGlobalVarEx4.py
def   learnAI():
	sub1="AI"
	print("\tTo Implement '{}'  Based Application, we use '{}' Programming Lang".format(sub1,lang))
def   learnML():
	sub2="ML"
	print("\tTo Implement '{}'  Based Application, we use '{}' Programming Lang".format(sub2,lang))

#Main Program
#learnAI()  # We can't access the Global Var Value 'lang' bcoz It is Defined after the function call
lang="PYTHON"  # Here lang is Called Global Variables
learnML()  # Function Call