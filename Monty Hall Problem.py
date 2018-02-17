
# coding: utf-8

# In[1]:

get_ipython().magic('matplotlib inline')
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.notebook_repr_html', True)
import seaborn as sns

prize=[]

for i in range(1,100):
    prize.append(np.random.randint(1,4,1))
    
def choose(a,i):
    for j in range(1,4,1):
        if j==a:
            break
        elif j==prize[i]:
            break
        else:
            return(j)
            
def test(prize):
    win_NC=0
    win_C=0
    lose_NC=0
    lose_C=0

    for i in range(1,99):
        a = np.random.randint(1,4,1)
        goat = choose(a,i)
    
        if prize[i]==a:
            win_NC = win_NC+1
        else:
            lose_NC = lose_NC+1
        
        for k in range(1,4,1):
            if goat==a:
                break
            else:
                a=k
        if prize[i]==a:
            win_C = win_C+1
        else:
            lose_C = lose_C+1
    
    print(win_NC,win_C)    

for tests in range(1,100):
    for i in range(1,100):
        prize.append(np.random.randint(1,4,1))
    print(test(prize))



# In[ ]:



