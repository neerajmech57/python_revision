#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


raw_csv_data=pd.read_csv("Absenteeism-data.csv")


# In[3]:


df=raw_csv_data.copy()


# In[5]:


df.head()


# In[6]:


pd.options.display.max_columns = None
pd.options.display.max_rows = None


# In[7]:


df


# In[8]:


df.info()


# Removing ID column 

# In[9]:


df=df.drop(['ID' ],axis=1)


# In[10]:


df


# REASON FOR ABSENCE(DUMMY VARIABLES)

# In[11]:


df['Reason for Absence']


# In[12]:


len(df['Reason for Absence'])


# In[13]:


df['Reason for Absence'].unique()


# In[15]:


reasons_columns=pd.get_dummies(df['Reason for Absence'],drop_first=True)
reasons_columns


# DROPPING REASON FOR ABSENCE COLUMN USING .DROP METHOD

# In[20]:


df=df.drop(['Reason for Absence'],axis=1)


# In[21]:


df


# In[18]:


reason_type1=reasons_columns.loc[:,1:14].max(axis=1)
reason_type2=reasons_columns.loc[:,15:17].max(axis=1)
reason_type3=reasons_columns.loc[:,18:21].max(axis=1)
reason_type4=reasons_columns.loc[:,22:28].max(axis=1)


# ##Concatenate Column Values

# In[22]:


df=pd.concat([df,reason_type1,reason_type2,reason_type3,reason_type4],axis=1)


# In[23]:


df


# In[25]:


df.columns.values


# In[30]:


columns_names=['Date', 'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education',
       'Children', 'Pets', 'Absenteeism Time in Hours','Reason1','Reason2','Reason3','Reason4']
df.columns=columns_names


# In[31]:


df


# reorder the columns shifting reason for absence on left side of dataframe

# In[32]:


column_reordered=['Reason1','Reason2','Reason3','Reason4','Date', 'Transportation Expense', 'Distance to Work', 'Age',
       'Daily Work Load Average', 'Body Mass Index', 'Education',
       'Children', 'Pets', 'Absenteeism Time in Hours']


# In[33]:


df=df[column_reordered]


# In[34]:


df


# WORKING ON DATES

# In[38]:


##creating a check point
df_Reason_mod=df.copy()


# In[39]:


type(df_Reason_mod['Date'][0])


# note date format is STR , we would change type to timestamp

# In[50]:


df_Reason_mod['Date']=pd.to_datetime(df_Reason_mod['Date'])


# In[51]:


df_Reason_mod['Date']


# In[42]:


type(df_Reason_mod['Date'][0])


# In[52]:


df_Reason_mod['Date']=pd.to_datetime(df_Reason_mod['Date'],format='%d/%m/%Y')


# In[54]:


df_Reason_mod['Date'][0]


# EXTRACT MONTH AND WEEKDAY VALUE AND MAKE TWO DIFFERENT COLUMN

# In[55]:


df_Reason_mod['Date'][0].month


# In[56]:


list_month=[]
list_month


# In[58]:


df_Reason_mod.shape[0]


# In[62]:


for i in range(df_Reason_mod.shape[0]):
    list_month.append(df_Reason_mod['Date'][i].month)
    


# In[63]:


list_month


# In[64]:


len(list_month)


# In[66]:


df_Reason_mod['Month_Value']=list_month


# In[67]:


df_Reason_mod.head()


# In[74]:


df_Reason_mod['Date'][0].weekday()


# In[83]:


list_weekday=[]


# In[84]:


for i in range(df_Reason_mod.shape[0]):
    list_weekday.append(df_Reason_mod['Date'][i].weekday())
    


# In[85]:


list_weekday


# In[86]:


type(list_weekday)


# In[87]:


len(list_weekday)


# In[88]:


df_Reason_mod['Day of the Week']=list_weekday


# In[89]:


df_Reason_mod.head()


# In[90]:


df_Reason_mod=df_Reason_mod.drop(['Date'],axis=1)


# In[91]:


df_Reason_mod


# EDUCATION COLUMN

# In[92]:


df_Reason_mod['Education']


# In[96]:


df_Reason_mod['Education'].value_counts()


# In[97]:


df_Reason_mod['Education']=df_Reason_mod['Education'].map({1:0,2:1,3:1,4:1})


# In[98]:


df_Reason_mod['Education'].value_counts()


# In[99]:


df_mech_cleaned=df_Reason_mod.copy()


# In[100]:


df_mech_cleaned


# In[ ]:




