#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
import time
import datetime
from win10toast import ToastNotifier


# In[13]:


try:
    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"
    querystring = {"country":"India"}
    headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "a52598e6cfmsh6bdb985ec3068a0p1395d6jsn3202bb7d79fe"
    }
    res = requests.request("GET", url, headers=headers, params=querystring)
except:
    res=None
    print("Check your network connection")
    
if res is not None:
    data=res.json()
    toaster=ToastNotifier()
    title="Covid19 India Latest News Update {}".format(datetime.date.today())
    
    news="Total Confirmed cases are: {} , Deaths: {} , Recovered: {}".format(data['data']['confirmed'],data['data']['deaths'],data['data']['recovered'])
    toaster.show_toast(title, news, duration=30)


# In[ ]:





# In[ ]:




