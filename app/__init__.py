import os
from flask import Flask, render_template, request, url_for
import numpy as np
import pickle
import gzip

# create and configure the app

def create_app(test_config=None):

    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # Configure the app
    app.config.from_mapping(
        SECRET_KEY= os.getenv('SECRET_KEY', 'fallback-secret-key')    
    )
    
    if test_config is None:

        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)

    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Create route for HTML templates
    @app.route('/')
    def home():
        return render_template('model.html')

    # Create an end point root for the app
    @app.route('/submit_data', methods=['GET', 'POST'])
    def predict():
        # try:
        if request.method == 'POST':
                # Accepting user input
            data= request.form.to_dict()

            # Import preprocessing module
            from .preprocessing import preprocess_data
            processed_data= preprocess_data(data)
            
            # model_path = os.path.join(os.path.dirname(__file__), 'models', 'model.pkl.gz')

            # Loading a compressed model efficiently
            with gzip.open('https://github.com/Ibdam/weather-prediction-systems/blob/main/models/model.pkl.gz', 'rb') as f:
                model = pickle.load(f)

            # Make a prediction and return result in form of an HTML
            prediction = model.predict(processed_data)
            if prediction[0]==True:
                return render_template('rain_result.html')

            else:
                return render_template('no_rain_result.html')
            # except:

    return app
