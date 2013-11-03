# fonctions pour conversions utiles
# le 03/10/2012

#Distances
def miles_to_km(miles):
	return float(miles) * 1.609344

def km_to_miles(km):
	return float(km) / 1.609344

def inches_to_cm(inches):
	return float(inches) * 2.54

def cm_to_inches(cm):
	return float(cm) / 2.54


#Temperatures
def fahrenheit_to_celsius(fah):
	return float(fah) * 0.6 - 17.7

def celsius_to_fahrenheit(cel):
	return float(cel) * 1.8 + 32


#Change
def dollar_to_euro(dollar):
	return float(dollar) * 0.77

def euro_to_dollar(euro):
	return float(euro) * 1.29


