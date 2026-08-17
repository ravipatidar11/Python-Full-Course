lst=[0,2,4,0,6,0,1,0,3,0,9]

count=lst.count(0)

while 0 in lst:
    lst.remove(0)

for i in range(count):
    lst.insert(0,0)

print(lst)