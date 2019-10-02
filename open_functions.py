import requests
import json

request_postcodes = requests.get('http://api.postcodes.io/postcodes/' + 'UB25QH')
retrieve_data = request_postcodes.json()
#print(retrieve_data)
#print(request_postcodes.content)


def write_to_file(file, postcode_item):
    try:
        with open(file, 'a') as opened_file:
            opened_file.write(postcode_item + '\n')
    except FileNotFoundError:
        print('File not found')



