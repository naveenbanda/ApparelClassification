
# coding: utf-8

# In[28]:

from shutil import copy2


# In[37]:

address=[]
with open('fashion-data/train.txt','r') as f:
    for i in f:
        address.append(i[:-1])
f.close()
train_size=len(address)
print (train_size)


# In[ ]:




# In[ ]:




# In[ ]:




# In[39]:

count=1
for i in address:
    src="fashion-data/images/"+i+".jpg"
    folder=i.split("/")
    #print (str(folder[0]))
    dst="dataset/training_set/"+str(folder[0])+"/"+str(count)+".jpg"
    copy2(src,dst)
    if (count%50==0 or count==train_size):
        print (str(count)+" Done")
    count+=1
    


# In[40]:

print(count)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[44]:

test_address=[]
with open('fashion-data/test.txt','r') as f:
    for i in f:
        test_address.append(i[:-1])
f.close()
test_size=len(test_address)
print (test_size)


# In[ ]:




# In[ ]:




# In[48]:

count=1
for i in test_address:
    src="fashion-data/images/"+i+".jpg"
    folder=i.split("/")
    dst="dataset/test_set/"+str(folder[0])+"/"+str(count)+".jpg"
    copy2(src,dst)
    if (count%50==0 or count==test_size):
        print (str(count)+" Done")
    count+=1
    


# In[49]:

print (count)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



