#InhProg1.py

class C1:
    def disp_c1(self):
        print("C1-disp()")
class C2(C1):
    def disp_c2(self):
        print("C2-disp()")
class C3(C2):
    def disp_c3(self):
        print("C3-disp()")

#Main Program
c3=C3()
c3.disp_c1()
c3.disp_c2()
c3.disp_c3()