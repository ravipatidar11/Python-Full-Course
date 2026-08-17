import calendar as cl
import functools as fct
print(cl.month(2026,7))
print("-----------------------------------")
lst=[10,20,30,40,50,-60]
sumlst=fct.reduce(lambda x,y:x+y,lst)
print(sumlst)
print("-----------------------------------")
pos=list(filter(lambda x:x>0,lst))
print(pos)
print("-----------------------------------")