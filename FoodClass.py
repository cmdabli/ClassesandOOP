class Customer:
    def __init__(self, customer_id, name, address, email, phone, member_status):
        self.__custid = customer_id
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__member_status = member_status

    def get_custid(self):
        return self.__custid
     
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

    def __init__(self, date, name, cost, cust_id):
        self.__date = date
        self.__foodname = name
        self.__cost = cost
        self.__custid = cust_id

    def get_date(self):
        return self.__date
    
    def get_foodname(self):
        return self.__date
    
    def get_cost(self):
        return self.__cost
    
    def get_customerid(self):
        return self.__custid
        
    
    
        
    

