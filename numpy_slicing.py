#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
a = np.array([6,7,8])
a [0:2]


# In[2]:


a[-1]


# In[8]:


a = np.array([[6,7,8],[1,2,3],[9,3,2]])
a


# In[9]:


a[1,2]


# In[10]:


a[0:2,2]


# In[15]:


a[-1]


# In[12]:


a[1]


# In[17]:


a[-1,0:2]


# In[23]:


a[:,1:3]


# In[24]:


a = np.array([[6,7,8],[1,2,3],[9,3,2]])
a


# In[27]:


for row in a :
    print(row)


# In[28]:


for cell in a.flat:
    print(cell)


# In[37]:


a = np.arange(6).reshape(3,2)
b = np.arange(6,12).reshape(3,2)


# In[41]:


a


# In[40]:


b


# In[42]:


np.vstack((a,b))


# In[43]:


np.hstack((a,b))


# In[44]:


a = np.arange(30).reshape(2,15)


# In[45]:


a


# In[46]:


np.hsplit(a,3)


# In[50]:


result= np.hsplit(a,3)


# In[51]:


result[1]


# In[58]:


result= np.vsplit(a,2)
result[0]


# In[60]:


a = np.arange(12).reshape(3,4)


# In[61]:


a


# In[62]:


b = a>4
b


# In[63]:


a[b]


# In[64]:


a[b]= -1


# In[65]:


a


# In[ ]:





# In[ ]:




