from GetLongitudeAndLatitude import getLogitudeAndLatitude

def start(URL, save_path):
    getLogitudeAndLatitude(XMLURL, save_path)



if __name__ == "__main__":
    from config import XMLURL
    import os
    save_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'outputdata')
    save_file_path = os.path.join(save_path, 'LatitudeAndLongitude.json')
    print("The output file will be saved at:")
    print(save_file_path)
    start(XMLURL, save_file_path)