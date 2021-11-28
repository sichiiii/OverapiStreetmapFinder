from xlsxwriter.workbook import Workbook
from map import Overpy_map
import app_logger

class Excel():
    def __init__(self) -> None:
        self.logger = app_logger.get_logger(__name__)

    def insert_data(self, filename, dict):
        try:
            wb = Workbook(f'/home/jabka/python/{filename}.xlsx')
            worksheet = wb.add_worksheet()
            fields = ["№", "адрес", "индекс", "область, город", "ссылка", "страна"]
            for i in range(0, 6):    
                worksheet.write(0, i, fields[i])
        except Exception as ex:
            self.logger.error('Error in excel file creating - ' + str(ex))

        try:
            count = 0
            for i, row in enumerate(dict): 
                if 'addr:street' in row.keys():
                    count+=1
                    worksheet.write(count+1, 0, count)
                    field = 'улица: '+ row['addr:street']
                    if 'addr:housenumber' in row.keys():
                        field += ' '+ row['addr:housenumber']
                    if 'building:levels' in row.keys():
                        field += ', количество этажей: ' + row['building:levels']
                    worksheet.write(count+1, 1, field)
                    if 'addr:city' in row.keys():
                        worksheet.write(count+1, 3, row['addr:city'])
                    if 'addr:postcode' in row.keys():
                        worksheet.write(count+1, 2, row['addr:postcode'])
                    if 'link' in row.keys():
                        worksheet.write(count+1, 4, row['link'])  
                    if 'addr:country' in row.keys():
                        worksheet.write(count+1, 5, row['addr:country'])    
            wb.close()
        except Exception as ex:
            self.logger.error('Error in inserting data - ' + str(ex))

ex = Excel()
om = Overpy_map()
aparts = om.get_apartments()

ex.insert_data('test1', aparts)
ex.insert_data('test', [{"адрес": 2, "индекс": 3, "область, город":4, "ссылка":56, "страна": 6 }, {"адрес": 752, "индекс": 3456, "область, город":4213, "ссылка":5631, "страна": 61 }])