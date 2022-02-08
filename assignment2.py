


import re
from tkinter import N

from sklearn.metrics import top_k_accuracy_score
data=open('data.txt','r')

nums=list()
total=list()
for line in data:
    nums=re.findall('[0-9]+',line)
    for i in range(len(nums)):
        total.append(int(nums[i]))
   
    


Sum=sum(total)
print(Sum)