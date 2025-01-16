"""This module is created to process the user input data"""

# Importing the necessaries libraries
import numpy as np
import pickle
import pandas as pd
# import sklearn
from sklearn.preprocessing import StandardScaler
import os

# Create a function for the pre-process data

def preprocess_data(data):

    # Accepting user input in form of a list
    user_input= [data['Location'], data['min.temp'], data['max.temp'], data['Evaporation'], data['Rainfall'],
                data['Sunshine'], data['WindGustDir'], data['WindGustSpeed'], data['WindDir9am'],
                data['WindDir3pm'], data['WindSpeed9am'], data['WindSpeed3pm'], data['Humidity9am'], data['Humidity3pm'],
                data['Pressure9am'], data['Pressure3pm'], data['Cloud9am'], data['Cloud3pm'], data['Temp9am'],
                data['Temp3pm'], data['RainToday'], data['Day'], data['Month'], data['Year']]
    
    # # Convert user input to 2D array
    input_array= np.array(user_input).reshape(1, -1)

    # file_path = os.path.join(os.path.dirname(__file__), 'models', 'scaler.pkl')

    # C:\Users\HP\Desktop\python_project\machine_learning\weather-prediction-systems\models\scaler.pkl

    # Load the scaled trained data
    with open('.\models\scaler.pkl', 'rb') as scaler_file:
        scaler= pickle.load(scaler_file)

    # Transform the input array to standard scaler using the trained scaled
    scaled_input= scaler.transform(input_array)

    return scaled_input
