class Food:
    def __init__(self,Food_id,Food_name,Quantity,Price,Discount):
        self.Food_id=Food_id
        self.Food_name=Food_name
        self.Quantity=Quantity
        self.Price=Price
        self.Discount=Discount
        
    def __str__(self):
        return f"Food Id: {self.Food_id} \nFood Name: {self.Food_name} \nQuantity: {self.Quantity} \nPrice: {self.Price} \nDiscount: {self.Discount} "
        
    def set_Food_id(self,Food_id):
        self.Food_id=Food_id
        
    def get_Food_id(self):
        return self.Food_id
    
    def set_Food_name(self,Food_name):
        self.Food_name=Food_name
        
    def get_Food_name(self):
        self.Food_name
        
    def set_Quantity(self,Quantity):
        self.Quantity=Quantity
        
    def get_Quantity(self):
        self.Quantity
        
    def set_Price(self,Price):
        self.Price=Price
        
    def get_Price(self):
        self.Price
        
    def set_Discount(self,Discount):
        self.Discount=Discount
        
    def get_Discount(self):
        self.Discount
        
        
class Admin:
    def __init__(self,Name,Phone_number,Email,Address,Password):
        self.Name=Name
        self.Phone_number=Phone_number
        self.Email=Email
        self.Address=Address
        self.Password=Password
        
    def set_Name(self,Name):
         self.Name=Name
        
    def get_Name(self):
         return self.Name
    
    def set_Phone_number(self,Phone_number):
         self.Phone_number=Phone_number
        
    def get_Phone_number(self):
         self.Phone_number
            
    def set_Email(self,Email):
         self.Email=Email
        
    def get_Email(self):
         self.Email
        
    def set_Address(self,Address):
         self.Address=Address
        
    def get_Address(self):
         self.Address
        
    def set_Password(self,Password):
         self.Password=Password
        
    def get_Password(self):
         self.Password    