#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import requests
get_ipython().system('pip install bs4')
from bs4 import BeautifulSoup


# In[29]:


#headers={'user-agents.net/string/mozilla-5-0-windows-nt-6-3-win64-x64-applewebkit-537-36-khtml-like-gecko-chrome-79-0-3945-79-safari-537-36'}
#webpage=requests.get('https://www.ambitionbox.com/list-of-companies?page=1',headers=headers).text


# In[28]:


#headers={'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}
#webpage=requests.get('https://www.ambitionbox.com/list-of-companies?page=1',headers=headers).text


# In[11]:


import requests

# Correct the headers definition to be a dictionary
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
}

# Make the GET request with the correct headers
webpage = requests.get('https://www.ambitionbox.com/list-of-companies?page=1', headers=headers).text

print(webpage)  # Optional: Print the webpage content


# # use 'soup' for beautifulsoup

# In[13]:


soup = BeautifulSoup(webpage,'lxml')


# In[16]:


#print(soup.prettify())


# # Extrxt the heading line

# In[17]:


for n in soup.find_all('h1'):
    print(n.text.strip())


# In[ ]:





# In[ ]:





# In[ ]:


for n in soup.find_all('h1'):
    print(n.text.strip())


# In[19]:


for n1 in soup.find_all('h2'):
    print(n1.text.strip())


# In[ ]:





# In[ ]:





# In[ ]:





# ### Extract compant rating

# In[23]:


for n2 in soup.find_all('span', class_='companyCardWrapper__companyRatingValue'):
    print(n2.text.strip())


# In[ ]:





# ###  Extract Card Data

# In[24]:


for n3 in soup.find_all('span', class_='companyCardWrapper__interLinking'):
    print(n3.text.strip())


# In[ ]:





# In[ ]:




