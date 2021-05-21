#!/usr/bin/env python
# coding: utf-8

# 1. What are escape characters, and how do you use them?
# Solu: 
# Escape characters are reserved characters which are used by backslash \ followed by alphabets to perform particular action which will inform python compiler to use those statements as plain text and a comment which doesn't have any affect on the code for its execution.
# Uses:
# \b-backspace character 
# \n-newline character 
# \t-tab character 
# \v-vertical tab character  
# \"-double quote character 
# \'-single quote character 
# \\-backslash character 

# 2. What do the escape characters n and t stand for?
# Solu:
# \n is escape character which stands for newline character 
# \t is escape characte which stands for tab character 

# In[2]:


#3. What is the way to include backslash characters in a string?
#solu:
#Backslash can be a combination of other alphabets or a backslash itself to perform a task.
#A way to include a backslash characters in a string is as shown in the example below:
print("My name is Tom\") #it throws an error because a single \is a escape character 
print("My name is jerry\\") #it is a correct format of using a backslash.


# In[11]:


#4. The string "Howl's Moving Castle" is a correct value.
#Why isn't the single quote character in the word Howl's not escaped a problem?

print("Howl's Moving Castle")#works as expected
print('Howl\'s Moving Castle')  #works with escape character inclusion
#print('Howl's Moving Castle') #throws error

#because the whole string is in double quotations which is encapsulated. 
#Incase if the double quotations are replaced by single quotations then we need to use escape characters to print the exact 
#string again.


# 5. How do you write a string of newlines if you don't want to use the n character?
# Solu:
# we can write a string of newlines without using the \n character by making use of built in end='<character >' property in print() function of python.

# In[21]:


#6. What are the values of the given expressions?
'Hello, world!'[1]
'Hello, world!'[0:5]
'Hello, world!'[:5]
'Hello, world!'[3:]
 #Solu:
#'Hello, world!'[1]---e
#'Hello, world!'[0:5]--Hello
#'Hello, world!'[:5]--Hello
#'Hello, world!'[3:]--lo,world!


# In[ ]:


#7. What are the values of the following expressions?
'Hello'.upper()
'Hello'.upper().isupper()
'Hello'.upper().lower()
#solu:
#'Hello'.upper()--HELLO
#'Hello'.upper().isupper()--True
#'Hello'.upper().lower()--hello


# In[26]:


#8. What are the values of the following expressions?
'Remember, remember, the fifth of July.'.split()
'-'.join('There can only one.'.split())
#Solu:
'Remember, remember, the fifth of July.'.split() #It splits the string by using space as delimiter and forms a list using by it.
#output: ['Remember,', 'remember,', 'the', 'fifth', 'of', 'July.']
'-'.join('There can only one.'.split())
#output:'There-can-only-one.'


# 9. What are the methods for right-justifying, left-justifying, and centering a string?
# Solu:
# 
# These functions respectively left-justify, right-justify and center a string in a field of given width. They return a string that is at least width characters wide, created by padding the string s with the character fillchar (default is a space) until the given width on the right, left or both sides. The string is never truncated.
# for example center().,
# 
# csr= "i love ineuron"
# print (csr.center(40, '#'))
# output: #############i love ineuron#############
# 

# 10. What is the best way to remove whitespace characters from the start or end?
# Solu:
# By using the trim() function we can remove the whitecharacters from a string completely. trimleft() and trimright() are used to remove white characters from start and end .

# In[ ]:





# In[ ]:




