import random
from food import Food,Admin
import re
class FoodAdding:
    FoodList = []
    adminlist = []
    def add_food(self):
       # book_id=int(input("Enter book id: "))
        f_id=random.randint(1, 101)
        Food_id=int(f_id)
        Food_id1=print("Food id is: ", Food_id)
        Food_name=str(input("Enter the Food name: "))
        Quantity=str(input("enter quantity: "))
        Price=str(input("Enter the Food Price: "))
        Discount=str(input("Enter the Discount: "))
        food_obj=Food(Food_id,Food_name,Quantity,Price,Discount)
        self.FoodList.append(food_obj)
        print("Successfully Food Added to the Menu!")
        
    def view_food(self):
        for i in self.FoodList:
            print("*************")
            print(i)

    def update_food(self):
        Food_id = int(input("Enter Food Id of the Food you want to update : "))
        for foods in self.FoodList:
            if foods.Food_id == Food_id:
                Food_name = str(input("Enter Food Name : "))
                Quantity = str(input("Enter Food Quantity : "))
                Price = str(input("Enter Food Price : "))
                Discount=str(input("Enter the Discount: "))
                
                foods.set_Food_name(Food_name)
                foods.set_Quantity(Quantity)
                foods.set_Price(Price)
                foods.set_Discount(Discount)
                
                print("Successfully Food Updated to the Menu")
                break
        else:
            print("No Food found!")

            
    def delete_food(self):
        Food_id=int(input("Enter Food id you want to delete: "))
        for foods in self.FoodList:
            if foods.Food_id==Food_id:
                self.FoodList.remove(foods)
                print("Food deleted successfully!")
                break
        else:
            print("No Food having Id you entered")
    
    def Admin_Register(self):
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
        Admin_obj=Admin(Name,Phone_number,Email,Address,Password)
        self.adminlist.append(Admin_obj)
        print("Registered Successfully!")
        