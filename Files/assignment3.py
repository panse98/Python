
from matplotlib import lines


filename="romeo.txt"
data=open(filename,'r')
lst = list()
words=list()
for line in data:
  sentence=line.split()
  for word in sentence:
      words.append(word)

for i in words:
    if i not in lst:
        lst.append(i)
lst.sort()
print(lst)
  





#print(line.rstrip())

