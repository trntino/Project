#%%
import deloqv
from deloqv import MAP
from deloqv import Algorithme

#%% la map interactive

MAP.interact(MAP.map.road, DEPART=MAP.Cities, ARRIVEE=MAP.Cities)

#%% le nom de la ville apartir de son indice

def name(i):
     for k in range (36):
        if MAP.map.index(MAP.Cities[k]) == i:
            return MAP.Cities[k]

name(6)

#%% l'optimisation de prix du trajet
Algorithme.interact(Algorithme.chemin_moins_cher, Depart=list(range(0,36)),arrivee=list(range(0,36)),Nb_sortie=list(range(0,22)))
