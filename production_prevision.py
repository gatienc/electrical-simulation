import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
import numpy as np
import config
#code pour la simulation de la production
def SAM_production_prevision(day):
    """
    This function is used to calculate the SAM's production forecast for a given day.
    The formula is based on the data from the previous 10 days.
    """
    day=pd.to_datetime(day, format='%d %m') 

    target_day=day
    end_day = day + pd.Timedelta(days=config.FORECAST_DAYS-1)


    df = pd.read_csv('data/resultatsimusam.csv',parse_dates=['Time stamp'])
    # on modifie le format de la date pour être plus facilement exploitable

    #changement du format de la date en string au format %d %m
    df['Time stamp'] = pd.to_datetime(df['Time stamp'], format='%b %d, %I:%M %p').dt.strftime('%d %m')
    #changement du format de la date en datetime
    df['Time stamp'] = pd.to_datetime(df['Time stamp'], format='%d %m')
    
    # Créez un masque pour sélectionner les données entre la date cible et la date de fin (incluses)
    mask = ((df['Time stamp'] >= target_day) & (df['Time stamp'] <= end_day))
    

    # Appliquez le masque pour obtenir un sous-ensemble du DataFrame contenant uniquement les données entre la date cible et la date de fin
    filtered_data = np.array(df.loc[mask]['System power generated | (kW)'].tolist())*1000 #on multiplie par 1000 pour avoir l'énergie en Wh
    print(filtered_data)
    #dans le cas où on execute la fonction pour la tester on montre le graphe de production donc on sort la liste des trois jours
    if __name__=="__main__":
        return filtered_data

    #on sort une liste des données pour chaque jour avec un pas de 24h séparé en plusieurs sous listes pour chaque jour
    sublist_size = 24
    #liste python d'array numpy
    sublists = [filtered_data[i:i+sublist_size] for i in range(0, len(filtered_data), sublist_size)]
    return sublists
    
    
    


if __name__ == "__main__":
    jour=28
    mois=2
    day=str(jour)+" "+str(mois)

    filtered_data=SAM_production_prevision(day)
    print(filtered_data)
    plt.plot(filtered_data)
    plt.show()