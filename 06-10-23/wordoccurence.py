ab=['aa','bab','cab','bbb','cca','abb']

count=0
a=str(input("word to search:"))
for i in ab:
    for f in i:
        if (f == "a"):
            count=count+1
print("count of ",a,"in",ab,"is",count)
