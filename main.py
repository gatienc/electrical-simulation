import config
import pandas as pd
#variables init


df = pd.read_csv('data/resultatsimusam.csv')
print(df)

#battery capacity in Wh
battery_power=[]

#daily photovoltaic production in Wh
production_=[]

#daily consumption in Wh
consumption=[]

#daily energy importation in Wh
importation=[]

#on calcule l'état réeel de la batterie au cours de la journée avec un pas de 1h
for i in range(24):
    #production_.append(production_prevision(i))
    #consumption.append(consuption_prevision(i))
    new_battery_power=battery_power[i-1]+production_[i]-consumption[i]
    battery_power.append(new_battery_power)
    if battery_power[i]/config.BATTERY_CAPACITY>1:
        #the battery is more than full
        importation.append(battery_power[i]-config.BATTERY_CAPACITY)
        battery_power[i]=config.BATTERY_CAPACITY
    elif battery_power[i]/config.BATTERY_CAPACITY<0:
        #the battery is empty
        importation.append(-battery_power[i])
        battery_power[i]=0