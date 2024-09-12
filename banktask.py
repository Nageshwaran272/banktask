names=["Naga","Priya","Mythu","Nisha","Arun"]
amount=[1000,2000,3000,4000,5000]
a=input("Enter a sender:")
b=input("Enter a rechiver:")
c=int(input("Enter the amount:"))
for i in names:
    if(i==a):
        print("Sender is available")
        y=(names.index(i))
        print("The sender balance",amount[y])
        print("the sender current balance :",amount[y]-c)
        print("sender debited amount",c)
        break
for j in names:
    if(j==b):
        print("rechiver name:",b)
        x=(names.index(j))
        print("The rechiver  balance :",amount[x])
        print("The rechiver current balance:",amount[x]+c)
        break
   
