#%%
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import folium
import geopandas as gpd
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import osmnx as ox
import pandas as pd
from shapely import geometry
from pyproj import Proj, transform
pd.options.display.max_rows = 8

#%%
#Reading the file as a `pandas` dataframe:
df = pd.read_csv('gares-peage-2019.csv', sep=";")

#%%
#Extraction des données relatives aux autoroutes A9,A709,A61,A62,A75 et A66
data_route=df[(df.route=="A0009") | (df.route=="A0061") | (df.route=="A0062") | (df.route=="A0066") | (df.route=="A0075") | (df.route=="A0709")]
data_route = data_route.reset_index()
data_route = data_route[['route',' Nom gare ','x','y']]

# %%
# Transformation des coordonéées Lambert93 en coordonnées GPS
from pyproj import Proj, transform

X = data_route['x']
Y = data_route['y']
inProj = Proj(init='epsg:2154')
outProj = Proj(init='epsg:4326')
GPS = []

for i in range (len(data_route)): 
    GPS.append(transform(inProj,outProj,X[i],Y[i]))


# %%
# Calcul des distances entre chaque gares de péages
import requests
import json
dist=[]
for i in range (len(GPS)):
    if i-1 <0 :
        x,y = GPS[i]
    else : x,y = GPS[i-1]

    x1,y1= GPS[i]

    r = requests.get(f"http://router.project-osrm.org/route/v1/car/{x},{y};{x1},{y1}?overview=false""")
    routes = json.loads(r.content)
    route_1 = routes.get("routes")[0]
    dist.append(route_1['distance']/1000)
print(dist)


# %%
#Importation du Dataframe des prix entre chaque gares de péages
dp = pd.read_csv('price.csv', sep=";")

# %%
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

