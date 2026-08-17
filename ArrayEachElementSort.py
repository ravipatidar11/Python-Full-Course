lst=[108,298,543]
result=[]
for i in lst:
    str1=str(i)
    sort=sorted(str1)
    x=''.join(sort)
    result.append(x)

print(result ,type(result))

