# the objective of this file is to predict the energy consumption of the next 24 hours 
# to do this, we want to find "the shape" of the consumption curve 
# we notice that this shape per hour is quite similar over time
# of hours but with a different amplitude

# the shape is dependent on the season
# we will use the consumption data of the year 2022 and 2023:
# the file used will be: eCO2mix_RTE_tempo_2022-2023.csv
# this file contains hour by hour consumption data for the whole of France.
# in our case it would have been better to find the form of the consumption for a house.
# 
# from this file, we created a csv file that contains the average consumption of France per hour of the year 2022 and 2023
# we will normalize the consumption according to the expected consumption of the total house in a day
# this expected consumption per day of the dwelling is very dependent on the types of dwellings, of these methods of heatings, of insulation and of the size of the dwelling.

import config
import pandas as pd
import matplotlib.pyplot as plt
def consumption_prevision(consumption_expected):
    #on importe les données de consommation
    df = pd.read_csv('data/typical-daily-energy-consumption.csv',header=0,names=['Heure','Consommation'])


    #on normalise la consommation
    df['Consommation']=(df['Consommation']/df['Consommation'].sum())*consumption_expected
        
    return df['Consommation'].tolist()


if __name__ == "__main__":
    consommation=consumption_prevision(config.CONSUMPTION_EXPECTED)
    plt.plot(consommation)

    plt.xlabel('heure de la journée')
    plt.ylabel('consommation (Wh)')
    plt.title('consommation typique d\'une journée pour un foyer')
    #plt.ylim(0,0.07)
    plt.show()

    