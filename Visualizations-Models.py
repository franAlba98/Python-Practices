#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import os


# In[3]:


os.getcwd()


# In[4]:


movies = pd.read_csv('P4-Movie-Ratings.csv')


# In[5]:


movies


# In[6]:


movies.columns


# In[7]:


movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRatings', 'BudgetMillions','Year']


# In[8]:


movies


# In[9]:


movies.describe()


# In[10]:


movies.Film=movies.Film.astype('category')


# In[11]:


movies.info()


# In[12]:


movies.Genre=movies.Genre.astype('category')
movies.Year=movies.Year.astype('category')


# In[13]:


movies.info()


# In[14]:


movies.describe()


# In[15]:


from matplotlib import pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')


# In[16]:


#Jointplots


# In[17]:


j=sns.jointplot(data=movies, x='CriticRating',y='AudienceRatings')


# In[18]:


j=sns.jointplot(data=movies, x='CriticRating',y='AudienceRatings',kind='hex')


# In[19]:


j=sns.jointplot(data=movies, x='CriticRating',y='AudienceRatings',kind='kde')


# In[20]:


#scatter
#sc=sns.scatterplot(data=movies,x='CriticRating',y='AudienceRatings')
reg=sns.regplot(data=movies,x='CriticRating',y='AudienceRatings')


# In[21]:


n1 = plt.hist(movies.AudienceRatings,bins=15)
#An histogram with pyplot


# ---

# In[22]:


#Stacked Histograms


# In[23]:


plt.hist(movies.BudgetMillions)
plt.show()


# In[24]:


filter1=movies.Genre == 'Drama'


# In[25]:


movies[filter1].BudgetMillions


# In[26]:


plt.hist(movies[filter1].BudgetMillions)


# In[27]:


plt.hist(movies[movies.Genre == 'Action'].BudgetMillions,bins=15)
plt.hist(movies[movies.Genre == 'Drama'].BudgetMillions,bins=15)
plt.hist(movies[movies.Genre == 'Thriller'].BudgetMillions,bins=15)
plt.show()


# In[28]:


listGenres=[movies[movies.Genre == 'Action'].BudgetMillions,movies[movies.Genre == 'Drama'].BudgetMillions]


# In[29]:


plt.hist(listGenres,bins=15,stacked=True)
plt.show()


# In[30]:


movies.Genre.cat.categories
#.cat.categories return a list with all elements in that category


# In[31]:


for gen in movies.Genre.cat.categories:
    print(gen)


# In[32]:


list=[]
labels=[]
for gen in movies.Genre.cat.categories:
    list.append(movies[movies.Genre == gen].BudgetMillions)
    labels.append(gen)
h=plt.hist(list,bins=30,stacked=True,rwidth=1,label=labels)
plt.legend()
#The thing here is that we can automatize the creation of the histogram for every genre
#If we were to add more genres to the dataset this function will still work


# In[33]:


#KDE plor


# In[34]:


movies.info()


# In[35]:


#Adding a grid to the grphs
sns.set_style('whitegrid')


# In[36]:


vis1=sns.lmplot(data=movies, x='CriticRating',y='AudienceRatings',
               fit_reg=False,hue='Genre',size=7,aspect=1)


# In[37]:


vis1=sns.lmplot(data=movies, x='CriticRating',y='AudienceRatings',
               fit_reg=False,size=7,aspect=1)


# In[38]:


k1=sns.kdeplot(movies.CriticRating,movies.AudienceRatings,size=7,shade=True,shade_lowest=False,cmap='Reds')


# In[39]:


k1=sns.kdeplot(movies.CriticRating,movies.AudienceRatings,size=7,shade=True,shade_lowest=False,cmap='Reds')
k1b=sns.kdeplot(movies.CriticRating,movies.AudienceRatings,size=7,cmap='Reds')
#If I run k1 and k1b together I'm going to get the shades of k1 but the outline of k1b. making much better the graph
#This happens because both graphs overlaps each other


# In[40]:


#Subplots


# In[41]:


k2=sns.kdeplot(movies.BudgetMillions,movies.CriticRating)
sns.set_style('dark')


# In[42]:


k3=sns.kdeplot(movies.BudgetMillions,movies.AudienceRatings)


# In[43]:


