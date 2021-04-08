#!/usr/bin/env python
# coding: utf-8

# In[1]:


#----- -2 ------ -1 ---- 0 ---- 1 ----- 2 -----


# In[3]:


import numpy as np
from numpy.random import randn


# In[16]:


randn() #generates a random number


# In[32]:


#----- -2 ------ -1 ---- 0 ---- 1 ----- 2 -----
answer = None
x = randn()
if x > 1:
    answer = 'greater'
print(x)
print(answer)


# In[39]:


#----- -2 ------ -1 ---- 0 ---- 1 ----- 2 -----
answer = None
x = randn()
if x > 1:
    answer = 'greater than 1'
else:
    answer = 'less than 1'
print(x)
print(answer)


# In[49]:


#----- -2 ------ -1 ---- 0 ---- 1 ----- 2 -----
#nested statements
answer = None
x = randn()
if x > 1:
    answer = 'greater than 1'
else:
    if x>=-1:
        answer = 'betweeen -1 and 1'
    else:
        answer = 'less than 1'
print(x)
print(answer)


# In[55]:


#----- -2 ------ -1 ---- 0 ---- 1 ----- 2 -----
#chained statements
answer = None
x = randn()
if x > 1:
    answer = 'greater than 1'
elif x>=-1:
    answer = 'betweeen -1 and 1'
else:
    answer = 'less than 1'
print(x)
print(answer)


# In[61]:


#----- -2 ------ -1 ---- 0 ---- 1 ----- 2 -----
#chained statements
answer = None
x = randn()
if x > 1:
    answer = 'greater than 1'
elif x>=-1:
    answer = 'betweeen -1 and 1'
else:
    answer = 'less than 1'
    print('hello')
print(x)
print(answer)


# In[64]:


#----- -2 ------ -1 ---- 0 ---- 1 ----- 2 -----
#chained statements
answer = None
n = 0
j = 0
while n != 10000: 
    x = randn()
    if x > 1:
        answer = 'greater than 1'
    elif x>=-1:
        answer = 'betweeen -1 and 1'
        n = n + 1
    else:
        answer = 'less than 1'
    j=j+1
    print(x)
    print(answer)
    print('n: ',n)
    print('j: ',j)
    print('Answer: ',n/j)

