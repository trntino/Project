#%%
import numpy as np
import pandas as pd

#%%
df = pd.read_csv('coordonnees.csv',sep=",")
dp = pd.read_csv('price.csv',sep=";")

#%%
#Partitionnement des routes
p1 = df.iloc[0:12,:]
P1 = p1.sort_index(axis=0,ascending = False)
P1 = P1.reset_index()

P2 = df.iloc[12:20,:]
P2 = P2.reset_index()

P3 = df.iloc[20:26,:]
P3 = P3.reset_index()

P4 = df.iloc[26:31,:]
P4 = P4.reset_index()

P5 = df.iloc[31:43,:]
P5 = P5.reset_index()

#%%
#Exemple de partitionnement
P5


#%%
#Groupement des partitions
V1 = pd.concat([P1,P2])
V2 = P3
V3 = pd.concat([P4,P5])

#%%
#Exemple de groupe
V3

#%%
#Associe la gare a sa partition
def partition_gare(i):
    if i>=0 and i<=11 :
        return P1
    if i>=12 and i<=19 :
        return P2
    if i>=20 and i<=25 :
        return P3
    if i>=26 and i<=30 :
        return P4
    if i>=31 and i<=42 :
        return P5

#%%
#test 
partition_gare(35)

#%%
#Associe la gare au nom de sa partition
def nom_partition_gare(i):
    if i>=0 and i<=11 :
        return "P1"
    if i>=12 and i<=19 :
        return "P2"
    if i>=20 and i<=25 :
        return "P3"
    if i>=26 and i<=30 :
        return "P4"
    if i>=31 and i<=42 :
        return "P5"

#%%
nom_partition_gare(35)

#%%
#Associe la partition a son groupement
def groupe_de_la_partition(i):
    if nom_partition_gare(i) == "P1" or nom_partition_gare(i) == "P2" :
        return V1
    if nom_partition_gare(i) == "P4" or nom_partition_gare(i) == "P5" :
        return V3
    if nom_partition_gare(i)== "P3":
        return V2

#%%
groupe_de_la_partition(35)

#%%
#Associe la partition au nom de son groupement
def nom_groupe_partition(i):
    if nom_partition_gare(i) == "P1" or nom_partition_gare(i) == "P2" :
        return "V1"
    if nom_partition_gare(i) == "P4" or nom_partition_gare(i) == "P5" :
        return "V3"
    else :
        return "V2"

#%%
nom_groupe_partition(35)


#%%
#Renvoie le nombre de gare par partition
def nb_de_gare_partition(i):
    return len(partition_gare(i))

#%%
nb_de_gare_partition(35)



#%%
#Renvoie le nombre de gare presente sur le trajet entre la gare i et la gare j
def nb_de_gare_sur_trajet(i,j):
    
    if nom_partition_gare(i)== nom_partition_gare(j) :
        if i==j or abs(i-j)==1 :
            return 0
        return (abs(i-j)-1)
    else :
        if nom_groupe_partition(i)==nom_groupe_partition(j) :
            if partition_gare(i)[partition_gare(i)['index']==i].index.values.astype(int)[0] == partition_gare(j)[partition_gare(j)['index']==j].index.values.astype(int)[0] == 0:
                return 0
            else :
                return partition_gare(i)[partition_gare(i)['index']==i].index.values.astype(int)[0] + partition_gare(j)[partition_gare(j)['index']==j].index.values.astype(int)[0]
        else :
            if (nom_groupe_partition(i)!= "V2") and (nom_groupe_partition(j)!= "V2") :
                if partition_gare(i)[partition_gare(i)['index']==i].index.values.astype(int)[0] == partition_gare(j)[partition_gare(j)['index']==j].index.values.astype(int)[0] == 0:
                    return nb_de_gare_partition(23)
                else :
                    return partition_gare(i)[partition_gare(i)['index']==i].index.values.astype(int)[0] + partition_gare(j)[partition_gare(j)['index']==j].index.values.astype(int)[0] + nb_de_gare_partition(23) 
            else :
                if nom_groupe_partition(i)=="V2" :
                    if partition_gare(i)[partition_gare(i)['index']==i].index.values.astype(int)[0] == partition_gare(j)[partition_gare(j)['index']==j].index.values.astype(int)[0] == 0  or  partition_gare(i)[partition_gare(i)['index']==i].index.values.astype(int)[0]-5 == partition_gare(j)[partition_gare(j)['index']==j].index.values.astype(int)[0] == 0:
                        return 0
                    else : 
                        if nom_groupe_partition(j)=="V1":
                            return partition_gare(i)[partition_gare(i)['index']==i].index.values.astype(int)[0] + partition_gare(j)[partition_gare(j)['index']==j].index.values.astype(int)[0]
                        if nom_groupe_partition(j)=="V3":
                            return (partition_gare(i)[partition_gare(i)['index']==i].index.values.astype(int)[0]-nb_de_gare_partition(23)) + partition_gare(j)[partition_gare(j)['index']==j].index.values.astype(int)[0]
                if nom_groupe_partition(j)=="V2":
                    if partition_gare(i)[partition_gare(i)['index']==i].index.values.astype(int)[0] == partition_gare(j)[partition_gare(j)['index']==j].index.values.astype(int)[0] == 0  or  partition_gare(j)[partition_gare(j)['index']==j].index.values.astype(int)[0]-5 == partition_gare(i)[partition_gare(i)['index']==i].index.values.astype(int)[0] == 0:
                        return 0
                    else : 
                        if nom_groupe_partition(i)=="V1":
                            return partition_gare(i)[partition_gare(i)['index']==i].index.values.astype(int)[0] + partition_gare(j)[partition_gare(j)['index']==j].index.values.astype(int)[0]
                        if nom_groupe_partition(i)=="V3":
                            return (partition_gare(j)[partition_gare(j)['index']==j].index.values.astype(int)[0]-nb_de_gare_partition(23)) + partition_gare(i)[partition_gare(i)['index']==i].index.values.astype(int)[0]
                
