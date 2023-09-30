cyear=int(input("enter the current year:"))
fyear=int(input("enter final year:"))
for i in range(cyear,fyear+1):
    if (i%4==0) & (i%100!=0) | (i%400==0):
        print(i)
