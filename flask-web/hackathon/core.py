#!/usr/bin/env python
# coding: utf-8

# In[61]:


import glob

#read txt files
txt_list = glob.glob("./hackathon/*.txt")


# In[62]:


search_list = []
for curr_file in txt_list:
    with open(curr_file) as f:
        lines = f.read().replace('\n', '')
        search_list.append(lines)


# In[63]:


def searchTextInFiles(search_keywords):
    
    success_list = []
    cntr = 0
    
    for curr_file in search_list:
        fileFlag = True
        for curr_keyword in search_keywords:
            if curr_keyword in curr_file:
                pass
            else:
                fileFlag = False
                break
        if fileFlag:
            success_list.append(txt_list[cntr].replace('.txt', ''))
            
        cntr += 1
        
    return success_list


# In[64]:


search_keywords = ['detecting', 'detect']
print(searchTextInFiles(search_keywords))


# In[ ]:




