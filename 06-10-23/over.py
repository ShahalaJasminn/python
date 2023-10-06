a=int(input("enter the number limit:"))

b=[]
v="over"
for i in range(0,a):
    lst=int(input("enter elements:"))
    if lst<99:
        b.append(lst)
    else:
        b.append(v)
        
print(b)
    

