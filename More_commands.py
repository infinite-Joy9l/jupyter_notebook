
# coding: utf-8

# # Starting a jupyter notebook

# In[*]

get_ipython().magic('matplotlib inline')

import matplotlib.pyplot as plt


# In[*]

get_ipython().magic('load_ext version_information')
get_ipython().magic('version_information scipy, numpy, Cython, matplotlib, version_information')


# ## SHould give date information at the start of every notebook

# In[*]

import datetime
print('This notebook last run on {date}'.format(date=datetime.datetime.today()))


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

