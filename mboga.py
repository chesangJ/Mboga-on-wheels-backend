
class Customer:
    def __init__(self):
        email= input('enter your email')
        print('your email is:',email)
        # self.email=email
    def signUp(self):
        name= input('enter your name')
        print('your name is:',name)

        

        phone_number= input('enter your phone number')
        print('your phone number is:',phone_number)

        password= input('enter your password')
        print('your password is:',password)
        print(f"your data has been saved")
    

    def login(self,email):
        login_email= input('enter your email')
        if(login_email!= email):
            print("email not correct")
        p_number= input('enter your phone number')
        print('your name is:',p_number)

    
        location= input('enter your location')
        print('your location is:',location)
        
        print('SUCCESSFULY LOGGED IN')


    
customer1=Customer()
customer1.signUp()
print("YOUR ACCOUNT HAS BEEN CREATED, YOU CAN LOGIN")
customer1.login("joyeuse@gmail.com")
  
   
  

class Stock:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    def add_stock(self, quantity):
        self.quantity += quantity
    def remove_stock(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
        else:
            print(f"Not enough {self.name} in stock")