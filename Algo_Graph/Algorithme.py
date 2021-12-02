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
#Groupement des partitions
V1 = [P1,P2]
V2 = P3
V3 = [P4,P5]

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
#Associe la partition a son groupement
def groupe_de_la_partition(i):
    if nom_partition_gare(i) == "P1" or nom_partition_gare(i) == "P2" :
        return V1
    if nom_partition_gare(i) == "P4" or nom_partition_gare(i) == "P5" :
        return V3
    if nom_partition_gare(i)== "P3":
        return V2

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
#Renvoie le nombre de gare par partition
def nb_de_gare_partition(i):
    return len(partition_gare(i))




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
#renvoi le nom de la gare en fonction de son index
def nom_gare(dataframe,i):

    return str(dataframe["NOMGARE"][i])  


#%%
#renvoi le cout minimum entre pour le trajet de i a j
def cout_minimum(dataframe,i,j) :

    min_cout=float(dp[nom_gare(dataframe,i)][j])

    for l in range(j):
        cout = 0
        cout = float(dp[nom_gare(dataframe,i)][l]) + float(dp[nom_gare(dataframe,l)][j])

        if cout < min_cout :
            min_cout = cout
            sortie = nom_gare(dataframe,l)
                
    return "Si vous sortez a " + sortie + " le prix de votre trajet est de " + str(min_cout) + " €"



# %%
#Renvoi le parcours le moins cher pour le trajet de la gare i a j
def chemin_moins_cher(i,j,k):
    
    nb_de_noeuds_possible = nb_de_gare_sur_trajet(i,j)
    nb_de_noeuds_souhaite = k

    if nb_de_noeuds_possible  < nb_de_noeuds_souhaite :
        return "Choisissez un nombre de noeuds inferieur ou egal a : " + str(nb_de_noeuds_possible) 

    else :
        data = tab_algo(i,j)
        trajet = data[["ROUTE","NOMGARE","X","Y"]]
        trajet = trajet.reset_index()
        del trajet["index"]

        depart_index = 0
        arrivee_index = nb_de_gare_sur_trajet(i,j)+1
        
        if k==0 :
            return "Le prix de votre trajet est de : " + str(dp[nom_gare(trajet,depart_index)][arrivee_index]) + " €"

        if k==1 :
            return cout_minimum(trajet,depart_index,arrivee_index)
        




        
            
        
        
    

    

# %%
