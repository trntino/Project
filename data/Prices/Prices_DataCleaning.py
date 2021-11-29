#%%
import numpy as np
import pandas as pd

#%%
#Importation du Dataframe des prix entre chaque gares de péages
dp = pd.read_csv('price.csv', sep=";")

#%%
#DataCleaning sur les colonnes 
columns = [
'Vendargues',
'Montpellier est',
'Montpellier sud', 
'Montpellier ouest',
'St-Jean-de-Vedas',
'Le Boulou (peage sys ouvert)',
'Frontiere Espagnole',
'Pamiers nord',
'Pamiers sud',
'Peage de Toulouse sud/ouest',
'Le palays',
'Peage de Toulouse sud/est',
'Montaudran',
'Lasbordes',
'Soupetrad',
'La Roseraie',
'La Croix Daurade',
'Borderouge',
'Les lzards',
'Sesquieres',
]
dpp = dp.drop(columns,axis=1)

#%% 
#DataCleaning sur les lignes
dpp.drop(index=[0,1,2,3,4,5,17,18,29,30,33,35,36,37,38,39,40,41,42])

#%%
#Exportation du DataFrame nettoie
dpp.to_csv('DataFrame_Prix.csv')


# %%
