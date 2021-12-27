import argparse, app_logger, overpy, os
from xlsxwriter.workbook import Workbook
import random
import time

class Overpy_map():
    def __init__(self) -> None:
        self.logger = app_logger.get_logger(__name__)
        self.ex = Excel()

    def get_apartments(self):
        try:
            state_arr = ['AU-NSW', 'AU-QLD', 'AU-SA', 'AU-TAS', 'AU-VIC', 'AU-WA', 'AU-ACT', 'AU-NT']
            for state in state_arr:
                try:
                    api = overpy.Overpass()
                    while 1:
                        try:
                            r = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-2"="{state}"]->.country; 
                            
                            ( 
                                way(area.country)
                            
                            
                                [building=apartments][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
                            );
                            out body;
                            >;
                            out meta qt;
                            """)
                            break
                        except: 
                            time.sleep(60)
                            pass

                    time.sleep(120)
                    print('!')
                    while 1:
                        try:
                            r_house = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-2"="{state}"]->.country;
                            
                            ( 
                                way(area.country)
                            
                                [building=house][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
                            );
                            out body;
                            >;
                            out meta qt ;
                            """)
                            break
                        except: 
                            time.sleep(60)
                            pass
                    time.sleep(120)
                    print('!')
                    while 1:
                        try:
                            r_bungalow = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-2"="{state}"]->.country;
                            ( 
                                way(area.country)
                            
                                [building=bungalow][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
                            );
                            out body;
                            >;
                            out meta qt ;
                            """)
                            break
                        except: 
                            time.sleep(60)
                            pass
                    time.sleep(120)
                    print('!')
                    while 1:
                        try:
                            r_cabin = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-2"="{state}"]->.country;
                            ( 
                                way(area.country)
                            
                                [building=cabin][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
                            );
                            out body;
                            >;
                            out meta qt ;
                            """)
                            break
                        except: 
                            time.sleep(60)
                            pass
                    time.sleep(120)
                    print('!')
                    while 1:
                        try:
                            r_detached = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-2"="{state}"]->.country;
                            ( 
                                way(area.country)
                            
                                [building=cabin][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
                            );
                            out body;
                            >;
                            out meta qt ;
                            """)
                            time.sleep(120)
                            break
                        except: 
                            time.sleep(60)
                            pass
                    print('!')
                    while 1:
                        try:
                            r_dormitory = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-2"="{state}"]->.country;
                            ( 
                                way(area.country)
                            
                                [building=dormitory][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
                            );
                            out body;
                            >;
                            out meta qt ;
                            """)
                            break
                        except: 
                            time.sleep(60)
                            pass
                    time.sleep(120)
                    print('!')
                    while 1:
                        try:
                            r_farm = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-2"="{state}"]->.country;
                            ( 
                                way(area.country)
                            
                                [building=farm][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
                            );
                            out body;
                            >;
                            out meta qt ;
                            """)
                            break
                        except: 
                            time.sleep(60)
                            pass
                    time.sleep(120)
                    print('!')
                    while 1:
                        try:
                            r_ger = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-2"="{state}"]->.country;
                            ( 
                                way(area.country)
                            
                                [building=ger][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
                            );
                            out body;
                            >;
                            out meta qt ;
                            """)
                            break
                        except: 
                            time.sleep(60)
                            pass
                    time.sleep(120)
                    print('!')
                    while 1:
                        try:
                            r_hotel = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-2"="{state}"]->.country;
                            ( 
                                way(area.country)
                            
                                [building=hotel][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
                            );
                            out body;
                            >;
                            out meta qt ;
                            """)
                            break
                        except: 
                            time.sleep(60)
                            pass
                    time.sleep(120)
                    print('!')
                    while 1:
                        try:
                            r_houseboat = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-2"="{state}"]->.country;
                            ( 
                                way(area.country)
                            
                                [building=houseboat][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
                            );
                            out body;
                            >;
                            out meta qt ;
                            """)
                            break
                        except: 
                            time.sleep(60)
                            pass
                    time.sleep(120)
                    print('!')
                    while 1:
                        try:
                            r_residental = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-2"="{state}"]->.country;
                            ( 
                                way(area.country)
                            
                                [building=residental][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
                            );
                            out body;
                            >;
                            out meta qt ;
                            """)
                            break
                        except: 
                            time.sleep(60)
                            pass
                    time.sleep(120)
                    print('!')
                    while 1:
                        try:
                            r_semidetached_house = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-2"="{state}"]->.country;
                            ( 
                                way(area.country)
                            
                                [building=semidetached_house][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
                            );
                            out body;
                            >;
                            out meta qt ;
                            """)
                            break
                        except: 
                            time.sleep(60)
                            pass
                    time.sleep(120)
                    print('!')
                    while 1:
                        try:
                            r_static_caravan = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-2"="{state}"]->.country;
                            ( 
                                way(area.country)
                            
                                [building=static_caravan][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
                            );
                            out body;
                            >;
                            out meta qt ;
                            """)
                            break
                        except: 
                            time.sleep(60)
                            pass
                    time.sleep(120)
                    print('!')
                    while 1:
                        try:
                            r_terrace = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-2"="{state}"]->.country;
                            ( 
                                way(area.country)
                            
                                [building=terrace][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
                            );
                            out body;
                            >;
                            out meta qt ;
                            """)
                            break
                        except: 
                            time.sleep(60)
                            pass
                    time.sleep(120)
                    print('!')
                    arr = [] 
                    res = r.ways
                    res.extend(r_bungalow.ways)
                    res.extend(r_house.ways)
                    res.extend(r_farm.ways)
                    res.extend(r_ger.ways)
                    res.extend(r_detached.ways)
                    res.extend(r_hotel.ways)
                    res.extend(r_dormitory.ways)
                    res.extend(r_houseboat.ways)
                    res.extend(r_residental.ways)
                    res.extend(r_semidetached_house.ways)
                    res.extend(r_static_caravan.ways)
                    res.extend(r_terrace.ways)
                    res.extend(r_cabin.ways)
                    self.logger.warning(res)
                    temp = 0
                    for j in range(0, len(res)):
                        try:
                            print(res[temp].tags)
                            # https://www.google.com/maps/place/12+Vla+d'Est%C3%A9,+75013+Paris/@48.8221615,2.3648274,17z/data=!3m1!4b1!4m5!3m4!1s0x47e67229a6ca577f:0xc13c63b0b6802c32!8m2!3d48.8221615!4d2.3670161
                            res[temp].tags['link'] = f"""https://www.google.com/maps/place/{res[temp].tags['addr:housenumber']}+{
                            res[temp].tags['addr:street']}+{res[temp].tags['addr:postcode']}+{res[temp].tags['addr:city']}/@{
                            res[temp].nodes[2].lat},{res[temp].nodes[2].lon},17z/"""
                            res[temp].tags['link'] = res[temp].tags['link'].replace(' ', '+')
                            arr.append(res[temp].tags)
                        except:
                            res[temp].tags['link'] = 'None'
                        temp +=1
                    print(arr)
                    self.ex.insert_data(arr, state)
                except Exception as ex:
                    self.logger.error('API Query error - ' + str(ex))
        except Exception as ex:
            self.logger.error('Loop error - ' + str(ex))

