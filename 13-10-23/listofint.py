i=-1
a=[]
b=[]
while i==-1:
    z=int(input("enter a list on '0' to exit:\n"))
    if z==0:
        break
    else:
        a.append(z)
while i==-1:
    z=(int(input("\n Enter number to list2 or '0' to exit:\n")))
    if z==0:
       break
    else:
        b.append(z)

if len(a)==len(b):
    print("list are same length",(a))
else:
    print("\n list 1:",len(a),"\n list 2:",len(b))
if(sum(a)==sum(b)):
    print("\n both lists have the same sum",sum(a))
else:
    print("\n sum of list1:",sum(a),"\n sum of the list 2:",sum(b))

for n in a:
    for z in b:
        if n==z:
            print("\n",n,"is in both list1 in position",a.index(n),"and list2")
