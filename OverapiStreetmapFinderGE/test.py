
import re

addr = 'ხუნდაძის ქუჩა (Khundadze St) 34'
re_str = re.compile(
                        "^.*?(?P<address>([A-Za-z]{1,30}\s*\.?){1,5}).*?\s*(?P<num>\d+)\s*(?P<symbol>.*?)$")
re_found = re_str.search(addr)
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
            print(address)
        except:
            pass
    except:
        pass