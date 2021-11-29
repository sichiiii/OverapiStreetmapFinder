import overpy
import app_logger


class Overpy_map():
    def __init__(self) -> None:
        self.logger = app_logger.get_logger(__name__)

    def get_apartments(self):
        try:
            api = overpy.Overpass()
            r = api.query("""[maxsize:1073741824][timeout:600]; area["ISO3166-2"="FR-75"]->.country;
      
      ( 
        way(area.country)
      
        [building=apartments][~"addr:postcode"~"."][~"addr:street"~"."];
      );
      out body 10;
      >;
      out meta qt ;
      """)
            arr = []
            res = r.ways
            for temp in range(0, 10):

                try:
                # https://www.google.com/maps/place/12+Vla+d'Est%C3%A9,+75013+Paris/@48.8221615,2.3648274,17z/data=!3m1!4b1!4m5!3m4!1s0x47e67229a6ca577f:0xc13c63b0b6802c32!8m2!3d48.8221615!4d2.3670161
                    res[temp].tags['link'] = f"""https://www.google.com/maps/place/{res[temp].tags['addr:housenumber']}+{
                    res[temp].tags['addr:street']}+{res[temp].tags['addr:postcode']}+{res[temp].tags['addr:city']}/@{
                    res[temp].nodes[2].lat},{res[temp].nodes[2].lon},17z/"""
                    res[temp].tags['link'] = res[temp].tags['link'].replace(' ', '+')
                    arr.append(res[temp].tags)
                    print(res[temp].tags['link'] )
                except Exception as ex:
                    continue
            print(arr)

            return arr
        except Exception as ex:
            self.logger.error('API Query error - ' + str(ex))