f, axes=plt.subplots(1,2,figsize=(12,6))
k2=sns.kdeplot(movies.BudgetMillions,movies.CriticRating,ax=axes[0])
k3=sns.kdeplot(movies.BudgetMillions,movies.AudienceRatings,ax=axes[1])
#Function subplot() is not the same as subplots()


# In[44]:


f, axes=plt.subplots(2,2,figsize=(12,6))
k2=sns.kdeplot(movies.BudgetMillions,movies.CriticRating,ax=axes[0,0])
k3=sns.kdeplot(movies.BudgetMillions,movies.AudienceRatings,ax=axes[0,1])
#axes functions like an array of positions. For example: We set the position of k1 in the position [0,0] (first row and column)
#The first two arguments of subplots() indicate the "matrix" of plots. In this case a 2x2 matrix.


# In[45]:


f, axes=plt.subplots(2,2,figsize=(12,6),sharex=True,sharey=True) 
# shares makes all subplots "the same". Meaning that every configuration we make for a single plot in the 
# X coordinates (the xlim for k2) will be applied to every other plot. Same for sharey in Y coordinates
# All this makes things easier to compare.
k2=sns.kdeplot(movies.BudgetMillions,movies.CriticRating,ax=axes[0,0]) 
k3=sns.kdeplot(movies.BudgetMillions,movies.AudienceRatings,ax=axes[0,1])
k2.set(xlim=(-30,200))#This makes k2 to go from -30 to 200 in the X coordinates.


# In[46]:


box=sns.boxplot(data=movies, x='Genre',y='CriticRating')


# In[47]:


violin=sns.violinplot(data=movies,x='Genre',y='CriticRating')


# In[48]:


box2=sns.boxplot(data=movies[movies.Genre=='Drama'], x='Year',y='CriticRating')


# In[49]:


violin=sns.violinplot(data=movies[movies.Genre=='Drama'],x='Year',y='CriticRating')
#The violinplot can show better the concentration of points. 
#The 2011 drama movies have 2 areas where the CriticRating is more present. Wich is difficult to see in a boxplot


# In[50]:


#Facet Grids


# In[51]:


#Preparing the facet grid
g= sns.FacetGrid(movies,row='Genre',col='Year',hue='Genre')


# In[52]:


g= sns.FacetGrid(movies,row='Genre',col='Year',hue='Genre')
g=g.map(plt.scatter,'CriticRating','AudienceRatings')
#We have to execute FacetGrid and map together for this to work.
#When we use map we have to specify the function we want to map in the facet grid


# In[53]:


d= sns.FacetGrid(movies,row='Genre',col='Year',hue='Genre')
d=d.map(plt.hist,'BudgetMillions')


# In[54]:


g= sns.FacetGrid(movies,row='Genre',col='Year',hue='Genre')
kws = dict(s=50,linewidth=0.5,edgecolor='black') #Key words dictionary
g=g.map(plt.scatter,'CriticRating','AudienceRatings',**kws) #Adding the keywords


# In[55]:


#Managing axes and diagonals
g = sns.FacetGrid(movies,row='Genre',col='Year',hue='Genre')
kws = dict(s=50,linewidth=0.5,edgecolor='black')
g=g.map(plt.scatter,'CriticRating','AudienceRatings',**kws)
g.set(xlim=(0,100),ylim=(0,100)) #limit between 0 and 100 for both axes
for ax in g.axes.flat:
    ax.plot((0,100),(0,100),c='gray',ls='--') #here we are making a line that goes from coordinate 0 to 100 in both axes
    #we use the loop to do this line in every element of g (wich are all the scatter plots)


# In[56]:


#with regresion line
g = sns.FacetGrid(movies,row='Genre',col='Year',hue='Genre')
#kws = dict(s=50,linewidth=0.5,edgecolor='black')
g=g.map(sns.regplot,'CriticRating','AudienceRatings')
g.set(xlim=(0,100),ylim=(0,100))
for ax in g.axes.flat:
    ax.plot((0,100),(0,100),c='gray',ls='--')
    
g.add_legend()


# In[57]:


#Dashboards


# In[63]:


sns.set_style('darkgrid')
f,axes = plt.subplots(2,2,figsize=(15,15))
k2=sns.kdeplot(movies.BudgetMillions,movies.CriticRating,ax=axes[0,0])
k3=sns.kdeplot(movies.BudgetMillions,movies.AudienceRatings,ax=axes[0,1])
k4=sns.violinplot(data=movies[movies.Genre=='Drama'],x='Year',y='CriticRating',ax=axes[1,0])
k5=sns.boxplot(data=movies[movies.Genre=='Drama'], x='Year',y='CriticRating',ax=axes[1,1])
k2.set(xlim=(-50,250))
k3.set(xlim=(-50,250))
plt.show()


