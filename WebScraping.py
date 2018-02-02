#Link being scarped:
#https://www.hitachivantara.com/en-us/news-resources/press-releases/2017/gl171213.html

#importing the BeautifulSoup library 
from bs4 import BeautifulSoup
import sys

#accessing the URL via Python
import requests

r  = requests.get("https://finance.yahoo.com/news/zerostack-sees-growing-demand-self-070000239.html")

data = r.text

#Output stored in a text file on the local system
f=open(r'C:\Users\Shravya.Shanmukh\Desktop\Work\Web Scraping\PR\Random\R106.txt', "w",encoding='utf-8')

#Parser - HTML
soup = BeautifulSoup(data,'html.parser')

#Looping through all the <p> tags in the HTML source code
for link in soup.find_all('p'):
    f.write(link.text)

#Close file
f.close()