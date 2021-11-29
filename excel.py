from xlsxwriter.workbook import Workbook
from map import Overpy_map
import app_logger, os

class Excel():
    def __init__(self) -> None:
        self.logger = app_logger.get_logger(__name__)
        self.om = Overpy_map()

    def insert_data(self, filename, count, country):
        try:
            aparts = self.om.get_apartments(count, country)
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

