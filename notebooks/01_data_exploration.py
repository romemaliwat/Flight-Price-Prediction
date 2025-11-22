#!/usr/bin/env python
# coding: utf-8

# ## 1. Data Exploration

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Load the dataset
df = pd.read_csv(r"../data/raw/Clean_Dataset.csv")
df


# Features that need to be considered that affect price flight: 
# airline, source_city, destination_city, departure_time, arrival_time, stops, class, duration, days_left
# 
# Target variable: price

# #### Evaluate and have an idea how many different values per feature using .value_counts() for categorical and/or nominal, and min, max, median for numerical.

# In[3]:


df.airline.value_counts()


# In[4]:


df.source_city.value_counts()


# In[5]:


df.destination_city.value_counts()


# In[6]:


df.departure_time.value_counts()


# In[7]:


df.arrival_time.value_counts()


# For these features that only have few different distinct values, OneHotEncoding could be the best approach.

# In[8]:


df.stops.value_counts()


# For the 'stops' feature, since its values are one, zero, and two_or_more ordinal encoding could be the best approach.

# In[9]:


df['class'].value_counts() # df.class won't run because 'class' is a python keyword


# Since class feature only has two values (Economy and Business), binary encoding could be the best approach assigning Economy as 0 and Business as 1.

# In[10]:


print('duration min: ',df.duration.min())
print('duration max: ',df.duration.max())
print('duration median: ',df.duration.median())


# In[11]:


print('days_left min: ',df.days_left.min())
print('days_left max: ',df.days_left.max())
print('days_left median: ',df.days_left.median())


# For the numerical features (duration and days_left), it's best to keep them as it is for now.
