#Program for Demonstrating the Functionality of Closure
#ClosureEx1.py
def   fun1(a): # Outer Function
	print("Outer Function:",a)
	def fun2():  # Closure
		print("\tInner Function:",a)
	return fun2


#Main Program
fn2=fun1(10) # Outer Function Call
fn2()  # Inner Function Call
fn2()  # Inner Function Call
fn2()  # Inner Function Call
