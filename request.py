#!/usr/bin/env python
# coding: utf-8

# In[10]:


import requests

url = 'http://localhost:5000/predict/'
r = requests.post(url,json={'LotArea':8450, 'YearBuilt':2003, '1stFlrSF':856, '2ndFlrSF':854, 'FullBath':2, 'BedroomAbvGr':3, 'TotRmsAbvGrd':8})

print(r.json())


# In[ ]:




