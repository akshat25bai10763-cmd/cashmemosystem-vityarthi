import customer

#def cashmemo():
a=input("Enter Shop Name:")
n=int(input("Enter invoice number:"))
v=int(input("Enter total number of items to be billed:"))
cust=customer.get_customer_details()
items=[]
   
for j in range(v):
    i=input('Enter item Name:')
    q=int(input('Enter Quantity of Item:'))
    c=int(input('Enter each item Price:'))
    h=q*c
    items.append([i,q,c,h])

    print("------------------------")
    print("        Cash Memo      ")
    print("       ",a,"           ")
    print("Invoice number:",n)
    print("Customer ID:",cust["id"])
    print("Customer Name:", cust["name"])
    print("Phone:",cust["phone"])
    print("------------------------")
    print("Items                Qty    Rate    Total")

    grand_total=0
    for item in items:
        print(f"{item[0]:15} {item[1]:5} {item[2]:6} {item[3]:7}")
        grand_total+=item[3]
        print("------------------------")
        print("Grand Total",grand_total)
        print("------------------------")
    

#cashmemo()