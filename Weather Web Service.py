
# function to get weather response
from urllib.request import *
import datetime

def weather_response(location, API_key):
	urlsave = urlopen("http://api.openweathermap.org/data/2.5/forecast?q=" + location + "&APPID=" + API_key)
	urlsave = urlsave.read().decode()
	return urlsave

# function to check for valid response 
def has_error(location,json):
	if (location not in json):
		return True


# function to get attributes on nth day
def get_temperature (json, n=0,t = "3:00"):
	curdate = datetime.date.today()
	datedif = datetime.timedelta(days=n)
	date = str(curdate + datedif)  + " " + str(t) + ":00"
	df = json.find(date)
	rf = json.rfind('"temp"',0,df)
	com = json.find(",",rf)
	json = json[rf+7:com]
	return float(json)

def get_humidity(json, n=0,t = "3:00"):
	curdate = datetime.date.today()
	datedif = datetime.timedelta(days=n)
	date = str(curdate + datedif)  + " " + str(t) + ":00"
	df = json.find(date)
	rf = json.rfind('"humidity"',0,df)
	com = json.find(",",rf)
	json = json[rf+11:com]
	return float(json)

def get_pressure (json, n=0,t = "3:00"):
	curdate = datetime.date.today()
	datedif = datetime.timedelta(days=n)
	date = str(curdate + datedif)  + " " + str(t) + ":00"
	df = json.find(date)
	rf = json.rfind('"pressure"',0,df)
	com = json.find(",",rf)
	json = json[rf+11:com]
	return float(json)

def get_wind (json, n=0,t = "3:00"):
	curdate = datetime.date.today()
	datedif = datetime.timedelta(days=n)
	date = str(curdate + datedif)  + " " + str(t) + ":00"
	df = json.find(date)
	rf = json.rfind('"speed"',0,df)
	com = json.find(",",rf)
	json = json[rf+8:com]
	return float(json)

def get_sealevel (json, n=0,t = "3:00"):
	curdate = datetime.date.today()
	datedif = datetime.timedelta(days=n)
	date = str(curdate + datedif)  + " " + str(t) + ":00"
	df = json.find(date)
	rf = json.rfind('"sea_level"',0,df)
	com = json.find(",",rf)
	json = json[rf+12:com]
	return float(json)


