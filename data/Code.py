#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ipywidgets import interact  # widget manipulation
from download import download  # download data / avoid redownloading
pd.options.display.max_rows = 8

#%%
#Reading the file as a `pandas` dataframe:
df = pd.read_csv('gares-peage-2019.csv', sep=";", header = None)
#%%
df1 =df.dropna()

#%%
#extraction l'entreprise ASF
df11 =df1[df1[16]=='ASF']
df11

# Nous allons extraire les villes qui nous interssent


# %%
df12 = df11()