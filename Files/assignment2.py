


filename=input("Enter file name:")
data=open(filename,'r')
count=0
total=0
for line in data:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
       
        line2=line
        count=count+1
        pos=line2.find(":")
        num=line2[pos+1:]
        numf=float(num)
        total=total+numf
avg=total/count
print(avg)


