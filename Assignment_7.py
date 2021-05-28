#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1. What is the name of the feature responsible for generating Regex objects?
#solu:re.compile("") is responsible for generatig Regex Objects

import re
path=re.compile("")
(path)#Regex Object


# In[3]:


#2. Why do raw strings often appear in Regex objects?
#solu:
#A Normal common string can be involved with escape characters but a raw string can be used to avoid the utility of escape
#characters and produce a raw string present in between (r"") clause. 
#for example.,
stringdummy="I am learning, \n artificial intelligence"
Rawstring=r"I am learning, \n artificial intelligence"
print(stringdummy)
#output:I am learning, 
 #artificial intelligence
print(Rawstring)
#output:I am learning, \n artificial intelligence


# In[8]:


#3. What is the return value of the search() method?
#solu:
#It returns the match object.
string = "Hey, world!"
matchstring = (re.search(r".* ", string))
type(matchstring)


# In[9]:


#4. From a Match item, how do you get the actual strings that match the pattern?
#solu
m = re.match(r".* ", s)
m # Match object


# In[10]:


m.group()


# In[17]:


#5. In the regex which created from the r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group zero cover? Group 2? Group 1?
s = "Hello 9183-090-4575"
pattern = r"(\d\d\d\d)-(\d\d\d-\d\d\d\d)"
m = re.search(pattern,s)


# In[19]:



# group(0)
print("group(0) gives all the numbers in the string:",m.group(0))

# group(1)
print("group(1) gives all the numbers present in the first parenthesis:",m.group(1))

# group(2)
print("group(2) gives all the numbers present in the second parenthesis:",m.group(2))


# In[19]:


#6. In standard expression syntax, parentheses and intervals have distinct meanings.
#How can you tell a regex that you want it to fit real parentheses and periods?
#solu:

# For example., we can tell a regex fit in real parenthese and periods by using \( , \) and \. before them .
import re 
s1 = "Assignments are not (getting). difficult."
pattern1 = r"\(.*\)\."
re.findall(pattern1, s1)


# In[18]:


#another method .,we can tell a regex fit in real parenthese and periods by using enclosing characters  in [(],[)] and [.] 
s2 = "It is taking time but will (complete). them"
pattern2 = r"[(].*[).]"
re.findall(pattern2, s2)


# 7. The findall() method returns a string list or a list of string tuples. What causes it to return one of the two options?
# Solu:
# string list => findall() method will return a list of strings when the regex expression doesn't contain any group(within paranthesis()). For e.g. r"\d\d\d-\d\d\d\d-\d\d\d\d\d"
# 
# string tuples => findall() method will return a list of string tuples if the regex expression contains groups, enclosed in (). For e.g. r"(\d\d\d)-(\d\d\d\d)-(\d\d\d\d\d)"

# In[32]:


s = "830-9045-75454 and 536-8954-75214"
pattern1 = r"\d\d\d-\d\d\d\d-\d\d\d\d\d" # regex pattern without any group
pattern2 = r"(\d\d\d)-(\d\d\d\d)-(\d\d\d\d\d)" # regex expression with 3 groups
pattern3 = r"(\d\d\d-\d\d\d\d)-(\d\d\d\d\d)" # regex expression with 2 groups

print(f"{pattern1}:", re.findall(pattern1, s))
print(f"{pattern2}:", re.findall(pattern2, s))
print(f"{pattern3}:", re.findall(pattern3, s))


# 8. In standard expressions, what does the | character mean?
# solu:
# | expression means either | or . which means regex has to match anyone of the expressions written with| symbol on both sides.

# In[36]:


sregx = "aaa bbbb ccc"
pattern = r"aaaa|bbbb|cccc"
re.findall(pattern, sregx)


# 9. In regular expressions, what does the character ? stand for?
# Solu:
# ? character means to either:
# 
# a) Match 0 or 1 group written just before ? in the regex expression
# 
# b) Signify nongreedy matching. In nongreedy matching, the regex engine matches as few characters as possible, just enough to match pattern in the given string, i.e. the shortest possible match from a given position in the string.
# 
# Different non-greedy quantifiers are: ??, *?, {m,n}?, +?
# 

# In[39]:


# Match 0 or 1 group

s = "vvvv"
pattern = r"v?"

re.findall(pattern, s)


# In[41]:


# Greedy match
s = "gggg"
pattern = r"g*"
print("Greedy match:",re.findall(pattern, s))


