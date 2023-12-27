#you may need to run "pip install beautifulsoup4" and "pip install requests" in your virtual environment for the code to run properly
from bs4 import BeautifulSoup
import requests
#Using beautiful soup I will be going through webpages and 
# 1) Gathering all the links on the page and whether they lead to a different site or just another chain on the current website. count the links that lead away and the ones that lead to for comparison
# 2) Go through all the text on the webpage and count the words 
# 3) Finds how many descendents of the webpage have proper tag names and how many are classified as none

#first we have to find a webpage let's say rutgers' main page rutgers.edu

url= "https://www.rutgers.edu/"
request= requests.get(url)
samelink= 0
differentlink= 0
totalcount=0
soup= BeautifulSoup(request.text, "html.parser")
#go through all the links under than page's a tags as well as find if they lead to rutgers subpages
for i in soup.find_all("a"):
    link= i.get("href")
    if "rutgers.edu" in link.lower():
        samelink+=1
    else:
        differentlink+=1
    totalcount+=1
#print the amount of links that lead away from rutgers or back into rutgers as well as the total amount of pages
print(f'The amount of links that lead to other rutgers subpages are {samelink}')
print(f'The amount of links that lead to other webpages are {differentlink}')
print(f'The total amount of links on this page is {totalcount}')

# create new counters and the like to count words.
wordcount= 0

alltext= soup.get_text()
#loop to go over all the letters in the text on the page
for letter in alltext:
    if letter == " ":
        wordcount+=1
print(f'The total amount of words on this webpage is {wordcount}')

#Create a counter variable  
none_counter=0
tag_counter=0
#loop over all of the children in soup, then take the name of each tag to determine if it has a name or is classified as none
for child in soup.descendants:
    if child.name == None:
        none_counter+=1
    else:
        tag_counter+=1
print(f'The amount of descendants that have proper tag names is {tag_counter}')
print(f'The amount of descendants that do not have proper tag names i.e. none is {none_counter}')
