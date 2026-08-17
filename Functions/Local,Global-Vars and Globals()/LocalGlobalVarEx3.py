#Program for Demonstrating the Need of Local and Global Variables
#LocalGlobalVarEx3.py
def LearnAI():
    sub1="AI"
    print("\tTo Implement {} based Applications , We used {} Programming Lang.".format(sub1,lang))

lang="PYTHON" # Here lang is Called Global Variables

def LearnML():
    sub2="ML"
    print("\tTo Implement {} based Applications , We used {} Programming Lang.".format(sub2,lang))

#Main Program
LearnAI()  # Function Call
LearnML()  # Function Call