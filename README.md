## WEATHER-PREDICTION-SYSTEM
This repository contains a machine learning model for predicting weather condition either it will rain tomorrow based on historical weather data. The historical data was analysed, cleaned and integrate machine learning algorithm to build model. The model built is deployed as a Flask web application, allowing users to input weather parameters and receive predictions.

---
## Features

- Predicts "Rain Tomorrow" or "No Rain Tomorrow" based on user inputs.
- Uses machine learning and historical weather data for predictions.
- Provides a simple web interface with animations for predictions.
- Includes sample data for testing.

---
## SET UP INSTRUCTIONS

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or higher
- Flask
- scikit-learn
- Bootstrap (for front-end styling)
- Seaborn
- Pickle
- Matplotlib
- Numpy
- Pandas

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/ibdam/weather-prediction-systems.git
    cd rain_prediction

## Create and activate a virtual environment
``` bash
python -m venv venv
source venv/bin/activate # On window: venv\Scripts\activate

## Installed the requirements
```bash
pip install requirements.txt

## Running the application locally
```bash
flask --app app run --debug
Access the application at http://127.0.0.1:5000

#Testing by inputting these data manually via the web

## INPUT AND OUTPUT
## Input parameters:
The model takes the following parameters:
1. Location (integer)
2. Min Temp, Max Temp (float)
3. Rainfall, Evaporation (float)
4. Wind Gust Speed, Humidity, Pressure (float)
5. Day, Month, Year (integer)

## Output: Prediction
Prediction: "There will be rain tomorrow" or "No rain tomorrow"

## Example of manual data input for testing
1. With Rain:

    'Location': 15,             # Paris
    'min.temp': 18.0,           # Minimum temperature in °C
    'max.temp': 25.0,           # Maximum temperature in °C
    'Evaporation': 5.0,         # Evaporation in mm
    'Rainfall': 12.0,           # Rainfall in mm (higher value indicates rain likely)
    'Sunshine': 3.0,            # Sunshine hours (low value increases rain likelihood)
    'WindGustDir': 5,           # Wind gust direction (West-South-West)
    'WindGustSpeed': 40.0,      # Wind gust speed in km/h
    'WindDir9am': 3,            # Wind direction at 9am (North-North-East)
    'WindDir3pm': 4,            # Wind direction at 3pm (West)
    'WindSpeed9am': 15.0,       # Wind speed at 9am in km/h
    'WindSpeed3pm': 20.0,       # Wind speed at 3pm in km/h
    'Humidity9am': 90.0,        # Humidity at 9am in %
    'Humidity3pm': 85.0,        # Humidity at 3pm in %
    'Pressure9am': 1010.0,      # Pressure at 9am in hPa
    'Pressure3pm': 1008.0,      # Pressure at 3pm in hPa
    'Cloud9am': 6,              # Cloud cover at 9am (0–8 scale, higher means more clouds)
    'Cloud3pm': 7,              # Cloud cover at 3pm (0–8 scale)
    'Temp9am': 20.0,            # Temperature at 9am in °C
    'Temp3pm': 24.0,            # Temperature at 3pm in °C
    'RainToday': 1,             # Rain today: 1 means "Yes", 0 means "No"
    'Day': 12,                  # Day of the month
    'Month': 8,                 # Month (e.g., August)
    'Year': 2023                # Year   

2. No Rain:
    'Location': 28,             # Jarkarta
    'min.temp': 12.0,           # Minimum temperature in °C
    'max.temp': 22.0,           # Maximum temperature in °C
    'Evaporation': 6.0,         # Evaporation in mm
    'Rainfall': 0.0,            # Rainfall in mm (indicates no rain)
    'Sunshine': 10.0,           # Sunshine hours (high value reduces rain likelihood)
    'WindGustDir': 3,           # Wind gust direction (North)
    'WindGustSpeed': 20.0,      # Wind gust speed in km/h
    'WindDir9am': 2,            # Wind direction at 9am (North-West)
    'WindDir3pm': 3,            # Wind direction at 3pm (West-North-West)
    'WindSpeed9am': 10.0,       # Wind speed at 9am in km/h
    'WindSpeed3pm': 12.0,       # Wind speed at 3pm in km/h
    'Humidity9am': 50.0,        # Humidity at 9am in %
    'Humidity3pm': 40.0,        # Humidity at 3pm in %
    'Pressure9am': 1015.0,      # Pressure at 9am in hPa
    'Pressure3pm': 1013.0,      # Pressure at 3pm in hPa
    'Cloud9am': 1,              # Cloud cover at 9am (0–8 scale, low indicates clear skies)
    'Cloud3pm': 2,              # Cloud cover at 3pm (0–8 scale)
    'Temp9am': 16.0,            # Temperature at 9am in °C
    'Temp3pm': 20.0,            # Temperature at 3pm in °C
    'RainToday': 0,             # Rain today: 0 means "No"
    'Day': 15,                  # Day of the month
    'Month': 3,                 # Month (e.g., March)
    'Year': 2023                # Year

By inputting this paramenters it will bring out the prediction with 85% efficiemcy

Deployment
To deploy the application:

1. Set up a server with Flask and Gunicorn.
2. Create a running app wsgi for deployment
2. Push the code to a cloud platform (e.g. Heroku, AWS, Google Cloud OR Render).

CONTRIBUTING
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request.

LICENCE
This project is licensed under the MIT License. See the LICENSE file for details.
