#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install lxml


# In[10]:


from lxml import html 
import requests
from bs4 import BeautifulSoup
import pandas as pd

#lxml: specify the html parser we want to use 
#html.text: it is the raw html text


# In[11]:


url= 'https://www.worldometers.info/coronavirus/'
html = requests.get(url)


# In[12]:


print(html.text)


# In[13]:


soup=BeautifulSoup(html.text,'lxml')


# In[14]:


print(soup.prettify())


# In[15]:


soup.h1


# In[16]:


header_h1 = soup.find_all(id="maincounter-wrap")
for head_h1 in header_h1:
    print(head_h1.h1.contents[0])
    print(head_h1.div.span.contents[0],end="\n"*2)


# In[17]:


scrp_table=soup.find('table', id= 'main_table_countries_today')


# In[18]:


scrp_table


# In[19]:


headers = []
for i in scrp_table.find_all('th'):
    title = i.text
    headers.append(title)


# In[20]:


print(title)


# In[21]:


print(headers)


# In[22]:


headers[10]


# In[23]:


headers[13]


# In[24]:


scrapdata=pd.DataFrame(columns=headers)


# In[25]:


for tr in scrp_table.find_all('tr')[1:]:
    row_data=tr.find_all('td')
    row=[td.text for td in row_data]
    length = len(scrapdata)


# In[26]:


print(row_data)


# In[27]:


print(length)


# In[28]:


print(row)


# In[ ]:




