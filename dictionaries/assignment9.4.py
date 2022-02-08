name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
data = open(name,'r')
words=list()
counts=dict()
for line in data:
    if line.startswith("From "):
        words=line.split()[1]
        #print(words)
       
        counts[words]=counts.get(words,0)+1


#print(counts)
maxword=None
maxcount=None
for word,count in counts.items():
    if maxcount is None or count>maxcount:
        maxword=word
        maxcount=count

print(maxword,maxcount)

