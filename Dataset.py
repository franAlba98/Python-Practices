#!/usr/bin/env python
# coding: utf-8

# In[102]:


import pandas as pd


# In[103]:


#method 1: Specify Full path to file


# In[104]:


#Windows:
stats = pd.read_csv('C:\\Users\\Francisco\\Desktop\\PYTHON\\P4-Demographic-Data.csv')


# In[105]:


stats


# In[106]:


#Method 2: Change working directory
import os


# In[107]:


print(os.getcwd())


# In[108]:


#Windows:
os.chdir('C:\\Users\\Francisco\\Desktop')


# In[109]:


print(os.getcwd())


# In[110]:


stats2= pd.read_csv('.\\PYTHON\\P4-Demographic-Data.csv')


# In[111]:


stats2


# In[112]:


#Exploring the data


# In[113]:


#1: Full dataframe
stats


# In[114]:


#2: number of rows
len(stats) #195 rows imported


# In[115]:


#3: columns
stats.columns


# In[116]:


#4: number of columns
len(stats.columns)


# In[117]:


#5: top rows
stats.head(6) #First 6


# In[118]:


#6: bottom rows
stats.tail(6)


# In[119]:


#7: info on columns
stats.info() #like str sunction in R


# In[120]:


#8: stats on the columns
stats.describe() #like summary in R


# In[121]:


stats.describe().transpose()


# In[122]:


#Renaming columns
stats.columns


# In[123]:


stats.columns = ['a','b','c','d','e']


# In[124]:


stats


# In[125]:


stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers',
       'IncomeGroup']


# In[126]:


stats.head()


# In[127]:


###Subsetting dataframes


# In[128]:


stats[21:26]


# In[129]:


stats[:]


# In[130]:


stats[23:]


# In[131]:


stats[:10]


# In[132]:


stats[::-1]


# In[133]:


stats[::20]


# In[134]:


#columns


# In[135]:


stats.columns


# In[136]:


stats['CountryName']


# In[137]:


stats['CountryName'].head()


# In[138]:


['CountryName','BirthRate']


# In[139]:


stats[['CountryName','BirthRate']].head()


# In[140]:


stats[['BirthRate','CountryName']].head()


# In[141]:


stats.BirthRate


# In[142]:


stats[4:8][['BirthRate','CountryName']]#[Row]/[Collumns]


# In[143]:


df2=stats[['BirthRate','CountryName']]
print(df2)


# In[144]:


df2[4:9]


# In[145]:


#Operations


# In[146]:


result= stats.BirthRate * stats.InternetUsers


# In[147]:


result.head()


# In[148]:


#Add columns


# In[149]:


stats['MyCalc'] = result


# In[150]:


stats.head()


# In[151]:


#Comparison to R
stats['xyz'] = [1,2,3,4,5] #Error because Python does not recycle values


# In[152]:


#Remove a col


# In[153]:


stats.drop('MyCalc',1) #RETURN A NEW OBJECT


# In[154]:


stats=stats.drop('MyCalc',1)


# In[155]:


stats.head()


# In[156]:


#FILTERING


# In[157]:


stats.head()


# In[158]:


stats.InternetUsers < 2
print(stats.InternetUsers < 2)


# In[159]:


Filter = stats.InternetUsers < 2
stats[Filter] #Same with R


# In[160]:


Filter2 = stats.BirthRate > 40


# In[161]:


stats[Filter2]


# In[162]:


stats[stats.BirthRate > 40 and stats.InternetUsers < 2]
#Python not being a vectorized language makes this AND to work with only one value of truth on each side, not with multiple ones.


# In[163]:


#For vector we need to use the '&'
Filter & Filter2


# In[164]:


stats[Filter & Filter2]


# In[165]:


stats[(stats.BirthRate > 40) & (stats.InternetUsers < 2)] #The () is to specify the order of operations
#All of this is realy similar to R


# In[166]:


stats[stats.IncomeGroup == 'High income']


# In[167]:


#How to get categories
stats.IncomeGroup.unique()


# In[168]:


stats[stats.CountryName == 'Malta']


# In[169]:


#Individual elements


# In[170]:


#.at  #for labels
#.iat #for integer location


# In[171]:


stats.iat[3,4] #3rd row - 4th column


# In[172]:


stats.iat[0,1]


# In[173]:


stats.at[3,'BirthRate']


# In[174]:


#Seaborn


# In[175]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = 8,4
import warnings
warnings.filterwarnings('ignore')


# In[176]:


#Distribution


# In[185]:


stats.head()


# In[186]:


vis1=sns.distplot(stats.InternetUsers)


# In[187]:


vis1=sns.distplot(stats.InternetUsers,30)


# In[188]:


#boxplot
vis2= sns.boxenplot(data=stats,x='IncomeGroup',y='BirthRate')


# In[189]:


vis3= sns.lmplot(data=stats,x='InternetUsers', y='BirthRate',fit_reg=False)


# In[190]:


vis3= sns.lmplot(data=stats,x='InternetUsers', y='BirthRate',fit_reg=False,hue='IncomeGroup',size=10,aspect=2)


# In[191]:


#Keyword arguments in python


# In[198]:


#marker size
vis3= sns.lmplot(data=stats,x='InternetUsers', y='BirthRate',fit_reg=False,hue='IncomeGroup',size=10,aspect=2,
                #Here scatter_kws is expecting a dictionary. The thing is that we can use de dictionary 
                #to use arguments of pyplot wich are not present in lmplot
                scatter_kws={'s':200}
                )


# In[ ]:




