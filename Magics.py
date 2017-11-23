
# coding: utf-8

# In[*]

get_ipython().run_cell_magic('bash', '', 'ls -ltr\necho "will read readme.md"\ncat README.md')


# In[*]

import pandas as pd
df = pd.read_csv('reddituserpostingbehavior.csv.gz', compression='gzip', nrows=10, sep=',', names=['user']+list(range(25))).fillna('')


# In[*]

get_ipython().run_cell_magic('time', '', '\nimport gzip\n\ndef compute_user_subreddit_ids():\n    user_ids = []\n    subreddit_ids = []\n    subreddit_to_id = {}\n    i = 0\n    with gzip.open(\'reddituserpostingbehavior.csv.gz\', \'rb\') as f:\n        for line in f:\n            this_line = line.decode("utf-8")\n            for sr in this_line.rstrip().split(\',\')[1:]:\n                if sr not in subreddit_to_id:\n                    subreddit_to_id[sr] = len(subreddit_to_id)\n                user_ids.append(i)\n                subreddit_ids.append(subreddit_to_id[sr])\n            i += 1\n        return user_ids, subreddit_ids\n    \nuser_ids, subreddit_ids = compute_user_subreddit_ids()')


# # Showing math equations

# In[*]

get_ipython().run_cell_magic('latex', '', '\\begin{aligned}\n\\nabla \\times \\vec{\\mathbf{B}} -\\, \\frac1c\\, \\frac{\\partial\\vec{\\mathbf{E}}}{\\partial t} & = \\frac{4\\pi}{c}\\vec{\\mathbf{j}} \\\\\n\\nabla \\cdot \\vec{\\mathbf{E}} & = 4 \\pi \\rho \\\\\n\\nabla \\times \\vec{\\mathbf{E}}\\, +\\, \\frac1c\\, \\frac{\\partial\\vec{\\mathbf{B}}}{\\partial t} & = \\vec{\\mathbf{0}} \\\\\n\\nabla \\cdot \\vec{\\mathbf{B}} & = 0\n\\end{aligned}')


# # showing profiling tools
# 
# The below command installs line profiler
# 
#     pip install line_profiler
#     pip install memory_profiler

# In[*]

get_ipython().magic('load_ext line_profiler')
get_ipython().magic('load_ext memory_profiler')


# In[*]

# some small functions for example purposes
import numpy as np

def func(n, a):
  y = np.arange(n)
  y = np.exp(-y*a)
  return y

def gunc(n, a):
  y = np.exp(-n*a)
  return y

def hunc(n, a):
  y1 = func(n, a)
  y2 = gunc(n, a)
  return y1, y2


# In[*]

get_ipython().magic('lprun -f func hunc(50000, 0.5)')


# In[*]

get_ipython().magic('memit hunc(50000, 0.5)')

