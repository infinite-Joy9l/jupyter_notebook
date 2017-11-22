
# coding: utf-8

# # Starting a jupyter notebook

# In[*]

get_ipython().magic('matplotlib inline')

import matplotlib.pyplot as plt



# In[*]




# In[*]




# In[*]




# # Linking to some other file

# In[*]

from IPython.display import FileLink, FileLinks
file = FileLink('Magics.ipynb')


# In[*]

file


# # Debugging using pdb

# In[*]

import pdb

def some_long_function():
    x = 0
    for i in range(10):
        import pdb; pdb.set_trace()
        x = i*2
    return x

print(some_long_function())

