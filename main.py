from food_adding import*
import re
class FoodMain:
    def __init__(self,foodfunction_obj):
        self.foodfunction_obj=foodfunction_obj
        
    def execute(self,choice):
        if choice==1:
            print("****************Register******************")
            self.foodfunction_obj.Admin_Register()
            
        elif choice==2:
            print("*****************Login****************")
            for info in foodfunction_obj.adminlist:
                Email=str(input("Enter your Email Address: "))
                res=re.findall(r"^[a-zA-Z0-9]+[@][a-z+]+[.]{1}[a-z]+$", Email)
                if res:
                    if info.Email==Email:
                        Password=str(input("Enter your Password!"))
                        password=re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', Password)
                        if password:
                            for psw in foodfunction_obj.adminlist:
                                if psw.Password==Password:
                                    print("Login Successfully")
                                    while True:
                                        print("1. Add Food: \n2.View Food List: \n3. Update Food to the Menu: \n4. Delete the Food from the Menu: \n")
                                        option=int(input("Enter your option: "))
                                        if option==1:
                                            self.foodfunction_obj.add_food()
                                        elif option==2:
                                            self.foodfunction_obj.view_food()
                                        elif option==3:
                                            self.foodfunction_obj.update_food()
                                        elif option==4:
                                            self.foodfunction_obj.delete_food()
                                        else:
                                            print("Sorry! you entere wrong option")
                                            print("Thank you! you have log out successfully! if you want to continue please login! ")
                                            break
                            else:
                                print("Incorrect Password!")
                print("You have not Registered!")
                break
            
if __name__=="__main__":
    
    foodfunction_obj=FoodAdding()
    foodmain_obj=FoodMain(foodfunction_obj)
    
    while True:
        try:
            print("1.Register: \n2.Login: ")
            choice=int(input("Enter your choice: "))
            foodmain_obj.execute(choice)
        except Exception as ex:
            print("you eneter wrong choice! please select correct one!  ")
