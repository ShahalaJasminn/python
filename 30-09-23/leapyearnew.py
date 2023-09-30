cyear=int(input("enter the current year:"))
fyear=int(input("enter final year:"))
if cyear < fyear:
    print("here is the list of leap years between ",cyear,"and",fyear,"is:")
while cyear< fyear:
    if (cyear%4==0) & (cyear%100!=0):
           print(cyear)
    if (cyear%100==0) & (cyear %400==0):
           print(cyear)
    cyear=cyear+1
if(cyear>=fyear):
        print("check your year input angain.")
