import requests, json, time

'''
taking a street address in the format used by the national postal service, a Google API key, and a time delay in seconds as parameters
'''
def geocoding(address, key="", delay=0):
    urlBase = "https://maps.googleapis.com/maps/api/geocode/json"
    urlAddr = "?address=" + address.replace(" ", "+")
    urlKey = "&key=" + key
    url = urlBase + urlAddr + urlKey
    response = requests.get(url)
    jsonDict = response.json()
    # jsonDict = json.loads(jsonRaw)
    if jsonDict['status'] == 'OK':
        addr = jsonDict['results'][0]['formatted_address']
        lat = jsonDict['results'][0]['geometry']['location']['lat']
        lng = jsonDict['results'][0]['geometry']['location']['lng']
    else:
        addr = 'N/A'
        lat = 'N/A'
        lng = 'N/A'
    time.sleep(delay)
    # returning a dictionary of the formatted address, the latitude, and the longitude
    return {'addr': addr, 'lat': lat, 'lng': lng}  # testing

