import app_logger
import overpy
import time
import sys
import os
import re

from xlsxwriter.workbook import Workbook


class Overpy_map():
    def __init__(self, states, buildings) -> None:
        self.logger = app_logger.get_logger(__name__)
        self.ex = Excel()
        self.states = states
        self.buildings = buildings

    def get_apartments(self):
        try:
            try:
                api = overpy.Overpass()
                res = []
                for state in self.states:
                    count = 1
                    for building in self.buildings:
                        while 1:
                            try:
                                r = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-2"="{state}"]->.country; 
                                ( 
                                    way(area.country)

                                    [building={building}][~"addr:postcode"~"."][~"addr:street"~"."][~"addr:housenumber"~"."];
                                );
                                out body;
                                >;
                                out meta qt;
                                """)
                                res.extend(r.ways)
                                break
                            except:
                                time.sleep(60)
                                pass
                        time.sleep(60)
                        print(f'{count}/{len(self.buildings)} for {state}')
                        count += 1
                    print(f'Сборка {state} завершена')
                    print('Запись в эксель...')

                    arr = []
                    temp = 0
                    for j in range(0, len(res)):
                        try:
                            res[temp].tags[
                                'link'] = f"""https://www.google.com/maps/place/{res[temp].tags['addr:housenumber']}+{
                            res[temp].tags['addr:street']}+{res[temp].tags['addr:postcode']}+{res[temp].tags['addr:city']}/@{
                            res[temp].nodes[2].lat},{res[temp].nodes[2].lon},17z/"""
                            res[temp].tags['link'] = res[temp].tags['link'].replace(' ', '+')
                            arr.append(res[temp].tags)
                        except:
                            res[temp].tags['link'] = 'None'
                        temp += 1

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
            wb = Workbook(os.path.dirname(os.path.abspath(__file__)) + f'/results/{filename}.xlsx')
            worksheet = wb.add_worksheet()
            fields = ["№", "адрес", "индекс", "область, город", "ссылка", "страна", 'тип здания']
            for i in range(0, 7):
                worksheet.write(0, i, fields[i])
        except Exception as ex:
            self.logger.error('Error in excel file creating - ' + str(ex))

        try:
            counter = 0
            added = []
            for i, row in enumerate(aparts):

                if ('addr:street' in row.keys()) and ('addr:housenumber' in row.keys()):
                    re_str = re.compile(
                        "^.*?(?P<address>([A-Za-z]{1,30}\s*\.?){1,5}).*?\s*(?P<num>\d+)\s*(?P<symbol>.*?)$")
                    re_found = re_str.search(row['addr:street']+ ' ' + row['addr:housenumber'])
                    if re_found is not None:
                        try:
                            address = re_found.group('address')
                            try:
                                num = re_found.group('num')
                                address += ' ' + num
                                try:
                                    symbol = re_found.group('symbol')
                                    address += symbol
                                except:
                                    pass
                            except:
                                pass
                            if (len(address) > 6) and (address not in added) and (row['addr:postcode'] not in added):
                                counter += 1
                                worksheet.write(counter + 1, 0, counter)
                                worksheet.write(counter + 1, 1, address)
                                if len(str(row['addr:postcode'])) > 3:
                                    worksheet.write(counter + 1, 2, row['addr:postcode'])
                                else:
                                    worksheet.write(counter + 1, 2, ("0" + row['addr:postcode']))
                                worksheet.write(counter + 1, 3, row['addr:city'])
                                worksheet.write(counter + 1, 4, row['link'])
                                worksheet.write(counter + 1, 5, 'Georgia')
                                if 'building' in row.keys():
                                    worksheet.write(counter + 1, 6, row['building'])

                                added.append(address)
                                added.apppend(row['addr:postcode'])
                        except:
                            pass
            wb.close()
        except Exception as ex:
            self.logger.error('Error in inserting data - ' + str(ex))


if __name__ == '__main__':
    allowed_states = ['GE-AB', 'GE-AJ', 'GE-GU', 'GE-IM', 'GE-KA', 'GE-KK', 'GE-MM', 'GE-RL', 'GE-SZ', 'GE-SJ', 'GE-TB', 'GE-SK']
    allowed_building = ['apartments', 'house', 'bungalow', 'cabin', 'dormitory', 'farm', 'ger', 'hotel', 'houseboat',
                        'residential', 'semidetached_house', 'static_caravan', 'terrace']
    print('Начало операции')
    if '-s' in sys.argv:
        states = []
        index = sys.argv.index('-s') + 1
        while index < len(sys.argv):
            region = sys.argv[index]
            if region in allowed_states:
                states.append(region)
            index += 1
    else:
        states = allowed_states

    if '-b' in sys.argv:
        index = sys.argv.index('-b') + 1
        while index < len(sys.argv):
            building = sys.argv[index]
            if building in allowed_building:
                allowed_building.remove(building)
            index += 1

    om = Overpy_map(states, allowed_building)
    om.get_apartments()
    print('Конец операции')
