fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

data= open(fname,'r')
count = 0
lst=list()
for line in data:
    words=line.rstrip()
    if words.startswith("From "):
        count=count+1
    
        lst=words.split()
        print(lst[1])


print("There were", count, "lines in the file with From as the first word")
