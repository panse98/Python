import re
from turtle import position
from unicodedata import name
from bs4 import BeautifulSoup

 
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
counts=int(input('Enter count: '))
names=list()
position=int(input('Enter position: '))

for i in range(counts):
   
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup('a')
  



    
    url=tags[position].get('href', None)
  
    names.append(tags[position].contents[0])
    i=i+1
    print(url)
print(names)
   
   

