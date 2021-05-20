#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. What does an empty dictionary's code look like?
#Solu:
dictEmpty={}
print(len(dictEmpty))


# In[16]:


#2. What is the value of a dictionary value with the key 'foo' and the value 42?
#Solu:
# Creating a Dictionary
DictF = {'foo': '42'}
print("\nDictionary used to call the value: ")
print(DictF['foo'])


# #3. What is the most significant distinction between a dictionary and a list?
# #solu
# List is based on indexing but a dictionary is based on key -value pairs.
# The retreival of data from a list happens based on the index values but in dictionary we can retreive the data based on the key value combination.
# 

# In[19]:


#4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

#Solu
#It gives a keyError because the key is not present in the dictionary .
spam={'bar':100}
#spam['foo']
#correct way to get the value 100 would be by calling the keyword bar like shown below.
spam['bar']


# In[35]:


#5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
spam={'cat':1234}
#spam={'1234':cat}
x= 'cat'
if(x in spam):
    print("true")
else:
    print("False")
    
#No Difference between the expressions because compiler check whether cat is in key pairs or not for both the expressions
#because the compiler ultimately checks the cat in key only as it is retrieved only through key pairs .


# In[40]:


#6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
spam={'A': 'cat'}
x='cat'
if(x in spam.values()):
    print("True")
else:
    print("False")
#In this condition it returns true when we check for the value in spam.values()
#but returns false when we check for the cat in spam because it holds the access through key pairs by default.


# In[51]:


#7. What is a shortcut for the following code?
spam={}
x='color'
if 'color' not in spam:
    spam['color'] = 'black'

#Alternative shortcut.,
spam={}
spam['color']='black' if('color'  not in spam) else print("It is in spam")
spam


# 8. How do you "pretty print" dictionary values using which module and function?
# Solu:
# step-1 Module:
# import pprint
# It is a module used to prettify the dictionary values .
# Step-2 function:
# pprint.pprint() is a function used to do "pretty print" dictionary values.

# In[ ]:




