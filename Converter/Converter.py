# -*- coding=UTF-8 -*-
# fichier convertisseur 04/10/2012

import time

from Convertions import miles_to_km 
from Convertions import km_to_miles
from Convertions import inches_to_cm 
from Convertions import cm_to_inches
from Convertions import fahrenheit_to_celsius 
from Convertions import celsius_to_fahrenheit
from Convertions import dollar_to_euro
from Convertions import euro_to_dollar

from tool_for_Converter import tool_convert

def converter():
	print """> This is a converter: \n *from miles to km and from km to miles
 	*from inches to cm and from cm to inches
 	*from fahrenheit degrees to celsius degrees and vice versa
 	*from $ to euro and from euro to $."""
	time.sleep(1.5)
	print "> Please enter the data you wish to convert or type 'exit' to quit \n (ex: 2 miles or 65 °F):"
	converter = True
	while converter:
		convert = raw_input(" ")
		if convert == "exit":
			converter = False
		else:
			for_convertion = tool_convert(convert)

			if "miles" in convert or "mile" in convert:
				print "%s are equivalent to %f km" % (convert, miles_to_km(for_convertion))

			elif "km" in convert:
				print "%s are equivalent to %f miles" % (convert, km_to_miles(for_convertion))

			elif "inches" in convert or "inch" in convert:
				print "%s are equivalent to %f cm" % (convert, inches_to_cm(for_convertion))

			elif "cm" in convert:
				print "%s are equivalent to %f inches" % (convert, cm_to_inches(for_convertion))

			elif "fahrenheit" in convert or "°F" in convert:
				print "%s are equivalent to %f celsius degrees" % (convert, fahrenheit_to_celsius(for_convertion))

			elif "celsius" in convert or "°C" in convert:
				print "%s are equivalent to %f fahrenheit degrees" % (convert, celsius_to_fahrenheit(for_convertion))

			elif "$" in convert or "dollar" in convert:
				print "%s are equivalent to %f euro" % (convert, dollar_to_euro(for_convertion))

			elif "€" in convert or "euro" in convert:
				print "%s are equivalent to $ %f" % (convert, euro_to_dollar(for_convertion))


			else:
				print "Invalid data input!"

if __name__ == "__main__":
	converter()
