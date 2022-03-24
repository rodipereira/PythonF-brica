#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


pip install matplotlib


# In[3]:


df1 =  pd.read_csv("C:\\Users\\roddy\\Desktop\\pythonex\\iris.csv")


# In[4]:


df1


# In[5]:


from matplotlib.pyplot import figure
figure(figsize = (15,6),dpi=80)


# In[8]:


p= df1['variety'] 
t=df1 ['sepal.length']
plt.plot(p,t,color='#E6B89C',lw=10)


# In[9]:


df1.sort_values(by='petal.length', ascending = True)


# In[ ]:




