import requests
import xml.etree.ElementTree as ET



def requestXML(URL):
    response = requests.get(URL).text
    xml_response = response.encode('ascii', 'ignore')
    xml_tree = ET.ElementTree(ET.fromstring(xml_response))
    # parse the locations
    locations = xml_tree.findall('//Location')
    result = []
    for location in locations:
        address = {}
        for node in location.getiterator():
            if node.tag == 'StreetAddress':
                address['StreetAddress'] = node.text
            elif node.tag == 'UnitNumber':
                address['UnitNumber'] = node.text
            elif node.tag == 'City':
                address['City'] = node.text
            elif node.tag == 'State':
                address['State'] = node.text
            elif node.tag == 'Zip':
                address['Zip'] = node.text
        result.append(address)
    return result




