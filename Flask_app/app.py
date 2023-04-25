from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

#  loads a trained encoder from a saved file named
# 'encoder.pkl' in the 'model' directory. The encoder is used to transform the input data before
# making a prediction using the trained model.
encoder = joblib.load('model/encoder.pkl')
model = joblib.load('model/SVR_best_model.pkl')

neighborhoods = ["Goutte-d'Or", 'Petit-Montrouge', 'Batignolles', 'Combat',
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
       'Place-Vendôme']

epochs = ['1971-1990', '1946-1970', 'Apres 1990', 'Avant 1946']

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':

        # get the data from the form
        neighborhood = request.form['nom_quartier']
        rooms = int(request.form['piece'])
        epoch = request.form['epoque']
        furnished = request.form['meublé'] == 'Meublé'

        # create a DataFrame with the input data
        new_data = pd.DataFrame({
            'nom_quartier': [neighborhood],
            'piece': [rooms],
            'epoque': [epoch],
            'meublé': [furnished]
        })

        # transform the input data using the trained encoder saved
        new_data_encoded = encoder.transform(new_data)

        # prediction using the trained model
        prediction = model.predict(new_data_encoded)
        prediction = f"Predicted rent: {prediction[0]:.2f} €"

    return render_template('index.html', neighborhoods=neighborhoods, epochs=epochs, prediction=prediction)

#API
@app.route('/predict', methods=['POST'])
def predict_api():

    # Get the input data from the JSON payload
    data = request.get_json(force=True)

    neighborhood = data['nom_quartier']
    rooms = int(data['piece'])
    epoch = data['epoque']
    furnished = data['meublé'] == 'Meublé'

    prediction = make_prediction(neighborhood, rooms, epoch, furnished)

    # Return the prediction as a JSON object
    response = {
        'predicted_rent': round(prediction, 2)
    }

    return jsonify(response)

def make_prediction(neighborhood, rooms, epoch, furnished):
    
    new_data = pd.DataFrame({
        'nom_quartier': [neighborhood],
        'piece': [rooms],
        'epoque': [epoch],
        'meublé': [furnished]
    })

    new_data_encoded = encoder.transform(new_data)

    prediction = model.predict(new_data_encoded)

    return prediction[0]

if __name__ == '__main__':
    app.run(debug=True)