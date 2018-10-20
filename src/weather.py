# ca57e7eea30cea06a0320e317b2d9057
import forecastio
import csv
import sys
from datetime import datetime

api_key = "ca57e7eea30cea06a0320e317b2d9057"

def getWeather(time, location):
	time = datetime.strptime(time,  "%Y-%m-%dT%X")
	lat, lng = getLongLag(location)
	forecast = forecastio.load_forecast(api_key, lat, lng, time)
	return forecast.json.get('currently')


def getLongLag(location):
	location = location[:-4]
	#read csv, and split on "," the line
	csv_file = csv.reader(open('airports.csv', "r"), delimiter=",")

	#loop through csv list
	for row in csv_file:
	    if location == row[4]:
	         return (row[6], row[7])
