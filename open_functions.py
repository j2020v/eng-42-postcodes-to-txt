import requests
import json

request_postcodes = requests.get('http://api.postcodes.io/postcodes/' + 'UB25QH')
retrieve_data = request_postcodes.json()
#print(retrieve_data)
#print(request_postcodes.content)

print(retrieve_data['result']['country'], '- Country')
print(retrieve_data['result']['primary_care_trust'], '- NHS')
print(retrieve_data['result']['longitude'], '- Longitude')
print(retrieve_data['result']['latitude'], '- Latitude')



def write_to_file(file):
    try:
        with open(file, 'w') as opened_file:
            opened_file.write('' + '\n')

            opened_file.close()
    except FileNotFoundError:
        print('File not found.')

