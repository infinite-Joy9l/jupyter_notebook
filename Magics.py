
# coding: utf-8

# In[*]

get_ipython().run_cell_magic('bash', '', 'ls -ltr\necho "will read readme.md"\ncat README.md')


# In[*]

import pandas as pd
df = pd.read_csv('reddituserpostingbehavior.csv.gz', compression='gzip', nrows=10, sep=',', names=['user']+list(range(25))).fillna('')


# In[*]

get_ipython().run_cell_magic('time', '', 'user_ids = []\nsubreddit_ids = []\nsubreddit_to_id = {}\ni = 0\n\nimport gzip\nwith gzip.open(\'reddituserpostingbehavior.csv.gz\', \'rb\') as f:\n    for line in f:\n        this_line = line.decode("utf-8")\n        for sr in this_line.rstrip().split(\',\')[1:]:\n            if sr not in subreddit_to_id:\n                subreddit_to_id[sr] = len(subreddit_to_id)\n            user_ids.append(i)\n            subreddit_ids.append(subreddit_to_id[sr])\n        i += 1')


# In[*]

get_ipython().run_cell_magic('time', '', "import numpy as np\nfrom scipy.sparse import csr_matrix\n\nrows = np.array(subreddit_ids)\ncols = np.array(user_ids)\ndata = np.ones((len(user_ids),))\nnum_rows = len(subreddit_to_id)\nnum_cols = i\n\n# the code above exists to feed this call.\nadj = csr_matrix((data, (rows, cols)), shape=(num_rows, num_cols))\nprint(adj.shape)\nprint('')")

