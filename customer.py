def get_customer_details():
    name=input("Enter customer's name:")
    phone=input("Enter customer's phone number:")

    cust_id=name[:3].upper()+phone[-4:]

    return{
        "name":name,
        "phone": phone,
        "id":cust_id
    }