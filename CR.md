# Compte-Rendus des Séances

Groupe AlphaGo:
- Romain Marques | romainmarques01@gmail.com
- Ivan Besevic | ivan.besevic_fr@yahoo.com
- Laurent GRONDIN | alter.gnu@gmail.com
- Mohamed Diallo | lanzark43@gmail.com
- Julie Gaydon | julie.gaydon@gmail.com

## Semaine 1 (du dimanche 31/01 au 03/02)
### Déroulé de la séance
Après avoir individuellement pris en main les différents outils de développement:(tutos/docs:trello, git, POO-Python
...) nous avons échangé nos idées concernant ce projet.

Comme présenté dans le cours, il se décompose en 3 grandes étapes :
- 1 : Construire un environnement de simulation pour le robot
- 2 : Développement et implémentation d'une "IA" permettant au robot de réaliser un certain nombre de tâches imposées :
  - i) Dessiner un carré
  - ii) S'approcher le plus vite possible et le plus près d'un mur sans le toucher
  - iii) Suivre une balise
- 3 : Développer notre "IA" afin qu'elle accomplisse des tâches plus complexes. (choix libre des scenari possibles)

Ces étapes devant être réalisées dans l'ordre, nous avons ensuite passé le reste de la séance à organiser l'étape 1
(avec un délai de livraison estimé à 5 semaines) et pour cela, nous avons:

- Établi le rôle et l'intérêt d'une telle interface de simulation:
  - *A terme, elle devra reproduire le plus justement possible le comportement du robot dans son environnement (Réel)*
  - *Cette interface de simulation nous permettra alors de mettre à l'épreuve le code du robot que nous aurons à développer au cours des étapes/semaines suivantes.*
- Pour cela, et dans un premier temps, nous devons nous représenter le plus simplement possible notre système:{environnement+robot}:
  - l'entité Environnement du système peut alors être résumée à un plan de l'espace, dans lequel sont placés des objets(~obstacles)
  - l'entité Robot, pouvant être représenté comme un objet, se déplaçant dans l'environnement.
- Nous avons ensuite réfléchi à l'implémentation d'un tel modèle, en le décomposant en
tâches/étapes/contraintes, elles mêmes décomposées en tâches élémentaires.
- Enfin, et avec les objectifs de la semaine en tête, nous avons planifié le sprint en nous répartissant le travail.

Notre approche consiste donc en une simplification maximale du système étudié, nous permettant ainsi de construire un modèle fonctionnel auquel nous ajouterons progressivement de la complexité (cela ayant pour objectif de nous rapprocher au fur et à mesure du système réel étudié)

C'est dans cette optique que nous avons été amenés à faire les choix suivants :

### Choix fait
- Se limiter à un espace à deux dimensions.(Donc 3 avec le temps, car notre système est évolutif : déplacement du robot)
- Modéliser cet espace de l'espace en 2D par une Grille (approche par Discrétisation de l'espace et du temps)


Concrètement, du point de vu utilisateur, cela aura pour conséquence le fait que les premières visualisations des simulations devront être interprétées comme une vue du dessus du déplacement d'un robot sur un terrain.

### Objectifs Sprint
Pour cette première semaine, nous avons choisi pour objectif principal de modéliser un terrain et la présence ou non d'objet sur ce-dernier, ce qui peut se traduire par la story :

*"En tant que développeur, je veux pouvoir afficher sur ma console une grille représentant un terrain sur lequel je veux pouvoir placer des objets"*

### Rétrospective/Bilan
#### Réussites
#### Difficultées

## Semaine 2 (du mercredi 03/02 au 10/02)
Pour cette deuxième semaine de sprint, nous avons choisi comme fonctionnalité principale de pouvoir ajouter un robot sur le terrain et de pouvoir le faire bouger. Pour ceci, nous avons dû d'abord discuter sur le meilleur moyen de pouvoir faire bouger le robot. Nous avons alors décidé que ce dernier devrait avoir une position, représentée par les coordonnées x et y, une vitesse, un angle d'inclinaison et un vecteur de déplacement.

Pour ce faire, nous avons rajouté une classe Vecteur, qui est composée d'un attribut x et d'un attribut y pour représenter sa position, et s'occupe de calculer la norme d'un vecteur, la somme de vecteurs ainsi que la multiplication de vecteurs. Enfin, sa fonctionnalité la plus importe est qu'elle permet de calculer un nouveau vecteur issu de la rotation du robot. Cette fonctionnalité permet de faire tourner le robot en fonction d'un angle. Le robot peut aussi avancer en fonction du temps passé en paramètres de la méthode. 

Quant au Terrain, nous avons développé une méthode pour pouvoir rendre une case vide, ce qui permet de supprimer un obstacle ou de retirer l'ancienne position du robot de la carte, et désormais l'affichage permet de regarder le robot sur la grille et donc de modéliser le déplacement de ce dernier. 

L'attribut vitesse et le vecteur de déplacement du Robot sont initialisés via la méthode vitesse qui prend comme initialisation 0 puis met à jour la vitesse. 
### Déroulé de la séance
### Choix fait
### Objectif
### Rétrospective/Bilan
#### Réussites
#### Difficultées


