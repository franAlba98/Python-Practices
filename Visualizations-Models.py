#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os


# In[2]:


os.getcwd()


# In[3]:


movies = pd.read_csv('P4-Movie-Ratings.csv')


# In[4]:


movies


# In[6]:


movies.columns


# In[39]:


movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRatings', 'BudgetMillions','Year']


# In[8]:


movies


# In[9]:


movies.describe()


# In[14]:


movies.Film=movies.Film.astype('category')


# In[15]:


movies.info()


# In[16]:


movies.Genre=movies.Genre.astype('category')
movies.Year=movies.Year.astype('category')


# In[17]:


movies.info()


# In[42]:


movies.describe()


# In[20]:


from matplotlib import pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')


# In[21]:


#Jointplots


# In[23]:


j=sns.jointplot(data=movies, x='CriticRating',y='AudienceRatings')


# In[24]:


j=sns.jointplot(data=movies, x='CriticRating',y='AudienceRatings',kind='hex')


# In[32]:


j=sns.jointplot(data=movies, x='CriticRating',y='AudienceRatings',kind='kde')


# In[33]:


n1 = plt.hist(movies.AudienceRatings,bins=15)
#An histogram with pyplot


# ---

# In[34]:


#Stacked Histograms


# In[41]:


plt.hist(movies.BudgetMillions)
plt.show()


# In[37]:


filter1=movies.Genre == 'Drama'


# In[43]:


movies[filter1].BudgetMillions


# In[44]:


plt.hist(movies[filter1].BudgetMillions)


# In[48]:


plt.hist(movies[movies.Genre == 'Action'].BudgetMillions,bins=15)
plt.hist(movies[movies.Genre == 'Drama'].BudgetMillions,bins=15)
plt.hist(movies[movies.Genre == 'Thriller'].BudgetMillions,bins=15)
plt.show()


# In[50]:


listGenres=[movies[movies.Genre == 'Action'].BudgetMillions,movies[movies.Genre == 'Drama'].BudgetMillions]


# In[52]:


plt.hist(listGenres,bins=15,stacked=True)
plt.show()


# In[61]:


movies.Genre.cat.categories
#.cat.categories return a list with all elements in that category


# In[62]:


for gen in movies.Genre.cat.categories:
    print(gen)


# In[80]:


list=[]
labels=[]
for gen in movies.Genre.cat.categories:
    list.append(movies[movies.Genre == gen].BudgetMillions)
    labels.append(gen)
h=plt.hist(list,bins=30,stacked=True,rwidth=1,label=labels)
plt.legend()
#The thing here is that we can automatize the creation of the histogram for every genre
#If we were to add more genres to the dataset this function will still work


# In[70]:


#KDE plor


# In[74]:


movies.info()


# In[83]:


#Adding a grid to the grphs
sns.set_style('whitegrid')


# In[84]:


vis1=sns.lmplot(data=movies, x='CriticRating',y='AudienceRatings',
               fit_reg=False,hue='Genre',size=7,aspect=1)


# In[86]:


vis1=sns.lmplot(data=movies, x='CriticRating',y='AudienceRatings',
               fit_reg=False,size=7,aspect=1)


# In[90]:


k1=sns.kdeplot(movies.CriticRating,movies.AudienceRatings,size=7,shade=True,shade_lowest=False,cmap='Reds')


# In[93]:


k1=sns.kdeplot(movies.CriticRating,movies.AudienceRatings,size=7,shade=True,shade_lowest=False,cmap='Reds')
k1b=sns.kdeplot(movies.CriticRating,movies.AudienceRatings,size=7,cmap='Reds')
#If I run k1 and k1b together I'm going to get the shades of k1 but the outline of k1b. making much better the graph
#This happens because both graphs overlaps each other


# In[ ]:




