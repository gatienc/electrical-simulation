import config
import pandas as pd
from production_prevision import SAM_production_prevision
from energy_consumption_previson import consumption_prevision
from scipy import optimize
import numpy as np

# def main():
#     daily_importation=[None]*config.FORECAST_DAYS
#     day="28/12"

#     #variable to optimize
#     best_daily_importation=[None]*config.FORECAST_DAYS
#     best_daily_importation=(daily_importation,day,best_daily_importation)



def price_simulation(daily_importation,battery_power_start,target_day):
    daily_production=SAM_production_prevision(target_day)
    battery_power=battery_power_start
    daily_export=[0]*config.FORECAST_DAYS
    daily_full_peak_import=[0]*config.FORECAST_DAYS

    #variable to optimize
    for day in range(config.FORECAST_DAYS):

        production=daily_production[day]
        consumption=consumption_prevision(config.CONSUMPTION_EXPECTED)


        # à minuit on recharge la batterie de la valeur donnée dans daily_importation (la valeur à optimiser)
        # puis on calcule l'importation en heure pleine qui aura était necessaire pour enfin calculer le cout totale de l'importation éléctrique
        # on simule l'état de charge de la batterie au cours de la journée avec un pas de 1h. on calcule dedans l'energie importée et l'energie perdue
        

        battery_power = min(battery_power + daily_importation[day], config.BATTERY_CAPACITY)


        for i in range(24):
            
            temp_battery_power=battery_power+production[i]-consumption[i]

            if temp_battery_power>config.BATTERY_CAPACITY:
                #the battery is more than full
                temp_battery_power=config.BATTERY_CAPACITY
                daily_export[day]+=temp_battery_power-config.BATTERY_CAPACITY


            elif temp_battery_power<0:
                #the battery is empty
                daily_full_peak_import[day]+=-temp_battery_power
                temp_battery_power=0
            else:
                battery_power=temp_battery_power

    return energetic_price(sum(daily_importation),sum(daily_full_peak_import),sum(daily_export))
    
def energetic_price(off_peak_import,full_peak_import,export):
    cost=(off_peak_import*config.OFFPEAK_PRICE+full_peak_import*config.FULL_PRICE-export*config.EXPORT_PRICE)/1000
    return cost

if __name__ == "__main__":
    jour=28
    mois=2
    target_day=str(jour)+" "+str(mois)
    daily_importation=[0]*config.FORECAST_DAYS #en Wh
    daily_importation=[12575.02204915,  6116.67064995,  2695.85427718]
    battery_power_start=0 #en Wh
    cost=price_simulation(daily_importation,battery_power_start,target_day)
    print("coût en euro pour les %d prochains jours avec comme import journaliers: "%(config.FORECAST_DAYS))
    print(daily_importation)
    print("{:.2f}€".format(cost))

    bounds = optimize.Bounds([0] * config.FORECAST_DAYS, [np.inf] * config.FORECAST_DAYS)
    x0 = np.ones(config.FORECAST_DAYS)
    result = optimize.minimize(price_simulation, x0, method='L-BFGS-B', bounds=bounds,args=(battery_power_start,target_day))
    print(result)
    result.x


