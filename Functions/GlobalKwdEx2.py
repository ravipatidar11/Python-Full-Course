#Program for Demonstrating global keyword
#GlobalKwdEx2.py
def modify1():
	global a,b
	a=a+1
	b=b+1
def  modify2():
	global a,b
	a=a*2
	b=b*2
def  accessvals():
	#No Need to write global kwd bcoz we are Just acessing Global Variables
	c=a+10
	d=b+10
	print("\tLocal Var C Value:",c)
	print("\tLocal Var D Value:",d)


#Main Program
a,b=10,20  # Here 'a', 'b' are called Global Variables
print("Main Program: before modify1()  a:{} b:{}".format(a,b)) # a:10  b:20
modify1() # Function Call
print("Main Program: after modify1()  a:{} b:{}".format(a,b)) # a:11  b:21
modify2() # Function Call
print("Main Program: after modify2()  a:{} b:{}".format(a,b)) # a:22  b:42
accessvals() # Function Call
print("Main Program: after accessvals()  a:{} b:{}".format(a,b)) # a:22  b:42