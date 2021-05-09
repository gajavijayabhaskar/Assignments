#!/usr/bin/env python
# coding: utf-8

# # Assignment 3

# In[ ]:





# 1. Why are functions advantageous to have in your programs?
# solu:
# The major advantage of functions is repeatability of them we can reuse them any number of times in the program which ultimately helps in avoiding the writing of code to perform the same operation/functionality . 

# 2. When does the code in a function run: when it's specified or when it's called?
# solu:
# The code in the function run only when it is called .

# 3. What statement creates a function?
# solu:
# defining the function takes place when we make use of the "def" statement followed by function name and parameters in between the ()parenthesis .It should pass the same number of parameters when it is calling the function has it has defined in its parameters while initialising. Like example below ,
# 
# def funcName(a,b):
#     
#     #statement
#     
#     funcName(a,b)

# 4. What is the difference between a function and a function call?
# solu:
# function is a separate part of the program which has a particular task need to be completed when it is called . Function call is something which calls the function to come and complete the task/work being assigned to it whenever and where-ever required after being called by the function call .

# 5. How many global scopes are there in a Python program? How many local scopes?
# solu:
# Basically there are two types : Global scopes and Local scope.
# Global scope : It is declared at the beginning/outside  of the function/constructor/method because of which it can be accessed from any where in the program.It allocates the memory for them at the beginning of the program itself.
# 
# Local scope :  It is declared inside the method /function/constructor becaus of which it can be accessed inside only the particular method in which it was declared .It allocates the memory only when the function/constructor/method is called or in use.
# 
# if both the variables in global and local have same name then first it will check for local variable if not present them it will take the global variable only when it has same name as of local variable.
# 
# 

# 6. What happens to variables in a local scope when the function call returns?
# solu:
# when the function call returns then the local scope destroy the memory after the execution .

# 7. What is the concept of a return value? Is it possible to have a return value in an expression?
# solu:
# Return value is mostly used in functions/methods.
# The concept of return value is to send the result of a function / method back to the callers statement of the function/method.
# If the defined function has explicit return statement then Yes we can have a return value in expression.
# 

# 8. If a function does not have a return statement, what is the return value of a call to that function?
# solu:
# In such case of function does not have a return statement it will simply return a NONE value .

# 9. How do you make a function variable refer to the global variable?
# solu:
# By using the Global keyword we can make a function variable refer to a global variable but the names of both the variables should be same.

# 10. What is the data type of None?
# solu:
# The data type of None is unique ,it's data type is also "NoneType".

# 11. What does the sentence import areallyourpetsnamederic do?
# solu:
# It imports the module naming areallyourpetsnamederic if it exists.

# 12. If you had a bacon() feature in a spam module, what would you call it after importing spam
# solu:
# step-1: Import spam
# step-2: spam.bacon()

# 13. What can you do to save a programme from crashing if it encounters an error?
# Solu: 
# By handling the expected errors by implementing try and catch method to handle the exceptions.

# 14. What is the purpose of the try clause? What is the purpose of the except clause?
# solu:
# The idea of the try-except clause is to handle runtime exceptions . try clause:consists of code which might trigger exceptions .  exception clause is used, it goes into the except block to let the programmer know about the exception occured and handle it further.
