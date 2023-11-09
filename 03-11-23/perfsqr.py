list=[]
def square(a,b):
    #list=[]
    for i in range(a,b+1):
        j=1;
        while j*j<=i:
            if j*j==i:
                list.append(str(i))
            j=j+1
        i=i+1
    return list
print(square(1000,9999))

list1=[]
for i in list:
    count=0
    for z in i:
        if int(z)%2==0:
            count=count+1
        else:
            break
    if count==4:
        list1.append(int(i))
print(list1)
