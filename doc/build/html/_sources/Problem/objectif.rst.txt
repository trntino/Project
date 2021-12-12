
Rapport 
===================

- Introduction
Dans le cadre du cours de d´eveloppement logiciel, il nous a ´été donnée pour projet de créer un package qui permettrait d’utiliser Map interactive des autoroutes du Sud de la France. Cette Map aurait pour intéré de renseigner le trajet le moins cher en terme de cout de>
2 Présentation du Package
- La Map

La Map est l'objectif central de notre projet. C'est en effet son aspect le plus pragmatique.
Elle permet à un utilisateur qui souhaiterais se déplacer entre une des villes presentée sur les données.
de visualiser son voyage et d'être informer du trajet a effectuer pour que le coût des péages lui soit minimum. Voyons tout de suite un exemple :
Alfonse habite dans l'Ouest Montpellierain et souhaite rendre visite à son ami qui vie à proximité de la sortie "Le Palays" dans la banlieue de Toulouse.
Il aimerait néanmoins que son trajet lui revienne le moins cher possible et puisque le voyage sera long, il prévoit de s'arrêter deux fois en cours de route. 
En utilisant la Map que nous avons développé, Alfonse va pouvoir déterminer où sortir afin que ses deux arrêts lui permettent d'optimiser le coût de son voyage. 
En effet une fois que les caractéristiques de son trajet auront été saisi (nom gare de départ, nom gare d'arrivée, nombre d'arrêts), 
la Map lui renverra le message suivant : Si vous sortez aux gares : (Beziers ouest,Lezignan), votre trajet vous coutera 20.3 €. Vous aurez ainsi fait une economie de 3.4 € sur le coût des péages.


- Distributions des Prix
Le deuxième aspect de notre package est de rendre compte de la distribution des prix entre les différentes gares de péages listées précédemment. Cette partie de notre travail est destinée à un utilsateur curieux de connaître la politique des prix mise en place par l'entreprise ASF (propriétaire des autoroutes). \newline\vspace{0.2cm}
En choisissant une gare d'entrée et une gare de sortie, notre programme va renvoyer les différentes fréquences de prix par kilomètres. En reprenant l'exemple précédent, voici ce que renverrait notre programme 
Alfonse constaterais alors que le prix par kilomètres est le plus souvent compris entre 0.08\euro / km et 0.1\euro /km.


- Data cleaning

La premiére étape  est de traiter les données qui nous ont été fourni afin que nous puissions les utiliser a nos
fins. Nous avons tout d’abord transformer les données de la page 3 du pdf suivant en format .csv afin de lui
utiliser via le logiciel VScode : https://public-content.vinci-autoroutes.com /PDF/Tarifs-peage-asf-vf/ASF-C1-TARIFS-WEB-2021-maille-vf.pdf
Nous avons ensuite supprimer les lignes et les colonnes qui nous ´etaient inutiles, c’est `a dire les lignes (respectivement les colonnes) qui faisaient réféences à des gares de péages qui ne constituaient pas des ”sorties” possibles. Par exemple, le Peage de Montpellier St-Jean.
Nous avons répété cette procédure avec le fichier :
gares-peage-2019.csv
disponible à l’url suivant : https://www.data.gouv.fr/en/datasets/gares-de-peage-du-reseau-routiernational-concede/. Nous avons ainsi supprimé les gares de péages qui ne faisait pas partie de notre champs
d’analyse (les gares de p´eages qui ne sont pas propos´ees dans le fichier des prix) afin de pouvoir l’utiliser en
parallèle avec le fichier des prix. Nous avons de plus supprimer toute les colonnes qui nous ´etaient inutiles afin
de ne garder au final que les colonnes qui indiquaient pour chaque gares leur nom, la section d’autoroute sur
laquelle elle était située et leurs coordonnées X et Y.
Une fois notre nettoyage de donn´ees r´ealis´e (voir le code : data cleaning.py), nous avons sauvegardé nos
résultats sous forme de dataframes dans les fichiers : prices clean.csv et coordonnees clean.csv.


- Algorithme du chemin le moins cher
Cette étape fut une des plus difficile à mettre en oeuvre. Notre objectif était le suivant : calculer le cout de
péage le moins ´elev´e entre un point de d´epart et d’arriv´e en fonction du nombre d’arrˆet qu’il ´etait possible de
faire.
Dans un premier temps, nous devions trouver le moyen de compter le nombre de gares pr´esentent sur le trajet
entre notre gare de d´epart et d’arrivée. Pour ce faire, nous avons d’abord partitionner les gares en fonction de
la portion de route sur laquelle elles étaient situées. 

