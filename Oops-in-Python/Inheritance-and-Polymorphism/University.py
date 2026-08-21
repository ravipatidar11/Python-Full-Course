#University.py
class University:
    def get_data(self):
        self.uname = input("enter university name:")
        self.uloc = input("enter university location:")


    def disp_data(self):
        print("----------------------------------------")
        print("University Details")
        print("----------------------------------------")
        print("University Name:", self.uname)
        print("University Location:", self.uloc)
        print("----------------------------------------")
