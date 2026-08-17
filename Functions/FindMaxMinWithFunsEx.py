#Program for finding Max and Min from List of Elements
#without using max() and min()
#FindMaxMinWithFunsEx.py
def read_val():
    a=int(input('Enter how many elements u want: '))
    if a<=0:
        return []
    else:
        lst=[]
        for i in range(1,a+1):
            val=float(input('value is {} : '.format(i)))
            lst.append(val)
    return lst

def max_val(lst):
    if len(lst)==0:
        print('No elements')
    else:
        mv=lst[0]
        for val in lst:
            if val>mv:
                mv=val
        else:
            print('Max ({}) = {}'.format(lst,mv))

def min_val(lst):
    if len(lst)==0:
        print('No elements')
    else:
        mv = lst[0]
        for val in lst:
            if val<mv:
                mv=val
        else:
            print('Min ({}) = {}'.format(lst,mv))


#main function

vals=read_val()
max_val(vals)
min_val(vals)