# Non-Greedy match

s = "gggg"
pattern = r"g*?"
print("NonGreedy match",re.findall(pattern, s))


# In[45]:


print("Greedy match:",re.findall('g?', 'ggggg'))

print("NonGreedy match:",re.findall('v??', 'vvvv'))


# 10.In regular expressions, what is the difference between the + and * characters?
# 
# 
# + => + is a metacharacter which means to match 1 or more occurences of the preceeding groups.
# 
# * => * is a metacharacter which matches 0 or more occurences of the preceeding groups. For 0 occurence at any position, an empty string ' ' is returned, otherwise the matched string is returned
# 

# In[48]:


s = "vijayaa"
pattern1 = r"a*"
pattern2 = r"a+"

print('r"a*" =>',re.findall(pattern1, s))
print('r"a+" =>',re.findall(pattern2, s))


# 11. What is the difference between {4} and {4,5} in regular expression?
# 
# {4} ==> It means search for the matches with exactly 4 continuous occurences of the preceeding group
# 
# {4,5} ==> It means search for the matches with the continuous occurings between 4 and 5, including 5, of the preceeding group

# In[53]:


s = "aaaa cccc bbbbb aaaaa"
pattern1 = r"a{4}"
pattern2 = r"a{4,5}"

print(f"{pattern1}:", re.findall(pattern1, s))
print(f"{pattern2}:", re.findall(pattern2, s))


# 12. What do you mean by the \d, \w, and \s shorthand character classes signify in regular expressions?

# In[2]:


import re
MyDet = "My Mobile number is @8309045754"

patternA = r"\d" 
patternB = r"\w"
patternC = r"\s"

print(f"{pattern1} = {re.findall(patternA, MyDet)}")#it only matches the digits between[0-9]
print(f"{pattern2} = {re.findall(patternB, MyDet)}")#it accepts only the alphabets from [a-zA-Z0-9]
print(f"{pattern3} = {re.findall(patternC, MyDet)}")#it only matches the no. of white spaces present in the string provided.


# 13. What do means by \D, \W, and \S shorthand character classes signify in regular expressions?

# In[3]:


import re
MyDet = "My Mobile number is @8309045754"

patternA = r"\D" 
patternB = r"\W"
patternC = r"\S"

print(f"{pattern1} = {re.findall(patternA, MyDet)}")#it's exactly opposite to \d[0-9],it matches everything other than digits
print(f"{pattern2} = {re.findall(patternB, MyDet)}")#it can be said as  [^a-zA-Z0-9] which acts opposite to \w regex 
print(f"{pattern3} = {re.findall(patternC, MyDet)}")#it takes everything other than spaces. similarly opposite to \s.


# 14. What is the difference between .? and .*?

# In[6]:


import re
strng = "vijay"
pattern1 = r".*"
pattern2 = r".*?"
#Based on greedy search, it'll return a complete string and a blank string in list
print(pattern1,":",re.findall(pattern1, strng))
#Based on non-greedy search , it'll return a emptyy string in placess to a single character of string.
print(pattern2,":",re.findall(pattern2,strng))


# 15. What is the syntax for matching both numbers and lowercase letters with a character class?

# In[16]:


import re
Samplestring="BE a datascientist by @ 2022"

PatternA=r"[a-z0-9]"
PatternB=r"[0-9a-z]"
print(f"{PatternA}"+":",re.findall(PatternA,Samplestring))
print(f"{PatternB}"+":",re.findall(PatternB,Samplestring))


# 16. What is the procedure for making a normal expression in regax case insensitive?
# Solu: By making use of ignorecase in the findall or search method normal expression in regex case insensitive is achievable.

# In[20]:


import re 
s = "vIJay BhaSKar"
pattern = "Bhaskar"

print(re.findall(pattern, s, re.IGNORECASE))
print(re.findall(pattern, s, re.I))


# 17. What does the . character normally match? What does it match if re.DOTALL is passed as 2nd argument in re.compile()?
# solu:
# . character normally matches any type of character except the \n character in the string.
# On passing re.DOTALL as the 2nd arguement of re.findall, the dot will also match the \n character
# for example.,

# In[26]:


import re
 
string="""Hey Ineuron,team 
"""
pattern="."

print("By using re.DOTALL",re.findall(pattern,string,re.DOTALL))
print("Not using re.DOTALL",re.findall(pattern,string))