class Excel():
    def __init__(self) -> None:
        self.logger = app_logger.get_logger(__name__)

    def insert_data(self, aparts, filename):
        try:
            wb = Workbook(os.path.dirname(os.path.abspath(__file__)) + '/results/' + 'AUS' + '/' +f'{filename}.xlsx')  #добавить создание нового файла
            worksheet = wb.add_worksheet()
            fields = ["№", "адрес", "индекс", "область, город", "ссылка", "страна", 'тип здания']
            for i in range(0, 7):    
                worksheet.write(0, i, fields[i])
        except Exception as ex:
            self.logger.error('Error in excel file creating - ' + str(ex))

        try:
            counter = 0
            for i, row in enumerate(aparts): 
                if 'addr:street' in row.keys():
                    counter+=1
                    field = ''
                    worksheet.write(counter+1, 0, counter)
                    field = row['addr:street']
                    if 'addr:housenumber' in row.keys():
                        field += ' ' + row['addr:housenumber']
                    worksheet.write(counter+1, 1, field)
                    if 'addr:city' in row.keys():
                        worksheet.write(counter+1, 3, row['addr:city'])
                    if 'addr:postcode' in row.keys():
                        worksheet.write(counter+1, 2, row['addr:postcode'])
                    if 'link' in row.keys():
                        worksheet.write(counter+1, 4, row['link'])  
                    worksheet.write(counter+1, 5, 'France') 
                    if 'building' in row.keys():
                        worksheet.write(counter+1, 6, row['building'])  
            wb.close()
        except Exception as ex:
            self.logger.error('Error in inserting data - ' + str(ex))

om = Overpy_map()
aparts = om.get_apartments()
