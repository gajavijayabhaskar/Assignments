#!/usr/bin/env python
# coding: utf-8

# 1. Is the Python Standard Library included with PyInputPlus?
# Solu:
# no, PyInputPlus is usually not included in the Python Standard Library we have install it manually.
# using >pip install PyInputPlus from anaconda prompt or any commandline

# 2. Why is PyInputPlus commonly imported with import pyinputplus as pypi?
# Solu:
# pypi is a alias name used to reduce the length of code while importing the module.
# Another reason for it is that the PyInputPlus is one of the many softwares present in the repository called pypi. "pypi" full form is Python package index.

# 3. How do you distinguish between inputInt() and inputFloat()?   

# inputInt() : function which accepts integer values with parameters like ‘min’, ‘max’, ‘greaterThan’ and ‘lessThan’  for bounds which returns the output in integer
# inputFloat() : function which accepts a floating-point numeric value with parameters like ‘min’, ‘max’, ‘greaterThan’ and ‘lessThan’  parameters which returns the output in float.

# In[8]:


#inputInt() only gives integer value even though you have inserted a float value it will convert internally to integer.
import pyinputplus as pypi
inp = pypi.inputInt("Enter integer only: ")
print(inp, type(inp))
num=5.0
print("Without using pypi :",type(num))


# In[9]:


#inputFloat() only gives float value even though you have inserted a integer value it will convert internally to float.
import pyinputplus as pypi
Anumber=pypi.inputFloat("Enter float value only:")
print(Anumber)
print(type(Anumber))


# 4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?

# In[10]:


#Solu:
Entr=pypi.inputInt(prompt="Enter a number: ",greaterThan=0,lessThan=99)


# 5. What is transferred to the keyword arguments allowRegexes and blockRegexes?
# solu:
# As the name suggests allowRegexes are used to accept the regex pattern as an input . Similarly, blockRegexes doesn't accept the input the regex pattern is in the form of blockRegexes. 
# For example.,

# In[13]:


# allowRegexes accepts the number in the pattern
phoneNumber = pypi.inputNum("Enter phone no: ",allowRegexes=r"^([+]91)-(\d\d\d\d\d)-(\d\d\d\d\d)$")
print(f"Entered Phone number is {phoneNumber}")


# In[15]:


#blockRegexes, blocks if sapce is available in the input
phoneNumber = pypi.inputNum("Enter phone without ' ' :",blockRegexes=r" ")
print("Entered Phone number: ",phoneNumber)


# 6. If a blank input is entered three times, what does inputStr(limit=3) do?
# Solu: 
# when limit is 3, for the first 2 inputs it will show a warning message "Blank values are not allowed", each time we input a blank value. The next time we enter a blank value, it raises a "ValidationException: Blank values are not allowed."
# warnings as below:
# 1.ValidationException: Blank values are not allowed.
# 2.RetryLimitException:

# In[16]:


inputs = pypi.inputStr(limit=3)
print(inputs)


# 7. If blank input is entered three times, what does inputStr(limit=3, default='hello') do?
# Solu: Since the limit is 3,for the first 2 inputs it will show a warning message "Blank values are not allowed". After the third blank hit it will return a default value which is 'hello' in this case along with warning message.
