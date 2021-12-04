#%%
import numpy as np
import pandas as pd
import csv

#%%
df = pd.read_csv('coordonnees_algo.csv',sep=",")
dp = pd.read_csv('price_algo.csv',sep=";")

#%%
########### Data Cleaning du dataframe des coordonnees ###########
# %%
df.drop([5,8,17,28,32,34],0,inplace=True)
# %%
df = df.reset_index()
# %%
df['index'] = df.index
# %%
del df["level_0"]

#%%
########### Data Cleaning du dataframe des prix ###########
# %%
dp.drop([5,8,17,28,32,34],0,inplace=True)
#%%
columns = ["Peage de Montpellier St-Jean","Peage de Beziers-Cabrials","Peage du Perthus","Peage de pamiers","Peage de Toulouse sud/ouest","Peage de Toulouse sud/est"]
dp.drop(columns,axis = 1,inplace=True)

#%%
dp = dp.reset_index()
# %%
dp['index'] = dp.index
# %%
del dp["index"]
# %%
########### Enregistrement des dataframes cleaned ###########
#%%
df.to_csv('coordonnees_clean.csv',index=False)
#%%
dp.to_csv('prices_clean.csv',index=False)


