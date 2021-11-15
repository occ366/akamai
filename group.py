from urllib.parse import urljoin

class group:
  
  def get(self,connection,baseurl):
    return conection.get(urljoin(baseurl, '/papi/v1/groups'))
  
   
