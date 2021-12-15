Map
===================================================

Catte partie parle sur la construction de la map car elle reprrésente la clé
 du projet.

Grace aux aux données suivantes : 

- distributions des prix :
Cette partie de notre travail est destinée à un utilsateur curieux de 
connaitre la politique des prix mise en place par l’entreprise ASF .
En choisissant une gare d’entrée et une gare de sortie, notre programme va 
renvoyer les différentes fréquences de prix par kilométres. 
Voici ce que renverrait notre programme :

<center>

![Exemple d](doc/source/deloqqv/output.png)

</center>

Nous castatons que le prix par kilomètres est compris entre 0.8 euro/km
et 0.1 euro/km.

-Data cleaning:
La première étape à été de traiter les données qui nous ont été fourni afin 
que nous puissions les utiliser a nos fins. Nous avons tout d’abord 
transformer les données de la page 3 du pdf suivant en format .csv afin de lui
utiliser.

</center>

https://public-content.vinci-autoroutes.com
/PDF/Tarifs-peage-asf-vf/ASF-C1-TARIFS-WEB-2021-maille-vf.pdf

</center>
Nous avons ainsi faire le traitement pour la rendre utulisable pour une 
visusalisation

Nous avons répété cette procédure avec le fichier :
 gares-peage-2019.csv 

disponible à l’url suivant 
</center>

: https://www.data.gouv.fr/en/datasets/gares-de-peage-du-reseau-routiernational-concede/.

</center>
 Nous avons ainsi supprimé les gares de p´eages qui ne faisait pas partie 
de notre champs d'analyse.

- Creation de la Map

La dernière étape de notre projet fut la création de la Map qui permettrait une utilisation pragmatique de
notre package.
Pour ce faire, nous avons utilisé le package python suivant :

</center>

openrouteservice

</center>

pour lequel nous avons du  créer un compte afin qu’il nous renvoi une clé de connexion :

</center>

clé = 5b3ce3597851110001cf62486f5564a064e34f3895221e5a0d9a2405

</center>

nécessaire pour son utilisation. En utilisant les dataframes prices clean.csv et coordonnees clean.csv
nous avons défini une classe map comprenant les fonction index prenant comme seul paramétre le nom d’une
gare de péage et qui renvoi son index, et la fonction road(DEPART,ARRIVEE) qui nous permet de convertir
les coordonn´ees ”X” et ”Y” de chaque gare de p´eage en format GPS afin d’afficher le trajet entre la gare de
départ et d’arrivée ainsi que son prix et la distance entre les deux gares.
Voici un  exeeple de visualisera d'un trajet  ci-dessous :

</center>

![Exemeple](doc/source/deloqqv/im.png)

</center>

  
