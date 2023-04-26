# Paris-rent-prediction

This application is a simulation of rent prices in Paris (per square meter) according to several criteria.

The model used is a SVR.

Origin of the training data : https://www.data.gouv.fr/fr/datasets/logement-encadrement-des-loyers/

Installation : 
- ```Git clone : https://github.com/AranOribu/Paris-rent-prediction.git``` in the desired folder.

- ```pip install -r requirements.txt``` in the desired folder.

- Run the **app.py** file and go to the local url displayed in the terminal.

- Select your criteria and click on the predict rent button.

![image](https://user-images.githubusercontent.com/64967048/234602411-c1510001-0606-4265-ad1d-2e12314b3df2.png)

<hr>

To try the model with the API use the local link displayed in the terminal with the path ***/predict***  (*POST REQUEST ONLY*).

Example : http://127.0.0.1:5000/predict

Example of data sent to the API : 
```json
{
 "nom_quartier": "Goutte-d'Or",
    "piece": 3,
    "epoque": "1971-1990",
    "meublé": "meublé"
 }
 ```
 
The criteria have predefined values:

 - for the criterion 'nom_quartier' (neighborhood name) : <br>
        "Goutte-d'Or", 'Petit-Montrouge', 'Batignolles', 'Combat',
       'Roquette', 'Sainte-Marguerite', 'Sorbonne', 'Faubourg-du-Roule',
       'Bel-Air', "St-Germain-l'Auxerrois", 'Bercy', 'Folie-Méricourt',
       'Faubourg-Montmartre', 'Porte-Saint-Denis', 'Auteuil', 'Europe',
       'Madeleine', 'Montparnasse', 'Saint-Merri', 'Enfants-Rouges',
       'Muette', 'Saint-Vincent-de-Paul', 'Vivienne', 'Rochechouart',
       'Porte-Dauphine', 'Clignancourt', 'Halles', 'Bonne-Nouvelle',
       'Gaillon', 'Hôpital-Saint-Louis', 'Mail', 'Charonne',
       'Saint-Georges', 'Plaisance', 'Maison-Blanche', 'Salpêtrière',
       'Jardin-des-Plantes', "Saint-Thomas-d'Aquin", 'Amérique',
       'Monnaie', 'Ecole-Militaire', 'Saint-Gervais', 'Père-Lachaise',
       'Chaillot', 'Archives', 'Notre-Dame-des-Champs', 'Croulebarbe',
       'Ternes', 'Saint-Fargeau', "Chaussée-d'Antin", 'Gros-Caillou',
       'Pont-de-Flandre', 'Invalides', 'Champs-Elysées', 'Belleville',
       'Gare', 'Saint-Lambert', 'Arts-et-Metiers', 'Odeon', 'Picpus',
       'Arsenal', 'Grenelle', 'Sainte-Avoie', 'Saint-Germain-des-Prés',
       'Val-de-Grace', 'Grandes-Carrières', 'Porte-Saint-Martin',
       'Villette', 'La Chapelle', 'Palais-Royal', 'Parc-de-Montsouris',
       'Quinze-Vingts', 'Javel 15Art', 'Notre-Dame', 'Epinettes',
       'Saint-Ambroise', 'Plaine de Monceaux', 'Necker', 'Saint-Victor',
       'Place-Vendôme'

 - the criterion 'piece' takes only the values **1,2,3 or 4** (number of rooms).

 - the criterion 'epoque': '1971-1990', '1946-1970', 'Apres 1990', 'Avant 1946' (period of construction of the buildings).
  
 - the criterion 'meublé' takes only 2 values : 'meublé' or 'non_meublé' ('furnished' or 'unfurnished).

![image](https://user-images.githubusercontent.com/64967048/234604345-2dd66c9d-e509-496b-9fc7-c4ae9e79435a.png)

    
