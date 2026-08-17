#program for accepting List of Numerical Integer Values and
# filter +VE Multiples of 3 and 5
#FilterEx1.py

print("Enter list of values separated by a comma: ")
vals=[int(val) for val in input().split(",") if int(val)>0]
print("Given Values: ",vals)
mul35=list(filter(lambda x: x%3==0 and x%5==0,vals))
print("Mul of 3 and 5 =",mul35)
