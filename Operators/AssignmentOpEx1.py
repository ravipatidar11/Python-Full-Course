# program for Assignment operations
# AssignmentOpEx1.py

A,B=float(input('Enter first number: ')),float(input('Enter second number: '))
ap,sp,mp,dp,fdp,mdp,ep=A+B,A-B,A*B,A/B,A//B,A%B,A**B
print('-'*50)
print('Arithmetic Operations')
print('-'*50)
print("The add of {} and {} is: {}".format(A,B,ap))
print("The sub of {} and {} is: {}".format(A,B,sp))
print("The mul of {} and {} is: {}".format(A,B,mp))
print("The div of {} and {} is: {}".format(A,B,dp))
print("The floorDiv of {} and {} is: {}".format(A,B,fdp))
print("The mod {} and {} is: {}".format(A,B,mdp))
print("The Expo of {} and {} is: {}".format(A,B,ep))
print('-'*50)