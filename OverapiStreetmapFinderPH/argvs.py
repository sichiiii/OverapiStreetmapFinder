import app_logger, overpy, os, sys, time

from xlsxwriter.workbook import Workbook


class Overpy_map():
    def __init__(self, states, buildings) -> None:
        self.logger = app_logger.get_logger(__name__)
        self.ex = Excel()
        self.states = states
        self.buildings = buildings

    def get_apartments(self) -> None:
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
            for i, row in enumerate(aparts):
                if 'addr:street' in row.keys():
                    counter += 1
                    field = ''
                    worksheet.write(counter + 1, 0, counter)
                    field = row['addr:street']
                    if 'addr:housenumber' in row.keys():
                        field += ' ' + row['addr:housenumber']
                    worksheet.write(counter + 1, 1, field)
                    if 'addr:city' in row.keys():
                        worksheet.write(counter + 1, 3, row['addr:city'])
                    if 'addr:postcode' in row.keys():
                        worksheet.write(counter + 1, 2, row['addr:postcode'])
                    if 'link' in row.keys():
                        worksheet.write(counter + 1, 4, row['link'])
                    worksheet.write(counter + 1, 5, 'Philippines')
                    if 'building' in row.keys():
                        worksheet.write(counter + 1, 6, row['building'])
            wb.close()
        except Exception as ex:
            self.logger.error('Error in inserting data - ' + str(ex))


if __name__ == '__main__':
    allowed_states = ['PH-00', 'PH-01', 'PH-02', 'PH-03', 'PH-05', 'PH-07', 'PH-08', 'PH-09', 'PH-10', 'PH-11',
                      'PH-12', 'PH-13', 'PH-14', 'PH-15', 'PH-40', 'PH-41']
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
