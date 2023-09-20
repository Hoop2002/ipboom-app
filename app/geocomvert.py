import io
import os
import csv
import time
import datetime
import pandas as pd 
from geopy.geocoders import Yandex


def geo_convert(api_key: str, file: bytes):
    
    dataframe = pd.read_csv(io.StringIO(file.decode("windows-1251")))
    
    try:
        geolocator = Yandex(api_key=api_key)
    except Exception as err:
        print(err)
    
    new_data = []
    file_name = "record_{date_time}.csv".format(date_time=datetime.datetime.today())
    file_path = os.path.abspath("src/result_files/{f}".format(f=file_name))
    columns = [u"Широта", u"Долгота", u"Описание", u"Подпись", u"Номер"]
    
    with open(file_path, "a", newline="") as some_file:
        writer_csv = csv.DictWriter(some_file, fieldnames=columns)
        writer_csv.writeheader()


        num = 0
        
        for i in dataframe.values:
            num += 1
            contract_number = i[0]
            unrestricted_value = i[6]
            latitude = float
            longitude = float
            try:
                g = geolocator.geocode(u'{unrestricted_value}'.format(unrestricted_value=unrestricted_value))
                latitude = g.latitude
                longitude = g.longitude
                
                new_data.append({
                    u"Широта": latitude,
                    u"Долгота":longitude,
                    u"Описание": contract_number,
                    u"Подпись": u" ",
                    u"Номер": num
                })

            except Exception as er:
                print(er)

                time.sleep(4)

                g = geolocator.geocode(u'{unrestricted_value}'.format(unrestricted_value=unrestricted_value))
                latitude = g.latitude
                longitude = g.longitude
                
                new_data.append({
                    u"Широта": latitude,
                    u"Долгота":longitude,
                    u"Описание": contract_number,
                    u"Подпись": u" ",
                    u"Номер": num
                })
        
        writer_csv.writerows(new_data)
        new_data = []
        num = 0

        return file_name
        