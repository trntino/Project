#%%
import openrouteservice as ors
from openrouteservice import convert
client = ors.Client(key='5b3ce3597851110001cf6248ec32a01981c344289c76bd7dbc72c78d')
import folium
import pandas as pd



#%%
#Importation du tableau des coordonnées des gares de péages
df = pd.read_csv("coordonnees.csv", sep=",")

#%%
#Importation du tableau des prix entre chaque gares de péages
dp = pd.read_csv("price.csv", sep=";")


#%%
#Fonction qui renvoi le nom de la i_eme gare de péage 
def nom_gare(df,i):
    if isinstance(i,int)== True and 0<=i<=42:
        
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
