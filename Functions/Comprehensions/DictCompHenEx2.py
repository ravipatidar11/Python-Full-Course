#Program for Reading List of + Values and find their Squares from Key Board
#DictCompHenEx3.py
print("Enter List of Values Separated by comma")
d={float(val):float(val)**2 for val in input().split(",") if float(val)>0 }
print(d)