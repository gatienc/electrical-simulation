import config
import pandas as pd
from production_prevision import SAM_production_prevision
from energy_consumption_previson import consumption_prevision
from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np

# def main():
#     daily_importation=[None]*config.FORECAST_DAYS
#     day="28/12"

#     #variable to optimize
#     best_daily_importation=[None]*config.FORECAST_DAYS
#     best_daily_importation=(daily_importation,day,best_daily_importation)

def price_simulation_without_solar_panel(battery_power_start,target_day):
    daily_production=SAM_production_prevision(target_day)

    battery_power=battery_power_start
    daily_hour_import=[0]*config.FORECAST_DAYS#importation qui a du être faites en heure journalières
    daily_importation=[0]*config.FORECAST_DAYS#importion à 00h00 en heure creuse

    for day in range(config.FORECAST_DAYS):
        production=daily_production[day]

        consumption=consumption_prevision(config.CONSUMPTION_EXPECTED)


        # à minuit on recharge la batterie au maximum
        # puis on calcule l'importation en heure pleine qui aura était necessaire pour enfin calculer le cout totale de l'importation éléctrique
        # on simule l'état de charge de la batterie au cours de la journée avec un pas de 1h. on calcule dedans l'energie importée au cours de la journée
        print(battery_power)
        daily_importation[day]=config.BATTERY_CAPACITY-battery_power
        battery_power = config.BATTERY_CAPACITY


        for i in range(24):
            
            temp_battery_power=battery_power+production[i]-consumption[i]
            if temp_battery_power>config.BATTERY_CAPACITY:
                #the battery is more than full
                temp_battery_power=config.BATTERY_CAPACITY
            elif temp_battery_power<0:
                #the battery is empty
                daily_hour_import[day]+=-temp_battery_power*config.OFFPEAK_PRICE if config.OFFPEAK_HOURS[i] else -temp_battery_power*config.FULL_PRICE
                temp_battery_power=0
            else:
                battery_power=temp_battery_power

    cost=(sum(daily_importation)*config.OFFPEAK_PRICE+sum(daily_hour_import))/1000
    return cost,daily_importation # return the cost of the importation
   


def price_simulation(daily_importation,battery_power_start,target_day):
    daily_production=SAM_production_prevision(target_day)
    battery_power=battery_power_start
    daily_export=[0]*config.FORECAST_DAYS
    daily_hour_import=[0]*config.FORECAST_DAYS

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
                daily_hour_import[day]+=-temp_battery_power*config.OFFPEAK_PRICE if config.OFFPEAK_HOURS[i] else -temp_battery_power*config.FULL_PRICE
                temp_battery_power=0
            else:
                battery_power=temp_battery_power

    return energetic_price(sum(daily_importation),sum(daily_hour_import),sum(daily_export))
    
def energetic_price(off_peak_import,daily_hour_peak_import,export):
    cost=(off_peak_import*config.OFFPEAK_PRICE+daily_hour_peak_import-export*config.EXPORT_PRICE)/1000
    return cost

if __name__ == "__main__":
    jour=28
    mois=2
    target_day=str(jour)+" "+str(mois)
    #calcul de la production avec aucune importation
    #daily_importation=[0]*config.FORECAST_DAYS #en Wh
    daily_importation=[0,0]

    battery_power_start=0 #en Wh

    cost=price_simulation(daily_importation,battery_power_start,target_day)
    print("coût en euro pour les %d prochains jours avec comme import journaliers: "%(config.FORECAST_DAYS))
    print(daily_importation)
    print("{:.2f}€".format(cost))
        
    cost,daily_importation=price_simulation_without_solar_panel(battery_power_start,target_day)
    print("coût en euro pour les %d prochains jours avec comme import journaliers: "%(config.FORECAST_DAYS))
    print(daily_importation)
    print("{:.2f}€".format(cost))


    #optimisation
    bounds = optimize.Bounds([0] * config.FORECAST_DAYS, [np.inf] * config.FORECAST_DAYS)
    x0 = np.ones(config.FORECAST_DAYS)
    options = {'maxiter': config.MAX_ITER}
    result = optimize.minimize(price_simulation, x0, method='L-BFGS-B', bounds=bounds,args=(battery_power_start,target_day),options=options)
    print(result.x)
    print("{:.2f}€".format(result.fun))

    #     x_values = np.linspace(0, 100, 100)
    # y_values = np.linspace(0, 100, 100)

    # # Créer une grille de points (X, Y) en utilisant les points x et y
    # X, Y = np.meshgrid(x_values, y_values)
    
    # Z = price_simulation([X,Y],battery_power_start,target_day)
    # # Créer un graphique 3D en utilisant Matplotlib
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')

    # # Tracer la surface en utilisant les valeurs X, Y et Z
    # ax.plot_surface(X, Y, Z)

    # ax.xlabel('import j1')
    # ax.ylabel('import j2')
    # ax.set_zlabel('prix en €')
    # ax.set_title('minimisation du prix en fonction des importations journalières')
    # # Afficher le graphique
    # plt.show()