# In[64]:


#adding plots that are not in seaborn
#like plt.hist(movies.BudgetMillions)
sns.set_style('darkgrid')
f,axes = plt.subplots(2,2,figsize=(15,15))
k2=sns.kdeplot(movies.BudgetMillions,movies.CriticRating,ax=axes[0,0])
k3=sns.kdeplot(movies.BudgetMillions,movies.AudienceRatings,ax=axes[0,1])
k4=sns.violinplot(data=movies[movies.Genre=='Drama'],x='Year',y='CriticRating',ax=axes[1,0])
#k5=sns.boxplot(data=movies[movies.Genre=='Drama'], x='Year',y='CriticRating',ax=axes[1,1])
#In this case we need to specify the axes before the plot
axes[1,1].hist(movies.BudgetMillions)
k2.set(xlim=(-50,250))
k3.set(xlim=(-50,250))
plt.show()


# In[76]:


sns.set_style('darkgrid')
f,axes = plt.subplots(2,2,figsize=(15,15))

k2=sns.kdeplot(movies.BudgetMillions,movies.CriticRating,shade=True,shade_lowest=True,cmap='inferno',ax=axes[0,0])
k2b=sns.kdeplot(movies.BudgetMillions,movies.CriticRating,cmap='inferno',ax=axes[0,0])

k3=sns.kdeplot(movies.BudgetMillions,movies.AudienceRatings,shade=True,shade_lowest=True,cmap='inferno',ax=axes[0,1])
k3b=sns.kdeplot(movies.BudgetMillions,movies.AudienceRatings,cmap='inferno',ax=axes[0,1])

k4=sns.violinplot(data=movies[movies.Genre=='Drama'],x='Year',y='CriticRating',ax=axes[1,0])

k5=sns.boxplot(data=movies[movies.Genre=='Drama'], x='Year',y='CriticRating',ax=axes[1,1])

k2.set(xlim=(-50,250))
k3.set(xlim=(-50,250))
plt.show()


# In[86]:


#we can also change the background of plots 1,0 and 1,1
#with 'axes.facecolor':'black' we override the dark or white of the default background color for black in this case
sns.set_style('dark', {'axes.facecolor':'black'})
f,axes = plt.subplots(2,2,figsize=(15,15))

k2=sns.kdeplot(movies.BudgetMillions,movies.CriticRating,shade=True,shade_lowest=True,cmap='inferno',ax=axes[0,0])
k2b=sns.kdeplot(movies.BudgetMillions,movies.CriticRating,cmap='inferno',ax=axes[0,0])

k3=sns.kdeplot(movies.BudgetMillions,movies.AudienceRatings,shade=True,shade_lowest=True,cmap='inferno',ax=axes[0,1])
k3b=sns.kdeplot(movies.BudgetMillions,movies.AudienceRatings,cmap='inferno',ax=axes[0,1])

k4=sns.violinplot(data=movies,x='Year',y='BudgetMillions',palette='YlOrRd',ax=axes[1,0])

k5=sns.boxplot(data=movies, x='Year',y='BudgetMillions',palette='YlOrRd',ax=axes[1,1])

k2.set(xlim=(-50,250))
k3.set(xlim=(-50,250))
plt.show()


# ---

# In[99]:


list=[]
labels=[]
for gen in movies.Genre.cat.categories:
    list.append(movies[movies.Genre == gen].BudgetMillions)
    labels.append(gen)
sns.set_style('whitegrid')
fig,ax=plt.subplots()
fig.set_size_inches(11.7,8.27) #A4 paper size
h=plt.hist(list,bins=30,stacked=True,rwidth=1,label=labels)
plt.title('Movie Budget Distribution',fontsize=35,color='DarkBlue',fontname='Times New Roman') #adding a title
plt.ylabel('Number of movies',fontsize=25) #label for axes
plt.xlabel('Budget of movies',fontsize=25)
plt.yticks(fontsize=20) #size of the ticks
plt.xticks(fontsize=20)
plt.legend(frameon=True,fancybox=True,shadow=True,framealpha=1,prop={'size':20})#A bigger legend
plt.show()


# In[ ]:




