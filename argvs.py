import argparse, app_logger, overpy, os
from xlsxwriter.workbook import Workbook

class Overpy_map():
  def __init__(self) -> None:
      self.logger = app_logger.get_logger(__name__)

  def get_apartments(self, count, country):
    try:
      api = overpy.Overpass()
      r = api.query(f"""[maxsize:1073741824][timeout:600]; area["ISO3166-2"="{country}"]->.country;
      
      ( 
        way(area.country)
      
        [building=apartments][~"addr:postcode"~"."][~"addr:street"~"."];
      );
      out body {count};
      >;
      out meta qt ;
      """)
      
      arr = [] 
      res = r.ways
      for temp in range(0, 10):
          arr.append(res[temp].tags)
          res[temp].tags['link'] = f"https://www.google.com/maps/place/*/@{res[temp].nodes[2].lat},{res[temp].nodes[2].lon},21z/"
      print(arr)
      return arr
    except Exception as ex:
      self.logger.error('API Query error - ' + str(ex))

class Excel():
    def __init__(self) -> None:
        self.logger = app_logger.get_logger(__name__)

    def insert_data(self, aparts, filename):
        try:
            wb = Workbook(os.path.dirname(os.path.abspath(__file__)) + '/results/'+ f'{filename}.xlsx')
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
                    if 'addr:country' in row.keys():
                        worksheet.write(counter+1, 5, row['addr:country'])    
            wb.close()
        except Exception as ex:
            self.logger.error('Error in inserting data - ' + str(ex))

parser = argparse.ArgumentParser()
parser.add_argument('--count', action='store',
                    dest='count', help='количество')
parser.add_argument('--country', action='store',
                    dest='country', help='страна')

args = parser.parse_args()
print(args.count, args.country)

known_countries = ['FR-75']
if args.country not in known_countries:
    print('Некорректная страна')
    exit()

ex = Excel()
om = Overpy_map()

aparts = om.get_apartments(args.count, args.country)
ex.insert_data(aparts, 'file1')