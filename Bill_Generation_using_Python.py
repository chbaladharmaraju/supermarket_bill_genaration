#displaying the lists
lists="""
Rice  rs 20/kg
Sugar rs 30/kg
Salt  rs 20/kg
Brush rs 20/each piece
Soap  rs 30/each Bar
pen   rs 05/each piece
"""
#list storing 
items={
    "rice":20,
    "sugar":30,
    "salt":20,
    "brush":20,
    "soap":30,
    "pen":5
}
#intilzing the values
llist=[]
qlist=[]
plist=[]
totalprice=0
finalprice=0
print("Welcome to Balu's Super Market !")
#customer detailes
name=input("Enter your name Sir :")

#logic code
option=int(input("Press 1 To buy or 2 to Exit:"))
while option==1:
    if option ==2:
        pass
    if option ==1:
        print(lists)
        item=input("Enter the item  name:")
        if item.lower() in items.keys():
            quantity =int(input("Enter the Quantity:"))
            price=quantity*(items[item])
            llist.append(item)
            qlist.append(quantity)
            plist.append(price)
            option=int(input("press '1' to buy another item or '2' get bill "))

        else:
            print("No item Found As you Entered.")
    else:
        print("You Can't Press the right .")
print(25*"*","Balu's super market",25*"*")
print(28*"-","Invoice Bill",28*"-")
print("customer name:",name.upper())
print("Sno",5*" ","Item name",5*" ","Quantity",5*" ","Price")
print("---",5*" ","---------",5*" ","--------",5*" ","-----")

for i in range(0,len(llist)):
    print(i+1,8*" ",llist[i],10*" ",qlist[i],12*" ",plist[i])
totalprice=sum(plist)
print("Total price :",totalprice)
gst=(sum(plist)*5)/100
print("GST         :",gst)
finalprice=totalprice+gst
print("Final Price :",finalprice)
print(20*"*","Thank you for visting us!",20*"*")





