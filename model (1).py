#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle


# In[18]:


df = pd.read_csv('house_predict.csv')


# In[19]:


df.head()


# In[20]:


df.columns


# In[21]:


feature_names = ['LotArea','YearBuilt','1stFlrSF','2ndFlrSF','FullBath','BedroomAbvGr','TotRmsAbvGrd']


# In[22]:


X = df[feature_names]


# In[23]:


X.head()


# In[24]:


y = df['SalePrice']


# In[25]:


y


# In[26]:


X.isnull().sum()


# In[27]:


X.astype('int64')


# In[28]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.75,random_state = 0)


# In[29]:


from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators = 500,random_state = 1)
regressor.fit(X_train,y_train)


# In[30]:


pickle.dump(regressor,open('model.pkl','wb'))


# In[31]:


model = pickle.load(open('model.pkl','rb'))


# In[32]:


print(model.predict([[8450,2003,856,854,2,3,8]]))


# In[48]:





# In[ ]:





# In[ ]:




