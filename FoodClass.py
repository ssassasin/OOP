class Customer:
    def __init__ (self, customerid, name, address, email, phone, member_status: bool):
        self.__customerid= customerid
        self.__name= name
        self.__address= address
        self.__email= email
        self.__phone= phone
        self.__member_status= member_status

    def get_customerid(self):
        return self.__customerid
        
    def get_name(self):
        return self.__name
        
    def get_address(self):
        return self.__address
        
    def get_email(self):
        return self.__email
        
    def get_phone(self):
        return self.__phone
        
    def get_member_status(self):
        return self.__member_status
    

class Transaction:
    def __init__ (self, customerid, date, item_name, cost):
        self.__customerid= customerid
        self.__date= date
        self.__item_name= item_name
        self.__cost= cost

    def get_customerid(self):
        return self.__customerid
    
    def get_date(self):
        return self.__date
    
    def get_item_name(self):
        return self.__item_name

    def get_cost(self):
        return self.__cost
    




        
