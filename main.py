import config
import pandas as pd
#variables init


df = pd.read_csv('data/resultatsimusam.csv')
print(df)

#
## pour l'instant on simule la production sur un jour seulement pour tester, on étendra ensuite à plusieurs jours


def cost_function():
    daily_production=production_prevision()

    #on simule l'état de charge de la batterie au cours de la journée avec un pas de 1h. on calcule dedans l'energie importée et l'energie perdue
    for i in range(24):

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
        return