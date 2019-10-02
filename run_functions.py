from open_functions import *

#Printing a few details from info retrieved using requests and json
print(retrieve_data['result']['country'], '- Country')
print(retrieve_data['result']['primary_care_trust'], '- NHS')
print(retrieve_data['result']['longitude'], '- Longitude')
print(retrieve_data['result']['latitude'], '- Latitude')

# Initiating txt
# file = open('postcode.txt', 'w')

list_order = ['Country: England', 'Primary Care Trust: Ealing', 'Longitude: -0.382433', 'Latitude: 51.497303']
for item in list_order:
    write_to_file('postcode.txt', item)
