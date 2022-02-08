filename=input("Enter file name:")
data=open(filename,'r')
for line in data:
    print(line.upper().strip())