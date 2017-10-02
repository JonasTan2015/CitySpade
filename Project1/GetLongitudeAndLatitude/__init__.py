
from GeocodingAPI import geocoding
from ReadXML import requestXML
import json
from collections import OrderedDict

def getLogitudeAndLatitude(XMLURL, save_path):
    address_list = requestXML(XMLURL)
    with open(save_path, 'a') as outfile:
        outfile.write('[\n')
        for address in address_list:
            append_address = address.get('StreetAddress', '')
            append_address += ','
            append_address += address.get('City', '')
            append_address += ','
            append_address += address.get('State', '')
            append_address += ','
            append_address += address.get('Zip', '')

            geolocation = geocoding(append_address)
            dict = OrderedDict({'UnitNumber': address.get('UnitNumber', ''),
                    'StreetAddress': address.get('StreetAddress', ''),
                    'City': address.get('City', ''),
                    'State': address.get('State', ''),
                    'Zip': address.get('Zip', ''),
                    'Longitude': geolocation.get('lng', '')})
            outfile.write(json.dumps(dict))
            outfile.write(',\n')
        outfile.write(']')


