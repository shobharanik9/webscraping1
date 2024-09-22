#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[ ]:


# url = "https://www.Naukri.com/"
response = requests.get(url)


# In[34]:


soup = BeautifulSoup(response.content,'html.parser')


# In[36]:


search_button = soup.find('button',{'id':'btn_search'})
response = requests.post(url,data={'txt_search': 'Data Scientist'})


# In[48]:


soup = BeautifulSoup(response.content,'html.parser')
location_filter = soup.find('input', {'id':'chk_location'})
location_filter['checked'] = True
salary_filter = soup.find('input',{'id':'chk_salary'})
salary_filter['checked'] = True


# In[49]:


job_listings = soup.find_all('div', {'class': 'w-100'})
data= []
for job in job_listings[:10]:
    title = job.find('h3').text.strip()
    location = job.find('span',{'class': 'location'}).text.strip()
    company = job.find('span',{'company-name'}).text.strip()
    experience = job.find('span',{'class':'exp'}).text.strip()
    data.append([title, location, company, experience])


# In[50]:


df = pd.DataFrame(data, columns=['job Title', 'job location', 'company name', 'experience required'])


# In[ ]:


# import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[ ]:


# step 1: Get webpage
url = "https://www.Shine.com"
response = requests.get(url)


# In[7]:


# step 2: enter search criteria and click search button
job_title = "Data Scientist"
job_location = "Delhi"
payload = {"search_query": job_title,"loc_query": job_location}
response=requests.post(url,data=payload)


# In[9]:


#step 3: Scrape the data for the first 10 jobs
soup = BeautifulSoup(response.content,"html.parser")
job_results = soup.find_all("div",class_="result-display")
job_data = []
for result in job_results[:10]:
    title = result.find("h2").text.strip()
    company = result.find("span",class_="company-name").text.strip()
    location = result.find("span",class_="location").text.strip()
    job_data.append({"job Title":title, "Company name": company,"Location": location})


# In[10]:


# step 4: Create a datframe of the scraped data
df = pd.DataFrame(job_data)
# print the dataframe
print(df)


# In[1]:


# Load the necessary libraries

from bs4 import BeautifulSoup as bs #bs4 stands for Beautifulsoup4

import requests 

name_list = []
rating_list = []
review_list = []
 #find_all() will give all the content of specif

for page in range(1,1105):
    
    url = "https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&page="+str(page)
    status_code = requests.get(url)


 #get() sends a HTTP GET request and receive a response

    #get() returns a HTTP status code of response

    #If status code is 200 then OK 
    #If status code is 404 then page not found
    #If status code is 503 for server unavailable currently, etc
    
    if str(status_code) == "<Response [200]>":
        
        soup = bs(status_code.content,'html.parser') # soup is an object of bs 
        
        print("Started to scrape page ",page)
   

#From inspect, click on select option (top right corner in inpect tab)
    #then click on any name of customer on page to get the name tag and it's class name
        
        
        names = soup.find_all('p',class_='_2sc7ZR _2V5EHH')
        
    

  # same with ratings and reviews
        
        ratings = soup.find_all('div',class_='_3LWZlK _1BLPMq')
        reviews = soup.find_all('div',class_='t-ZTKy')
      

for page in range(1,100):
    
    url = "https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPCART PAGE="+str(page)
    status_code = requests.get(url)


#get() sends a HTTP GET request and receive a response

    #get() returns a HTTP status code of response

    #If status code is 200 then OK 
    #If status code is 404 then page not found
    #If status code is 503 for server unavailable currently, etc
    
    if str(status_code) == "<Response [200]>":
        
        soup = bs(status_code.content,'html.parser') # soup is an object of bs 
        
        print("Started to scrape page ",page)
    

 #From inspect, click on select option (top right corner in inpect tab)
    #then click on any name of customer on page to get the name tag and it's class name
        
        
        names = soup.find_all('p',class_='_2sc7ZR _2V5EHH')
   

 # same with ratings and reviews
        
        ratings = soup.find_all('div',class_='_3LWZlK _1BLPMq')
        reviews = soup.find_all('div',class_='t-ZTKy')
        
       

 #find_all() will give all the content of specified tag and class
        
        for i in range(len(names)):
            name_list.append(names[i].get_text())
            if len(ratings) > i:
                rating_list.append(ratings[i].get_text())
            else:
                rating_list.append("N/A")
            if len(reviews) > i:
                review_list.append(reviews[i].get_text())
            else:
                review_list.append("N/A")
            
        print("Page ",page," scraped succesfully")
            



