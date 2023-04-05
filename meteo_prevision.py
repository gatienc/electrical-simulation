import requests
import scipy
import numpy as np
import matplotlib.pyplot as plt
import config


def meteo_prevision(latitude, longitude, hourly, forecast_days):
    # Get the data
    api_request = "https://api.open-meteo.com/v1/forecast?latitude=" + str(latitude) + "&longitude=" + str(longitude) + "&hourly=" + hourly + "&forecast_days=" + str(forecast_days)

    response = requests.get(api_request)
    data = response.json()

    #number of data sent is 24*forecast_days - 1 (the last one is the last at 23:00)

    # Get the temperature
    temperature = data["hourly"]["temperature_2m"]
    print(temperature)
    # Get the direct radiation
    direct_radiation = data["hourly"]["direct_radiation_instant"]
    print(direct_radiation)
    return temperature, direct_radiation



if __name__ == "__main__":
    temperature,direct_radiation=meteo_prevision(config.LATITUDE, config.LONGITUDE, config.HOURLY, config.FORECAST_DAYS)
    sun_energy = np.cumsum(direct_radiation) * config.PANEL_AREA
    
    # Créer le plot et le premier axe des ordonnées
    fig, ax1 = plt.subplots()

    # Plot pour le premier axe des ordonnées
    ax1.plot(temperature, color='blue')
    ax1.set_xlabel('temps (h)')
    ax1.set_ylabel('Temperature (C°)', color='blue')

    # Créer un deuxième axe des ordonnées et l'associer au plot
    ax2 = ax1.twinx()

    # Plot pour le deuxième axe des ordonnées
    ax2.plot(direct_radiation, color='red')
    ax2.set_ylabel('direct_radiation (W/m²)', color='red')

    # Créer un deuxième axe des ordonnées et l'associer au plot

    ax3 = ax1.twinx()
    # Plot pour le deuxième axe des ordonnées
    ax3.plot(sun_energy, color='green')
    ax3.set_ylabel('sun_energy W', color='green')

    # Afficher le plot
    plt.show()



