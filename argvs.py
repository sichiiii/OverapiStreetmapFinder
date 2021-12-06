import argparse, app_logger, overpy, os
from xlsxwriter.workbook import Workbook
import random
import time

class Overpy_map():
  def __init__(self) -> None:
      self.logger = app_logger.get_logger(__name__)

  def get_apartments(self, count, country):
    try:
        api = overpy.Overpass()
        r = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-1"="{country}"]->.country;
        
        ( 
            way(area.country)
        
            [building=apartments][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
        );
        out body;
        >;
        out meta qt ;
        """)
        time.sleep(60)
        r_house = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-1"="{country}"]->.country;
        
        ( 
            way(area.country)
        
            [building=house][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
        );
        out body;
        >;
        out meta qt ;
        """)
        time.sleep(60)

        r_bungalow = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-1"="{country}"]->.country;
        ( 
            way(area.country)
        
            [building=bungalow][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
        );
        out body;
        >;
        out meta qt ;
        """)
        time.sleep(60)

        r_cabin = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-1"="{country}"]->.country;
        ( 
            way(area.country)
        
            [building=cabin][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
        );
        out body;
        >;
        out meta qt ;
        """)
        time.sleep(60)

        r_detached = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-1"="{country}"]->.country;
        ( 
            way(area.country)
        
            [building=cabin][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
        );
        out body;
        >;
        out meta qt ;
        """)
        time.sleep(60)

        r_dormitory = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-1"="{country}"]->.country;
        ( 
            way(area.country)
        
            [building=dormitory][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
        );
        out body;
        >;
        out meta qt ;
        """)
        time.sleep(60)

        r_farm = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-1"="{country}"]->.country;
        ( 
            way(area.country)
        
            [building=farm][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
        );
        out body;
        >;
        out meta qt ;
        """)
        time.sleep(60)

        r_ger = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-1"="{country}"]->.country;
        ( 
            way(area.country)
        
            [building=ger][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
        );
        out body;
        >;
        out meta qt ;
        """)
        time.sleep(60)

        r_hotel = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-1"="{country}"]->.country;
        ( 
            way(area.country)
        
            [building=hotel][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
        );
        out body;
        >;
        out meta qt ;
        """)
        time.sleep(60)

        r_houseboat = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-1"="{country}"]->.country;
        ( 
            way(area.country)
        
            [building=houseboat][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
        );
        out body;
        >;
        out meta qt ;
        """)
        time.sleep(60)

        r_residental = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-1"="{country}"]->.country;
        ( 
            way(area.country)
        
            [building=residental][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
        );
        out body;
        >;
        out meta qt ;
        """)
        time.sleep(60)

        r_semidetached_house = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-1"="{country}"]->.country;
        ( 
            way(area.country)
        
            [building=semidetached_house][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
        );
        out body;
        >;
        out meta qt ;
        """)
        time.sleep(60)

        r_static_caravan = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-1"="{country}"]->.country;
        ( 
            way(area.country)
        
            [building=static_caravan][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
        );
        out body;
        >;
        out meta qt ;
        """)
        time.sleep(60)

        r_terrace = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-1"="{country}"]->.country;
        ( 
            way(area.country)
        
            [building=	terrace][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
        );
        out body;
        >;
        out meta qt ;
        """)
        time.sleep(60)

        arr = [] 
        res = r.ways
        res.extend(r_bungalow.ways)
        res.extend(r_detached.ways)
        res.extend(r_cabin.ways)
        res.extend(r_farm.ways)
        res.extend(r_ger.ways)
        res.extend(r_hotel.ways)
        res.extend(r_houseboat.ways)
        res.extend(r_residental.ways)
        res.extend(r_semidetached_house.ways)
        res.extend(r_static_caravan.ways)
        res.extend(r_terrace.ways)
        
        
        random.shuffle(res)
        temp = 0
        for i in range(0, len(res)):
            try:
                # https://www.google.com/maps/place/12+Vla+d'Est%C3%A9,+75013+Paris/@48.8221615,2.3648274,17z/data=!3m1!4b1!4m5!3m4!1s0x47e67229a6ca577f:0xc13c63b0b6802c32!8m2!3d48.8221615!4d2.3670161
                res[temp].tags['link'] = f"""https://www.google.com/maps/place/{res[temp].tags['addr:housenumber']}+{
                res[temp].tags['addr:street']}+{res[temp].tags['addr:postcode']}+{res[temp].tags['addr:city']}/@{
                res[temp].nodes[2].lat},{res[temp].nodes[2].lon},17z/"""
                res[temp].tags['link'] = res[temp].tags['link'].replace(' ', '+')
                arr.append(res[temp].tags)
                temp +=1
                print(res[temp].tags['link'])
            except Exception as ex:
                print(temp)
                continue
        print(arr)
        return arr
    except Exception as ex:
        self.logger.error('API Query error - ' + str(ex))

class Excel():
    def __init__(self) -> None:
        self.logger = app_logger.get_logger(__name__)

    def insert_data(self, aparts, filename):
        try:
            wb = Workbook(os.path.dirname(os.path.abspath(__file__)) + '/results/' + filename + '/' +f'{filename}.xlsx')  #добавить создание нового файла
            worksheet = wb.add_worksheet()
            fields = ["№", "адрес", "индекс", "область, город", "ссылка", "страна"]
            for i in range(0, 6):    
                worksheet.write(0, i, fields[i])
        except Exception as ex:
            self.logger.error('Error in excel file creating - ' + str(ex))

        try:
            counter = 0
            for i, row in enumerate(aparts): 
                if 'addr:street' in row.keys():
                    counter+=1
                    worksheet.write(counter+1, 0, counter)
                    field = 'улица: '+ row['addr:street']
                    if 'addr:housenumber' in row.keys():
                        field += ' '+ row['addr:housenumber']
                    if 'building:levels' in row.keys():
                        field += ', количество этажей: ' + row['building:levels']
                    worksheet.write(counter+1, 1, field)
                    if 'addr:city' in row.keys():
                        worksheet.write(counter+1, 3, row['addr:city'])
                    if 'addr:postcode' in row.keys():
                        worksheet.write(counter+1, 2, row['addr:postcode'])
                    if 'link' in row.keys():
                        worksheet.write(counter+1, 4, row['link'])  
                    worksheet.write(counter+1, 5, country)    
            wb.close()
        except Exception as ex:
            self.logger.error('Error in inserting data - ' + str(ex))

parser = argparse.ArgumentParser()
parser.add_argument('--count', action='store', type=int,
                    dest='count', help='количество')
parser.add_argument('--country', action='store',
                    dest='country', help='страна')

args = parser.parse_args()
print(args.count, args.country)

country = args.country.upper()
count = args.count
print(country)

known_countries = ['FR', 'AU', 'AT', 'NZL']
if country not in known_countries:
    print('Некорректная страна')
    exit()

ex = Excel()
om = Overpy_map()

aparts = om.get_apartments(count, country)
ex.insert_data(aparts, country)