# In[2]:


import requests
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.content,'html.parser')


# In[ ]:


url = "https://www.flipcart.com/"
search_query = "sneakers"
max_listings = 100
scraped_data =[]


# In[ ]:


listings_container = soup.find("div", attrs={"class"})
# Extract the required attributes from each listing for listing in
brand = listing.find("div", attrs={"class"})
price = listing.find("div",attrs={"class"})


# In[ ]:


scraped_data.append({"Brand": brand, "ProductDescription": description, "Price": price})


# In[ ]:


#Find the "Next" button and navigate to the next page
next_button = soup.find("a",attrs={"class"})
if next_button:url = "https://www.flipcart.com" + next_button["herf"]
else:
#print the scraped data
 print(data)


# In[ ]:





# In[ ]:


# import requests
from bs4 import BeautifulSoup

url = "https://www.azquotes.com/"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

response = requests.get(url)
top_quotes_html = response.content

top_quotes_soup = BeautifulSoup(top_quotes_html, "html.parser")

quote_container = top_quotes_soup.find("div", class_="list-quotes")

  # Extract the quote text
  quote = quote.find("a", class_="title").text
  
  # Extract the author
  author = quote.find("a", class_="author").text
  
  # Extract the type of quote
  quote_type = quote.find("div", class_="quote-tags").text
  
  # Print or store the extracted data as per your requirement
  print("Quote:", quote_text)
  print("Author:", author)
  print("Type of Quote:", quote_type)
  print()


# In[ ]:


from salenium import webdriver
import pandas as pd
Set up the Selenium webdriver:
driver = webdriver.Chrome('path_to_chromedriver')
Make sure you have downloaded the ChromeDriver executable and provided the correct path.

Open the webpage:
driver.get('https://www.jagranjosh.com/')
Click on the "GK" option:
gk_option = driver.find_element_by_link_text('GK')
gk_option.click()
Click on the "List of all Prime Ministers of India":
pm_option = driver.find_element_by_link_text('List of all Prime Ministers of India')
pm_option.click()
Scrape the data:
data = []
table = driver.find_element_by_xpath('//table[@class="table4"]')
rows = table.find_elements_by_tag_name('tr')
for row in rows:
  cols = row.find_elements_by_tag_name('td')
  if len(cols) == 4:
  name = cols[0].text
  born_dead = cols[1].text
  term_of_office = cols[2].text
  remarks = cols[3].text
  data.append([name, born_dead, term_of_office, remarks])
Create a DataFrame:
df = pd.DataFrame(data, columns=['Name', 'Born-Dead', 'Term of Office', 'Remarks'])
Close the webdriver:
driver.quit()


# In[ ]:


from selenium import webdriver
import pandas as pd

# Step 1: Get the webpage
driver = webdriver.Chrome('path_to_chromedriver')  # Replace 'path_to_chromedriver' with the actual path to your ChromeDriver executable
driver.get('https://www.motor1.com/')

# Step 2: Type in the search bar
search_bar = driver.find_element_by_id('search-input')
search_bar.send_keys('50 most expensive cars')
search_bar.submit()

# Step 3: Click on the link
link = driver.find_element_by_link_text('50 Most Expensive Cars in the World')
link.click()

# Step 4: Scrape the data and create a dataframe
car_names = driver.find_elements_by_xpath('//div[@class="article-content"]/h3')
car_prices = driver.find_elements_by_xpath('//div[@class="article-content"]/p')

data = []
for name, price in zip(car_names, car_prices):
  data.append([name.text, price.text])

df = pd.DataFrame(data, columns=['Car Name', 'Price'])
print(df)

driver.quit()

