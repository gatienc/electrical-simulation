# Description: Configuration file for the electrical simulation

# Simulation parameters
LATITUDE=48.53
LONGITUDE=7.72
HOURLY="temperature_2m,direct_radiation_instant"
FORECAST_DAYS=1 # between 1 and 7 (augment the time of the simulation)

# solar panel parameters
PANEL_AREA=1.65

# electricity consumption
CONSUMPTION_EXPECTED=27000 # Wh/day

# electricity price

OFFPEAK_PRICE=0.1672
FULL_PRICE=0.2285
EXPORT_PRICE=0


# offpeak_hours

OFFPEAK_HOURS=[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]# offpeak from 23h to 7h

# battery parameters
BATTERY_CAPACITY=13000# Wh

# minimization precisio
MAX_ITER=30