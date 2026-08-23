import random
import string

passwords = {}

#load existing password file

try:
    with open("password.txt", "r") as file:
        for line in file:
            website,pwd = line.strip().split(":")
            passwords[website] = pwd
except:
    pass

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&"
    password = "".join(random.choice(chars) for _   in range(8))
    return password

while True:
     print("\n-------PERSONAL PASSWORD MANGER-------")
     print("1. Save password")
     print("2. View password")
     print("3. Generate password")
     print("4. Exit")

     print("-------------------------------")
     choice = input("Enter your choice: ")
     print("-------------------------------")

     if choice == "1":
         site = input("Enter website: ")
         pwd = input("Enter password: ")

         passwords[site] = pwd

         with open("password.txt", "a") as file:
             file.write(f"{site}:{pwd}\n")

         print("Password saved")
         print("-------------------------------")

     elif choice == "2":
         if not passwords:
             print("No Data")
         else:
             for site, pwd in passwords.items():
                 print(site,":",pwd)
         print("-------------------------------")
     elif choice == "3":
         print("Generate password",generate_password())
         print("-------------------------------")
     elif choice == "4":
         print("Ok Bye..")
         break
     else:
         print("Invalid Input")
         print("-------------------------------")