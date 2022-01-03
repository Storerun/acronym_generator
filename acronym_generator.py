#!/usr/bin/env python
# coding: utf-8

# ## Description
# This is an acronym generator that produces abbreviations using the first letter of each word in a phrase.
# The first line of the code uses the input function which allows the user to input whatever phrase they want.
# Then an empty string is initialized and stored in a varibale called output. Using the string method split to converts the string into a list then  a 'for loop' is used to iterate over the first letter of each word in the list.

# In[3]:


text= input('Enter a phrase: ')
output=''
for letter in text.split():
    output+= str(letter[0]).upper()
print(output)    


# In[ ]:





# In[ ]:




