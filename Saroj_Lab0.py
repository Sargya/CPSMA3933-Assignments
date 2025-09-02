#!/usr/bin/env python
# coding: utf-8

# # Assignment CPSMA 3933
#  
# 
# **Name:** Saroj Bhandari  
# **Class:** CPSMA 3933  
# **Assignment:** Computer Lab #0  
# **Date:** September 2, 2025  
# 
# ---
# 

# # My Favorite Python Function
# 
# My favorite function is `len()`. I like it because it quickly tells me the number of elements in a list, string, or other collection. It saves time when working with datasets or checking user input length, and I use it almost every time I code.  
# 

# # My Custom Function Using Python
# 
# I created a function called `square()` that returns the square of a number. This is useful in mathematics, data analysis, and machine learning applications.  
# 

# In[2]:


def square(x):
    return x * x

# Testing my function with different values
print("Square of 2:", square(2))
print("Square of 5:", square(5))
print("Square of 10:", square(10))


# ## Working with Lists
# 
# Here is a list of 10 numbers I generated. I will compute the **sum**, **minimum**, **maximum**, and the **average** of the numbers.  
# 

# 

# In[4]:


numbers = [4, 7, 2, 9, 12, 6, 3, 8, 15, 10]

print("Numbers:", numbers)
print("Sum:", sum(numbers))
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Average:", sum(numbers)/len(numbers))


# In[ ]:




