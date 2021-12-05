#%%
import openrouteservice as ors
from openrouteservice import convert
client = ors.Client(key='5b3ce3597851110001cf6248ec32a01981c344289c76bd7dbc72c78d')
import folium
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ipywidgets import widgets, interact, interactive, fixed , interact_manual

from download import download  # download data / avoid re-downloading
from IPython import get_ipython

pd.options.display.max_rows = 8

#%%
#Importation du tableau des coordonnées des gares de péages
df = pd.read_csv("coordonnees_clean.csv", sep=",")

#%%
#Importation du tableau des prix entre chaque gares de péages
dp = pd.read_csv("prices_clean.csv", sep=",")


#%%
#Fonction qui renvoi le nom de la i_eme gare de péage 
def nom_gare(df,i):
    if isinstance(i,int)== True and 0<=i<=35:
        
        return str(df["NOMGARE"][i])  
    
    else: 
        return "veuillez inserer un entier entre 0 et 42"


#%%
#Classe permettant d'afficher le trajet entre deux gares et ses propriétés
class graphique:
    def __init__(self) -> None:
        pass
    def graph_rang(i,j,df):
        if isinstance(i,int)==True and isinstance(j,int)==True:
            coords = ((df["X"][i],df["Y"][i]),(df["X"][j],df["Y"][j]))
            res = client.directions(coords,preference="fastest")
            geometry = client.directions(coords)['routes'][0]['geometry']
            decoded = convert.decode_polyline(geometry)
            distance_txt = "<h4> <b>Distance :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['distance']/1000,1))+" Km </strong>" +"</h4></b>"
            duration_txt = "<h4> <b>Durée :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['duration']/60,1))+" Mins. </strong>" +"</h4></b>"
            price_txt = "<h4> <b>Prix :&nbsp" + "<strong>"+ str(dp[nom_gare(df,i)][j]) +" € . </strong>" +"</h4></b>"
            m = folium.Map(location=[df["Y"][i],df["X"][i]],zoom_start=9, control_scale=True,tiles="cartodbpositron")
            folium.GeoJson(decoded).add_child(folium.Popup(distance_txt+duration_txt+price_txt,max_width=300)).add_to(m)
        
            folium.Marker(
                location=list(coords[0][::-1]),
                popup=df["NOMGARE"][i],
                icon=folium.Icon(color="green"),
            ).add_to(m)

            folium.Marker(
                location=list(coords[1][::-1]),
                popup=df["NOMGARE"][j],
                icon=folium.Icon(color="blue"),
            ).add_to(m)

            return m
        else:
            return "Vos variables n'ont pas le bon format ou utilisez la fonction 'nomCoord'"


    def distance(i,j,df):
        coords = ((df["X"][i],df["Y"][i]),(df["X"][j],df["Y"][j]))
        res = client.directions(coords, preference="fastest")
        dist=float(round(res['routes'][0]['summary']['distance']/1000,1))
        return dist



#%%
#Exemple de trajet
graphique.graph_rang(3,16,df)



# %%
graphique.distance(3,16,df)


#%%

def prices_distribution(i,j,bw):
    
    n_bins = 24
    alpha = 0.25
    density = False

    vector = []  
    for k in range(j-1):
        vector.extend([float(dp[nom_gare(df,i+k)][i+k+1])/float(graphique.distance(i+k,i+k+1,df))])
    A = np.asarray(vector)

    sns.kdeplot(A, bw_adjust=bw, shade=True, cut=0)
    plt.xlabel("Prix/km")
    plt.ylabel("Niveau de densité")
    plt.tight_layout()
    plt.show()
    
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    ax.hist(A, density=density, bins=n_bins, alpha=alpha)  # standardization
    plt.xlabel("Prix/km")
    plt.ylabel("Niveau de densité")
    plt.tight_layout()
    plt.show()
    
#%%
prices_distribution(3,19,0.5)

# %%
