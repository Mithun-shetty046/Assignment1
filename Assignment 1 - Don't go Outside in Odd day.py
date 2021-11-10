#!/usr/bin/env python
# coding: utf-8

# Write a Python program to count the number of even and odd numbers from a series of numbers.
# 
# 
# 
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# 
# Expected Output :
# 
# Number of even numbers : 5
# 
# Number of odd numbers : 4

# In[6]:


num=[1,4,3,6,10,9,56,4,8,123,65]

Even_count=0
Odd_count=0

for i in num:
    if i%2==0:
        Even_count=Even_count+1
    else:
        Odd_count=Odd_count+1

print('Count of Even numbers: ',Even_count)
print('Count of Odd numbers: ',Odd_count)


# In[ ]:




