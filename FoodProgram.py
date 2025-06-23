import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

transactions = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}

#Non-Member Danni Sellyar
customer= fc.Customer(570, 'Danni Sellyar', '97 Mitchell Way Hewitt Texas 76712', 'dsellyarft@gmpg.org', '254-555-9362', False)


#Member Aubree Himsworth
#customer= fc.Customer(569, 'Aubree Himsworth', '1172 Moulton Hill Waco Texas 76710', 'ahimsworthfs@list-manage.com', '254-555-2273',True)

print(f"Customer Name: {customer.get_name()}")
print(f"Phone: {customer.get_phone()}")

order_total = 0

for t in transactions.values():
    date, item_name, cost, cust_id= t
    if cust_id == customer.get_customerid():
        print(f"Order Item: {item_name} Price: ${cost: .2f}")
        order_total+= cost

print(f"Total Cost: ${order_total: .2f}")

if customer.get_member_status():
    discount= order_total * .2
    final_total= order_total - discount
    print(f"Member Discount: ${discount: .2f}")
    print(f"Total cost after the discount: ${final_total: .2f}")




