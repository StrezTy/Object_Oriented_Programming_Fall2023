import requests, csv, pathlib
from pathlib import Path
import  json
#This is a program that goes through the NY Times API to find articles with Christmas in the travel section
#It goes through the years of 2018-2022 in order to see the results pre, during, and post covid
curr_dir= Path.cwd()
API_KEY= "WVbkR9vJnH5Wf4FAgDAyAKCGpDApL3EH"
URL= "https://api.nytimes.com/svc/search/v2/articlesearch.json"


#function to get parameter for searching NYT API. Takes the input for start date, end date, and the key
def findarticle(start, end, key):

    parameters = {'q': 'christmas', 'api-key': key, "fq":'source:("The New York Times") AND section_name:("Travel")'
                  ,'begin_date': start,'end_date':end}
    return parameters

#variables used for creation or iteeration to find the articles in NYT API
# startlist and endlist are there to iterate year over year
x=0
years=[2018,2019,2020,2021,2022]
startlist=[20180101,20190101,20200101,20210101,20220101]
endlist=  [20181230,20191230,20201230,20211230,20221230]
totaldict={}

#In this for loop the number of articles is recorded and then inputted into a dictionary 
for  i in startlist:
    
    response = requests.get(url=URL, params=findarticle(i, endlist[x], API_KEY))
    content = response.json()
    if 'response' in content:
        hit_count = content['response']['meta']['hits']
        totaldict[years[x]] = hit_count
        print(f"Year: {years[x]}, Hits: {hit_count}")
    else:
        print(f"Year: {years[x]}, Error: No 'response' key found in the response.")
        print(content['response'])
        break

    x+=1
print(totaldict)
#Now we make the csv file that the data will be transferred to.
christmas_data = curr_dir / ("Christmas_data")  
christmas_data.mkdir(exist_ok=True)

christmas_file = christmas_data/("Christmas_Travel_Data.csv")  # file
#Once the csv file is made we write a title and export the data from the dictionary
with open(christmas_file, "w", newline='') as file:
   writer = csv.DictWriter(file, fieldnames=["years", "hit_count"])
   writer.writeheader()
   for key in totaldict.keys():
       file.write("%s,%s\n"%(key, totaldict[key]))