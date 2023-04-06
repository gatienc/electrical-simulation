import pandas as pd
from datetime import date
import config
#code pour la simulation de la production
def SAM_production_prevision(day):
    day=pd.to_datetime(day, format='%d %m') 

    target_day=day
    end_day = day + pd.Timedelta(days=config.FORECAST_DAYS)
    print("target_day",target_day)
    print("end_day",end_day)

    df = pd.read_csv('data/resultatsimusam.csv',parse_dates=['Time stamp'])
    # on modifie le format de la date pour être plus facilement exploitable
    df['Time stamp'] = pd.to_datetime(df['Time stamp'], format='%b %d, %I:%M %p').dt.strftime('%d %m')
    df['Time stamp'] = pd.to_datetime(df['Time stamp'], format='%d %m')
    
    # Créez un masque pour sélectionner les données entre la date cible et la date de fin (incluses)
    mask = ((df['Time stamp'] >= target_day) & (df['Time stamp'] <= end_day))
    

    # Appliquez le masque pour obtenir un sous-ensemble du DataFrame contenant uniquement les données entre la date cible et la date de fin
    filtered_data = df.loc[mask]

    print(filtered_data)
    
    
    


if __name__ == "__main__":
    jour=28
    mois=2
    day=str(jour)+" "+str(mois)

    SAM_production_prevision(day)