#%%
nb_de_gare_sur_trajet(35,3)




# %%
#Renvoie le dataframe ordonnée des gares entre la gare i et j du trajet (i,j)
def tab_algo(i,j):
    
    if nom_partition_gare(i)== nom_partition_gare(j) :
        if i==j or abs(i-j)==1 :
            return "Veuiller entrer deux chiffre différents"
        else :
            if i<j :
                df1 = df.iloc[i:j,:]
                return df1
            else :
                df1 = df.iloc[j:i,:]
                DF1 = df1.sort_index(axis=0,ascending = False)
                return DF1
    
    else :
        
        if nom_groupe_partition(i)==nom_groupe_partition(j) :
            df1 = partition_gare(j).iloc[0:partition_gare(j)[partition_gare(j)['index']==j].index.values.astype(int)[0]+1,:]
            df2 = partition_gare(i).iloc[0:partition_gare(i)[partition_gare(i)['index']==i].index.values.astype(int)[0]+1,:]
            DF2 = df2.sort_index(axis=0,ascending = False)
            return pd.concat([DF2,df1])
            
        else :
            if (nom_groupe_partition(i)!= "V2") and (nom_groupe_partition(j)!= "V2") :
                if nom_groupe_partition(i)=="V1":
                    df1 = partition_gare(j).iloc[0:partition_gare(j)[partition_gare(j)['index']==j].index.values.astype(int)[0]+1,:]
                    df2 = partition_gare(i).iloc[0:partition_gare(i)[partition_gare(i)['index']==i].index.values.astype(int)[0]+1,:]
                    DF2 = df2.sort_index(axis=0,ascending = False)
                    return pd.concat([DF2,V2,df1])
                else :
                    df1 = partition_gare(j).iloc[0:partition_gare(j)[partition_gare(j)['index']==j].index.values.astype(int)[0]+1,:]
                    df2 = partition_gare(i).iloc[0:partition_gare(i)[partition_gare(i)['index']==i].index.values.astype(int)[0]+1,:]
                    DF2 = df2.sort_index(axis=0,ascending = False)
                    DV2 = V2.sort_index(axis=0,ascending=False)
                    return pd.concat([DF2,DV2,df1])
                
            else :
                if nom_groupe_partition(i)=="V2" :
                    if nom_groupe_partition(j)=="V1":
                        df1 = partition_gare(j).iloc[0:partition_gare(j)[partition_gare(j)['index']==j].index.values.astype(int)[0]+1,:]
                        df2 = partition_gare(i).iloc[0:partition_gare(i)[partition_gare(i)['index']==i].index.values.astype(int)[0]+1,:]
                        DF2 = df2.sort_index(axis=0,ascending = False)
                        return pd.concat([DF2,df1])
                    
                    else :
                        df1 = partition_gare(j).iloc[0:partition_gare(j)[partition_gare(j)['index']==j].index.values.astype(int)[0]+1,:]
                        df2 = partition_gare(i).iloc[partition_gare(i)[partition_gare(i)['index']==i].index.values.astype(int)[0]+1:nb_de_gare_partition(23),:]
                        DF2 = df2.sort_index(axis=0,ascending = False)
                        return pd.concat([DF2,df1])
                
                
                if nom_groupe_partition(j)=="V2":
                    if nom_groupe_partition(i)=="V1":
                        df1 = partition_gare(j).iloc[0:partition_gare(j)[partition_gare(j)['index']==j].index.values.astype(int)[0]+1,:]
                        df2 = partition_gare(i).iloc[0:partition_gare(i)[partition_gare(i)['index']==i].index.values.astype(int)[0]+1,:]
                        DF2 = df2.sort_index(axis=0,ascending = False)
                        return pd.concat([DF2,df1])
                    
                    else :
                        df1 = partition_gare(i).iloc[0:partition_gare(i)[partition_gare(i)['index']==i].index.values.astype(int)[0]+1,:]
                        df2 = partition_gare(j).iloc[partition_gare(j)[partition_gare(j)['index']==j].index.values.astype(int)[0]+1:nb_de_gare_partition(23),:]
                        DF1 = df1.sort_index(axis=0,ascending = False)
                        return pd.concat([DF1,df2])

