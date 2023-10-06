a=str(input("enter the sentence:"))
b=str(input("enter the word you wnat to count:"))
c=a.split()
count=0
for i in c:
    if i==b:
        count+=1
print("no.of",b,"is",count)              
