lst=[0,2,4,0,6,0,1,0,3,0,9]
lst1=[]
for i in lst:
    if i==0:
        lst1.append(lst[i])
while 0 in lst:
    lst.remove(0)
lst1.extend(lst)
print(lst1)

