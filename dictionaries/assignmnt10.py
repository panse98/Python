
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
data = open(name,'r')


words=list()
hours=list()
counts=dict()
tmp=tuple()
final=list()
for line in data:
    if line.startswith("From "):
        words=line.split()[5]
        hours=words.split(':')[0]
        #print(hours)
        
        counts[hours]=counts.get(hours,0)+1
for k,v in counts.items():
            tmp=(k,v)
            final.append(tmp)
            
finalprint=(sorted(final,reverse=False))

for k,v in finalprint:
    print(k,v)
#print(finalprint)
           


#print(counts)

        #print(hours[0])



