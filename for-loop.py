#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##python for loop


# In[ ]:


##print square of numbers between 1 to 5


# In[2]:


for i in range(1,6):
    print(i*i,end=' ')
 


# In[ ]:


##print square of numbers between 1 to 5 skipping the even numbers using continue function


# In[10]:


for i in range(1,6):
    if i% 2 == 0:
     continue
    print(i*i,end=' ')


# In[ ]:


##break funtion in for loop
##question. find the lost key location.


# In[22]:


key_location='chair'
locations=['living room','bedroom','kitchen','chair','almirah']
for i in locations:
    if i==key_location:
            print("key is found in",i)
            break
    else:
        print("key is not found in",i)
            
            


# In[ ]:




