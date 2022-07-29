import unittest
import requests
from config import hostname,port

url_main = 'http://'+hostname+':'+str(port)
url_api = 'http://'+hostname+':'+str(port)+'/api'
class testEndpoints(unittest.Testcase):
    def test_get_main(self):
        r = requests.get(url_main)
        self.assertEqual(r.status_code,200)
    def test_get_api(self):
        r = requests.get(url_api)
        self.assertEqual(r.status_code,200)
    def test_post_api(self):
        r = requests.post(url_api)
        self.assertEqual(r.status_code,200)
if __name__ == '__main__':
    unittest.main()