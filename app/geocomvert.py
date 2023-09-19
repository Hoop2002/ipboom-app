import io
import datetime
import pandas as pd 
from geopy.geocoders import Yandex


def geo_convert(api_key: str, file: bytes):
    
    dataframe = pd.read_csv(io.StringIO(file.decode("windows-1251")))
    
    try:
        geolocator = Yandex(api_key=api_key)
    except:
        pass
    
    for i in dataframe.values:
       contract_number = i[0]
       unrestricted_value = i[6]
       latitude = float
       longitude = float

       try:
          g = geolocator.geocode(u'{unrestricted_value}'.format(unrestricted_value=unrestricted_value))
          latitude = g.latitude
          longitude = g.longitude
       except Exception as er:
           print(er)

        