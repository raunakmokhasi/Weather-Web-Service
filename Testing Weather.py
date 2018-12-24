
import unittest
from a1 import weather_response
from a1 import has_error
from a1 import get_temperature 
from a1 import get_humidity
from a1 import get_pressure
from a1 import get_wind
from a1 import get_sealevel

class testpoint(unittest.TestCase):
	
	def test_weather_response(self):
		self.assertEqual(weather_response("Delhi","5753b64e9e1290004733b7726fb5aa15"),weather_response("Delhi","5753b64e9e1290004733b7726fb5aa15"))
		self.assertEqual(weather_response("Mumbai","5753b64e9e1290004733b7726fb5aa15"),weather_response("Mumbai","5753b64e9e1290004733b7726fb5aa15"))
		self.assertEqual(weather_response("Bangalore","5753b64e9e1290004733b7726fb5aa15"),weather_response("Bangalore","5753b64e9e1290004733b7726fb5aa15"))
		self.assertEqual(weather_response("Chennai","5753b64e9e1290004733b7726fb5aa15"),weather_response("Chennai","5753b64e9e1290004733b7726fb5aa15"))
		self.assertEqual(weather_response("Hyderabad","5753b64e9e1290004733b7726fb5aa15"),weather_response("Hyderabad","5753b64e9e1290004733b7726fb5aa15"))


	def test_has_error(self):
		self.assertTrue(has_error("Delhi",weather_response("London","5753b64e9e1290004733b7726fb5aa15")))
		self.assertTrue(has_error("Mumbai",weather_response("Munich","5753b64e9e1290004733b7726fb5aa15")))
		self.assertTrue(has_error("Bangalore",weather_response("Dubai","5753b64e9e1290004733b7726fb5aa15")))
		self.assertTrue(has_error("Chennai",weather_response("Doha","5753b64e9e1290004733b7726fb5aa15")))
		self.assertTrue(has_error("Hyderabad",weather_response("Beijing","5753b64e9e1290004733b7726fb5aa15")))

	def test_get_temperature(self):
		json = weather_response("Delhi","5753b64e9e1290004733b7726fb5aa15")
		t = ["03:00:00","06:00:00","09:00:00","12:00:00","15:00:00"]
		self.assertAlmostEqual(get_temperature(json,0,t[0]),300,delta=35)
		self.assertAlmostEqual(get_temperature(json,1,t[1]),300,delta=35)
		self.assertAlmostEqual(get_temperature(json,2,t[2]),300,delta=35)
		self.assertAlmostEqual(get_temperature(json,3,t[3]),300,delta=35)
		self.assertAlmostEqual(get_temperature(json,4,t[4]),300,delta=35)	
		

	def test_get_humidity(self):
		json = weather_response("Delhi","5753b64e9e1290004733b7726fb5aa15")
		t = ["03:00:00","06:00:00","09:00:00","12:00:00","15:00:00"]
		self.assertAlmostEqual(get_humidity(json,0,t[0]),95,delta=45)
		self.assertAlmostEqual(get_humidity(json,1,t[1]),95,delta=45)
		self.assertAlmostEqual(get_humidity(json,2,t[2]),95,delta=45)
		self.assertAlmostEqual(get_humidity(json,3,t[3]),95,delta=45)
		self.assertAlmostEqual(get_humidity(json,4,t[4]),95,delta=45)
	
	def test_get_pressure(self):
		json = weather_response("Delhi","5753b64e9e1290004733b7726fb5aa15")
		t = ["03:00:00","06:00:00","09:00:00","12:00:00","15:00:00"]
		self.assertAlmostEqual(get_pressure(json,0,t[0]),975,delta=40)
		self.assertAlmostEqual(get_pressure(json,1,t[1]),975,delta=40)
		self.assertAlmostEqual(get_pressure(json,2,t[2]),975,delta=40)
		self.assertAlmostEqual(get_pressure(json,3,t[3]),975,delta=40)
		self.assertAlmostEqual(get_pressure(json,4,t[4]),975,delta=40)
	
	def test_get_wind(self):
		json = weather_response("Delhi","5753b64e9e1290004733b7726fb5aa15")
		t = ["03:00:00","06:00:00","09:00:00","12:00:00","15:00:00"]
		self.assertAlmostEqual(get_wind(json,0,t[0]),10,delta=10)
		self.assertAlmostEqual(get_wind(json,1,t[1]),10,delta=10)
		self.assertAlmostEqual(get_wind(json,2,t[2]),10,delta=10)
		self.assertAlmostEqual(get_wind(json,3,t[3]),10,delta=10)
		self.assertAlmostEqual(get_wind(json,4,t[4]),10,delta=10)


	def test_get_sealevel(self):
		json = weather_response("Delhi","5753b64e9e1290004733b7726fb5aa15")
		t = ["03:00:00","06:00:00","09:00:00","12:00:00","15:00:00"]
		self.assertAlmostEqual(get_sealevel(json,0,t[0]),1025,delta=50)
		self.assertAlmostEqual(get_sealevel(json,1,t[1]),1025,delta=50)
		self.assertAlmostEqual(get_sealevel(json,2,t[2]),1025,delta=50)
		self.assertAlmostEqual(get_sealevel(json,3,t[3]),1025,delta=50)
		self.assertAlmostEqual(get_sealevel(json,4,t[4]),1025,delta=50)
	
if __name__=='__main__':
	unittest.main()