# 18. If numReg = re.compile(r'\d+'), what will numRegex.sub('X', '11 drummers, 10 pipers, five rings, 4 hen') return?
# solu:
# The digits are replaced with X.

# In[29]:


numRegex = re.compile(r'\d+')
numRegex.sub('X', '11 drummers, 10 pipers, five rings, 4 hen')


# 19. What does passing re.VERBOSE as the 2nd argument to re.compile() allow to do?
# Solu:
# With re.VERBOSE arguement, it is helpful in making the expression prettier ,readable .
# sections separated apart are helpful in understanding regex pattern better.
# It is allowed for usage of comments in between the regular expressions.
# whitespaces with in the pattern is ignored except in some cases like.,
# 1) used in a character class, or
# 2) When white space is preceded by an unescaped backslash(/ ), or with the tokens like *?, (?: or (?P

# In[39]:


# Python3 program to show the Implementation of VERBOSE in RegEX
import re

def validate_PersonAdd(address):
    regex_address=re.compile(r"""
                            ^([a-zA-Z]+)				 # local Part for district
                            @
                            ([0-9]+)				 # Domain name
                            @
                            ([a-z]{2,6})$				 # Top level Domain for state 	
                            """,re.VERBOSE | re.IGNORECASE)
    res=regex_address.fullmatch(address)
    if res:
        print("{} is Valid. Details are as follow:".format(address))
        print("Local:{}".format(res.group(1)))
        print("PINCODE:{}".format(res.group(2)))
        print("State of living:{}".format(res.group(3)))
        print()
    else:
    #If match is not found,string is invalid
        print("{} is Invalid".format(address))

# Address call Code
validate_PersonAdd("kurnool@518002@AP")
validate_PersonAdd("Mumbai@400006@maharastra")


# 20. How would you write a regex that match a number with comma for every three digits? It must match the given following:
# '42'
# '1,234'
# '6,368,745'
# but not the following:
# '12,34,567' (which has only two digits between the commas)
# '1234' (which lacks commas)
# 

# In[45]:


def Match_Digits(*argv):
    pattern=r"^\d(,\d{3})*$|^\d{2}$"
    
    for arg in argv:
        MatchedPattern=re.search(pattern,arg)
        if(MatchedPattern):
            print(f"{arg} has correct pattern")
        else:
            print(f"{arg} has incorrect pattern")
Match_Digits("42","1,234", "6,368,745", "12,34,567","1234","12,123,456")


# 21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:
# 'Haruto Watanabe'
# 'Alice Watanabe'
# 'RoboCop Watanabe'
# but not the following:
# 'haruto Watanabe' (where the first name is not capitalized)
# 'Mr. Watanabe' (where the preceding word has a nonletter character)
# 'Watanabe' (which has no first name)
# 'Haruto watanabe' (where Watanabe is not capitalized)
# 

# In[51]:


def Match_Names(*argv):
    pattern=r"^[A-Z][\w^\d]*\s(Watanabe)$"
    
    for arg in argv:
        MatchedPattern=re.search(pattern,arg)
        if(MatchedPattern):
            print(f"{arg} has correct pattern")
        else:
            print(f"{arg} has incorrect pattern")
Match_Names('Haruto Watanabe','Alice Watanabe','RoboCop Watanabe','haruto Watanabe','Mr. Watanabe','Watanabe','Haruto watanabe')


# 22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:
# 'Alice eats apples.'
# 'Bob pets cats.'
# 'Carol throws baseballs.'
# 'Alice throws Apples.'
# 'BOB EATS CATS.'
# but not the following:
# 'RoboCop eats apples.'
# 'ALICE THROWS FOOTBALLS.'
# 'Carol eats 7 cats.'
# 

# In[56]:


def Match_Patts(*argv):
    pattern=r"^(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)[.]$"
    
    for arg in argv:
        MatchedPattern=re.search(pattern,arg)
        if(MatchedPattern):
            print(f"{arg}--> has correct pattern")
        else:
            print(f"{arg}--> has incorrect pattern")
Match_Patts('Alice eats apples.',
'Bob pets cats.',
'Carol throws baseballs.',
'Alice throws Apples.',
'BOB EATS CATS.',
'RoboCop eats apples.',
'ALICE THROWS FOOTBALLS.',
'Carol eats 7 cats.')


# In[ ]:




