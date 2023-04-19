import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import optimize,minimize_scalar
import config
#le paramètres à optimiser est l'import d'éléctricité dans la batterie
#cette fonction est appelé quand on réalise une optimisation avec une prévision météo de 1 jour.
def oneDim_minimize(f,current_battery_capacity):
    bounds=(0,config.BATTERY_CAPACITY-current_battery_capacity)
    result = minimize_scalar(f, bounds=bounds, method='bounded')
    print(result)
    return result.x

def multDim_minimise(f):
    bounds = optimize.Bounds([0] * config.FORECAST_DAYS, [np.inf] * config.FORECAST_DAYS)
    x0 = np.ones(config.FORECAST_DAYS)

    result = optimize.minimize(f, x0, method='L-BFGS-B', bounds=bounds,)
    return result.x


if __name__ == "__main__":
    #x est la variable à minimiser

    # Fonction test à minimiser
    def f(x):
        return x**2+2*x+1+np.sin(2*np.pi*x)*np.cos(2*np.pi*x)
    x0=12
    x_min=oneDim_minimize(f)
    
    print(f"Minimum de la fonction atteint à x = {x_min}")
    print(f"Valeur minimale de la fonction = {f(x_min)}")

    # Tracer la fonction
    x_range = np.linspace(-5, 5, 100)
    y_range = f(x_range)
    fig, ax = plt.subplots()
    ax.plot(x_range, y_range)
    ax.plot(x_min, f(x_min), 'ro')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Fonction à minimiser')
    plt.show()

