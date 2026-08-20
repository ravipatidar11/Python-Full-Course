#InhProg2.py

class C1:
    def disp_c1(self):
        print("C1-disp()")
class C2(C1):
    def disp_c2(self):
        print("C2-disp()")
class C3(C1):
    def disp_c3(self):
        print("C3-disp()")

#Main Program
print("w.r.t C2")
o2=C2()
o2.disp_c1()
o2.disp_c2()
#o2.disp_c3  ---- Gives AttributeError
print("w.r.t C3")
o3=C3()
o3.disp_c1()
o3.disp_c3()
#o3.disp_c2()  ---- Gives AttributeError