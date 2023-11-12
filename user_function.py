import random
from user_info import User
import re
class UserInfo:
    Userslist = []
    foodlist=[]
    def User_Register(self):
        Name=str(input("Enter the your name: "))
        Phone_number=str(input("Enter your contact: "))
        length = len(Phone_number)
        if length == 10:
            pass
        else:
            Phone_number=str(input("Minimum having 10 dugits: "))
        Email=str(input("Enter your Email Address: "))
        res=re.findall(r"^[a-zA-Z0-9]+[@][a-z+]+[.]{1}[a-z]+$", Email)
        if res:
            pass
        else:
            Email=str(input("Please Enter the Correct email: "))
        Address=str(input("Enter your Address: "))
        Password=str(input("Set the Password: "))
        if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', Password):
            pass
        else:
            Password=str(input("The Password have minimum 8 characters: "))
        User_obj=User(Name,Phone_number,Email,Address,Password)
        self.Userslist.append(User_obj)
        print("Registered Successfully!")
                
    def place_new_order(self):
        lst=[]
        #lst2=[]
        lst1=["1.Thandori (4 pieces) [INR 240]","2.Vegan Burger (1 Piece) [INR 320]","3.Truffle Cake (500gm) [INR 900] "]
        for i in lst1:
            print(i)
        choose=int(input("Please Enter how many you want to oder: "))
        for i in range(int(choose)):
            l=int(input())
            if l==1:
                self.foodlist.append(lst1[0])
            elif l==2:
                self.foodlist.append(lst1[1])
            elif l==3:
                self.foodlist.append(lst1[2])
            lst.append(l)
        print("you selected food is!: ")
        for j in self.foodlist:
            print(j)
        place=input("Do you want place these orders: ")
        if place=='yes':
            print("Thank you! your order is placed: ")
            #sys.exit()
        else:
            pass
        
    def update_profile(self):
        Email=str(input("Enter your Email Address: "))
        res=re.findall(r"^[a-zA-Z0-9]+[@][a-z+]+[.]{1}[a-z]+$", Email)
        if res:
            pass
        else:
            Email=str(input("Please Enter the Correct email: "))
        for lg in self.Userslist:
            if lg.Email == Email:
                Name=str(input("Enter the your name: "))
                Phone_number=str(input("Enter your contact: "))
                length = len(Phone_number)
                if length == 10:
                    pass
                else:
                    Phone_number=str(input("Minimum having 10 dugits: "))
                Address=str(input("Enter your Address: "))
                Password=str(input("Set the Password: "))
                if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', Password):
                    pass
                else:
                    Password=str(input("The Password have minimum 8 characters: "))
                
                lg.set_Name(Name)
                lg.set_Phone_number(Phone_number)
                lg.set_Address(Address)
                lg.set_Password(Password)
                
                print("Profile Information Successfully Updated! ")
                break
        else:
            print("Invalid Email! ")

    
    def order_history(self):
        print("your order history is: ")
        for i in self.foodlist:
            print(i)