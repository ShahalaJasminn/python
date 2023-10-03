year=int(input("enter year to be checked:"))
if(year%4==0) & (year%100!=0) | (year%400==0):
    print("the year is leap year")

else:
    print("the year isn't leap year")
