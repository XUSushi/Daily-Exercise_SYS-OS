
# coding: utf-8

# In[1]:

#导入sys模块
import sys


# In[2]:

#使用它做参数传递比较多


# In[3]:

sys.argv


# In[4]:

sys.version


# In[5]:

sys.path


# In[6]:

sys.platform


# In[7]:

import os


# In[8]:

os.system('dir')


# In[9]:

str1=os.popen('dir')  #\n在python里不会处理为换行


# In[10]:

str1.read()


# In[11]:

out=str1.read().split('\n')


# In[12]:

out


# In[13]:

for in in out:
    if 'VirtualBox' in i:
        print i[0:16]


# In[14]:

help(os.path.exists('chinese_eg.txt'))


# In[15]:

os.path.exists('C:/Users/chinese_eg.txt')


# In[16]:

os.mkdir("xinjian") #在用户的文档下面


# In[17]:

os.linesep


# In[18]:

os.path.basename('C:/Users/chinese_eg.txt')




