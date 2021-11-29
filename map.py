import overpy
import app_logger

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