#%%
tab_algo(3,35)



#%%
def index_gare(dataframe,gare):
    data_gare = dataframe[dataframe["NOMGARE"]==gare]
    index = int(data_gare["index"])
    return index

#%%
index_gare(df,'Vendargues')



#%%
#renvoi le nom de la gare en fonction de son index
def nom_gare(dataframe,i):
    return str(dataframe["NOMGARE"][i])  

#%%
nom_gare(df,35)


#%%
def Le_Trajet(dataframe):
    tab = dataframe[["index","ROUTE","NOMGARE","X","Y"]]
    tab = tab.reset_index()
    return tab

#%%
Le_Trajet(tab_algo(3,35))

#%%
tab = Le_Trajet(tab_algo(3,35))
gare = nom_gare(df,35)
index_gare(tab,gare)
index_gare(Le_Trajet(tab_algo(3,35)),nom_gare(df,35))


#%%
#renvoi le cout minimum entre pour le trajet de i a j
def cout_minimum(tab_ord_gares,dep,arr) :

    min_cout=float(dp[nom_gare(tab_ord_gares,dep)][index_gare(df,nom_gare(tab_ord_gares,arr))])

    for l in range(arr):
        
        cout = float(dp[nom_gare(tab_ord_gares,dep)][index_gare(df,nom_gare(tab_ord_gares,l))]) + float(dp[nom_gare(tab_ord_gares,l)][index_gare(df,nom_gare(tab_ord_gares,arr))])

        if cout < min_cout :
            min_cout = cout
            sortie = nom_gare(tab_ord_gares,l)
                
    return "Si vous sortez a " + sortie + " le prix de votre trajet est de " + str(min_cout) + " €"

#%%
cout_minimum(df,3,9)
#%%
cout_minimum(Le_Trajet(tab_algo(3,35)),0,16)
#%%




# %%
#Renvoi le parcours le moins cher pour le trajet de la gare i a j
def chemin_moins_cher(i,j,k):
    
    nb_de_noeuds_possible = nb_de_gare_sur_trajet(i,j)
    nb_de_noeuds_souhaite = k

    if nb_de_noeuds_possible  < nb_de_noeuds_souhaite :
        return "Choisissez un nombre de noeuds inferieur ou egal a : " + str(nb_de_noeuds_possible) 

    else :
        
        data = tab_algo(i,j)
        trajet = Le_Trajet(data)
        
        depart_index = 0
        if nom_partition_gare(i)== nom_partition_gare(j) :
            arrivee_index = nb_de_gare_sur_trajet(i,j)
        else :
            arrivee_index = nb_de_gare_sur_trajet(i,j) +1

        
        if nb_de_noeuds_souhaite == 0 :
            return "Le prix de votre trajet est de : " + str(dp[nom_gare(trajet,depart_index)][index_gare(df,nom_gare(trajet,arrivee_index))]) + " €"

        else :
            return cout_minimum(trajet,depart_index,arrivee_index)
        

# %%
chemin_moins_cher(3,23,1)
# %%
chemin_moins_cher(3,9,0)
# %%
