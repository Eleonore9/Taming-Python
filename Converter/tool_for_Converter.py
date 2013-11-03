# Outil pour le convertisseur 04/10/2012.

# Function to extract the number to be converted from the raw_input"

def tool_convert(to_convert):
	"""Function to extract a number out of an string
	Takes in a string, returns a number"""
	liste = to_convert.split()
	for data in liste:
		try:
			num_data = float(data)
		except ValueError:
			pass
	return num_data
