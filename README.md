# Weather-Web-Service
TL;DR - Getting data from a weather web service which provides the weather condition for a particular location in the world.


To use the service, you employ special URLs that start with the following prefix:
http://api.openweathermap.org/data/2.5/forecast ?
This prefix is followed by a weather query. A weather query has two pieces of information in the
following format -
q=location & APPID=API Key
where location is name of any city in the world and API key is the interface to the web service.
For example, if you want to know the weather condition of Delhi, the query is
q=Delhi&APPID=2ab136be1543b5789451a5994364c0d3
The full URL for this query is
http://api.openweathermap.org/data/2.5/forecast?q=Delhi&APPID=2ab136be1543b5789451a5994364c0d3

It is displayed as -
{"temp":300.71,"temp_min":300.71,"temp_max":301.189,"pressure":992.81,"sea_level":1017.24,
"grnd_level":992.81,"humidity":96,"temp_kf":-0.48}
This is what is known as JSON representation

The python script interacts with the web service and processes the JSON Data to give the desired weather attribute.

I have also included a testing module for the weather web service.
