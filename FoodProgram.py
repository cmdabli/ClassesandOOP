import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}

order_total = 0
discount = 0

cust_id = 570
cust_name = 'Danni Sellyar'
cust_address = '97 Mitchell Way Hewitt Texas 76712'
cust_email = 'dsellyarft@gmpg.org'
cust_phone = '254-555-9362'
cust_member = False

#cust_id = 569
#cust_name = 'Aubree Himsworth'
#cust_address = '1172 Moulton Hill Waco Texas 76710'
#cust_email = 'ahimsworthfs@list-manage.com'
#cust_phone = '254-555-2273'
#cust_member = True

customer = fc.Customer(cust_id, cust_name, cust_address, cust_email, cust_phone, cust_member)

print(f'Customer Name: {customer.get_name()}')
print(f'Phone: {customer.get_phone()}')

for row in dict:
    transaction = fc.Transaction(dict[row][0], dict[row][1], dict[row][2], dict[row][3])

    if customer.get_custid() == transaction.get_customerid():
        print(f'Order Item: {transaction.get_foodname()} Price: ${transaction.get_cost():.2f}')
        order_total += transaction.get_cost()
        discount += .2 * transaction.get_cost()
print(f'Total Cost: ${order_total:.2f}')

if customer.get_member_status():
    print(f'Member Discount: ${discount:.2f}')
    order_total -= discount
    print(f'Total Cost after discount: ${order_total:.2f}')
    




