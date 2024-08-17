#!/usr/bin/env python
# coding: utf-8

# In[4]:


import warnings
warnings.filterwarnings("ignore")


# In[5]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


df1=pd.read_csv("Unemployment in India.csv")
df2=pd.read_csv("Unemployment_Rate_upto_11_2020.csv")


# In[7]:


df1.head()


# In[8]:


df1.tail()


# In[9]:


df1.shape


# In[10]:


df1.info()


# In[11]:


df1.isnull().sum()


# In[12]:


df1=df1.dropna()


# In[13]:


df1.isnull().sum()


# In[14]:


df1.describe()


# In[15]:


plt.figure(figsize=(15,10))
sns.countplot(y="Region",data=df1)
plt.show()


# In[25]:


df2.head()


# In[26]:


print(df2.isnull().sum())


# In[27]:


df2.columns= ["States","Date","Frequency",
               "Estimated Unemployment Rate",
               "Estimated Employed",
               "Estimated Labour Participation Rate",
               "Region","longitude","latitude"]


# In[31]:


df2.columns= ["States","Date","Frequency",
               "Estimated Unemployment Rate","Estimated Employed",
               "Estimated Labour Participation Rate","Region",
               "longitude","latitude"]
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Employed", hue="Region", data=df2)
plt.show()


# In[32]:


plt.figure(figsize=(12, 10))
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Unemployment Rate", hue="Region", data=df2)
plt.show()


# In[33]:


unemploment = df2[["States", "Region", "Estimated Unemployment Rate"]]
figure = px.sunburst(unemploment, path=["Region", "States"], 
                     values="Estimated Unemployment Rate", 
                     width=700, height=700, color_continuous_scale="RdY1Gn", 
                     title="Unemployment Rate in India")
figure.show()


# In[36]:


round(df2[['Estimated Unemployment Rate', 'Estimated Employed', 'Estimated Labour Participation Rate']].describe().T,2)

#rounded to 2 decimal points and transposed to get a horizontal version


# In[37]:


regionStats = df2.groupby(['Region'])[['Estimated Unemployment Rate',
                                      'Estimated Employed',
                                      'Estimated Labour Participation Rate']].mean().reset_index()

#rounding the values to 2 decimal points
round(regionStats,2)


# In[38]:


#constructing a 'heatMap' to find the 'pair-wise correlation' values

#dataframe of all the numerical columns
heatMap = df2[['Estimated Unemployment Rate', 'Estimated Employed', 
              'Estimated Labour Participation Rate', 'longitude', 'latitude']]

#constructing on heatMap with correlation values
heatMap = heatMap.corr()

#plotting the figure
plt.figure(figsize=(23,8))
sns.heatmap(heatMap, annot=True,cmap='twilight_shifted', fmt='.3f', linewidths=1)
plt.title('heatMap')
plt.show()


# In[39]:


fig = px.box(
    df2,
    x='States',
    y='Estimated Unemployment Rate',
    color='States',
    title='unemploymentRate',
    template='plotly'
)
fig.show()


# In[41]:


newDF = df2[['Estimated Unemployment Rate','States']]

#grouping the dataframe by 'States' and finding the corresponding 'mean'
newDF = newDF.groupby('States').mean().reset_index()

#sorting the values in the dataframe
newDF = newDF.sort_values('Estimated Unemployment Rate')

fig = px.bar(newDF, 
             x='States',
             y='Estimated Unemployment Rate',
             color='States',
             title='State-wise Average Employment Rate')
fig.show()


# In[45]:





# In[ ]:




