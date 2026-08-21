#College.py

from University import University
class College(University):
    def get_data(self):
        self.cname=input("enter College Name:")
        self.cloc=input("enter College Location:")
        super().get_data()
    def disp_data(self):
        print("----------------------------------------")
        print("College Details")
        print("----------------------------------------")
        print("College Name:",self.cname)
        print("College Location:",self.cloc)
        print("----------------------------------------")