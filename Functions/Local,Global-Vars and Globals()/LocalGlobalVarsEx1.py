#Program for Demonstrating the Need of Local and Global Variables
#LocalGlobalVarEx1.py
def LearnAI():
    sub1="AI"
    print("\tTo Implement {} based Applications , We used {} Programming Lang.".format(sub1,lang))
def LearnML():
    sub2="ML"
    print("\tTo Implement {} based Applications , We used {} Programming Lang.".format(sub2,lang))

#Main Program
lang="PYTHON" # Here lang is Called Global Variables
LearnAI()  # Function Call
LearnML()  # Function Call