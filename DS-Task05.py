#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import folium
from folium.plugins import HeatMap


# In[3]:


file_path = r'C:\Users\harsh\AccidentsBig.csv'
dtype_spec = {
    'Column8': 'str',
    'Column10': 'str',
    'Column28': 'str',
    'Column29': 'str'
}
data = pd.read_csv(file_path, dtype=dtype_spec, low_memory=False)
data.head()


# In[5]:


data.columns


# In[8]:


data.isnull().sum()
data.dropna(subset=['Date', 'Time', 'Accident_Severity', 'latitude', 'longitude', 'Weather_Conditions'], inplace=True)
data['DateTime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'], format='%d-%m-%Y %H:%M')
data['Hour'] = data['DateTime'].dt.hour
data['DayOfWeek'] = data['DateTime'].dt.dayofweek
data['Month'] = data['DateTime'].dt.month
data['Year'] = data['DateTime'].dt.year


# In[9]:


plt.figure(figsize=(10, 5))
sns.histplot(data['Hour'], bins=24, kde=False)
plt.title('Accidents by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Accidents')
plt.show()


# In[10]:


plt.figure(figsize=(10, 5))
sns.countplot(x='DayOfWeek', data=data)
plt.title('Accidents by Day of Week')
plt.xlabel('Day of Week')
plt.ylabel('Number of Accidents')
plt.show()


# In[19]:


plt.figure(figsize=(12, 6))
sns.countplot(y='Weather_Conditions', data=data, order=data['Weather_Conditions'].value_counts().index)
plt.title('Accidents by Weather Condition')
plt.xlabel('Number of Accidents')
plt.ylabel('Weather Condition')
plt.show()


# In[21]:


sample_data = data.sample(n=10000, random_state=1)
m = folium.Map(location=[sample_data['latitude'].mean(), sample_data['longitude'].mean()], zoom_start=5)
heat_data = [[row['latitude'], row['longitude']] for index, row in sample_data.iterrows()]
HeatMap(heat_data).add_to(m)
output_path = 'C:/Users/harsh/Documents/accident_heatmap.html'
m.save(output_path)
print(f'Heatmap saved to {output_path}')


# In[24]:


plt.figure(figsize=(14, 7))
sns.violinplot(x='Accident_Severity', y='Weather_Conditions', data=data)
plt.title('Severity Distribution by Weather Condition')
plt.xlabel('Severity')
plt.ylabel('Weather Condition')
plt.show()


# In[23]:


plt.figure(figsize=(14, 7))
sns.boxplot(x='Hour', y='Accident_Severity', data=data)
plt.title('Severity Distribution by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Severity')
plt.show()


# In[ ]:




