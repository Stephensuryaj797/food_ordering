from user_function import*
class UserMain:

    def __init__(self,userfunction_obj):
        self.userfunction_obj=userfunction_obj


    def Userchoice(self,select):
        if select==1:
            print("*************Register******************")
            self.userfunction_obj.User_Register()

        elif select==2:
            print("*************Login*******************")
            for info in userfunction_obj.Userslist:
                Email=str(input("Enter your Email Address: "))
                res=re.findall(r"^[a-zA-Z0-9]+[@][a-z+]+[.]{1}[a-z]+$", Email)
                if res:
                    if info.Email==Email:
                        Password=str(input("Enter your Password!"))
                        password=re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', Password)
                        if password:
                            for psw in userfunction_obj.Userslist:
                                if psw.Password==Password:
                                    print("Login Successfully")
                                    while True:
                                        print("1. Place new Order: \n2. Update Profile: \n3. Order History: \n")
                                        option=int(input("Enter your option: "))
                                        if option==1:
                                            self.userfunction_obj.place_new_order()
                                        elif option==2:
                                            self.userfunction_obj.update_profile()
                                        elif option==3:
                                            self.userfunction_obj.order_history()
                                        else:
                                            print("Sorry! you entere wrong option")
                                            print("Thank you! you have log out successfully! if you want to continue please login! ")
                                            break
                            else:
                                print("Incorrect Password!")
                print("You have not Registered!")
                break
                            
if __name__=="__main__":
    
    userfunction_obj=UserInfo()
    usermain_obj=UserMain(userfunction_obj)                                            
                                            
                                            
    while True:
        print("1.Register: \n2.Login: ")
        select=int(input("Enter your choice: "))
        usermain_obj.Userchoice(select)                                        
                                    