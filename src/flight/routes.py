from flask import jsonify, request, abort, Response, render_template
from flight import app
from extractor import getData, filterResults
from datetime import datetime
import json
import requests
from weather import getWeather

url = "http://partners.api.skyscanner.net/apiservices/"

@app.route('/', methods=['GET'])
def index(path):
    return app.send_from_directory('static', path)

@app.route('/flight/<country>/<currency>/<locale>/<originPlace>/<destinationPlace>/<inboundDate>', methods=['GET'])
@app.route('/flight/<country>/<currency>/<locale>/<originPlace>/<destinationPlace>/<outboundDate>/<inboundDate>', methods=['GET'])
def flight(country, currency, locale, originPlace, destinationPlace, inboundDate, outboundDate = None):
    if request.args:
        api = request.args.get('apiKey')
        if not api:
            return jsonify({ 'error': 'Missing API Key' })
        adults = request.args.get('adults')
        if not adults:
            return jsonify({ 'error': 'Missing Adults attributes' })
        children = request.args.get('children')
        if not children or 0 <= int(children) >= 16:
            return jsonify({ 'error': 'Incorrect children attributes' })
        infants = request.args.get('infants')
        if not infants or 0 <= int(infants) >= 16:
            return jsonify({ 'error': 'Incorrect infants attributes' })
        # The cabin class. Can be “economy”, “premiumeconomy”, “business”, “first”
        cabinClass = request.args.get('cabinClass')
        if not cabinClass or cabinClass.lower() not in ['economy', "premiumeconomy", "business", "first"]:
            return jsonify({ 'error': 'Incorrect cabinClass attributes' })
        minLayover = request.args.get('minLayover')
        if not minLayover or int(minLayover) < 0:
            return jsonify({ 'error': 'Incorrect minLayover attributes' })
        includeCarriers = request.args.get('includeCarriers')
        excludeCarriers = request.args.get('excludeCarriers')
        groupPricing = request.args.get('groupPricing')
        data = getData(originPlace,destinationPlace,inboundDate,int(adults),int(children),int(infants),cabinClass,int(minLayover))
        # return jsonify(data)
        return render_template('index.html', flights=data)

@app.route('/<originPlace>/<inboundDate>/<destinationPlace>/<layover>/<adults>/<children>/<infants>/<cabinClass>', methods=['GET'])
def fly(originPlace, inboundDate, destinationPlace, layover, adults, children, infants, cabinClass):
    # originPlace = originPlace.lower()
    # destinationPlace = destinationPlace.lower()
    layover = layover * 60
    if 0 <= int(children) >= 16:
        return jsonify({ 'error': 'Incorrect children attributes' })
    if 0 <= int(infants) >= 16:
        return jsonify({ 'error': 'Incorrect infants attributes' })
    cabinClass = cabinClass.lower()
    cabinClass = cabinClass.replace(" class", "")
    if cabinClass not in ['economy', "premiumeconomy", "business", "first"]:
        return jsonify({ 'error': 'Incorrect cabinClass attributes' })
    data = getData(originPlace,destinationPlace,inboundDate,int(adults),int(children),int(infants),cabinClass,int(layover))
    return jsonify(data)

@app.route('/<originPlace>/<month>/<day>/<year>/<destinationPlace>/<layover>/<adults>/<children>/<infants>/<cabinClass>', methods=['GET'])
def price(originPlace, month, day, year, destinationPlace, layover, adults, children, infants, cabinClass):
    # originPlace = originPlace.lower()
    # destinationPlace = destinationPlace.lower()
    layover = layover * 60
    inboundDate = year + '-' + month + '-' + day
    if 0 <= int(children) >= 16:
        return jsonify({ 'error': 'Incorrect children attributes' })
    if 0 <= int(infants) >= 16:
        return jsonify({ 'error': 'Incorrect infants attributes' })
    cabinClass = cabinClass.lower()
    cabinClass = cabinClass.replace(" class", "")
    if cabinClass not in ['economy', "premiumeconomy", "business", "first"]:
        return jsonify({ 'error': 'Incorrect cabinClass attributes' })
    data = getData(originPlace,destinationPlace,inboundDate,int(adults),int(children),int(infants),cabinClass,int(layover))
    return jsonify(data)

@app.route('/weather/<airport>/<date>', methods=['GET'])
def weather(date, airport):
	return jsonify(getWeather(date, airport))


@app.route('/suggest/<country>/<currency>/<locale>', methods=['GET'])
def suggest(country, currency, locale):
    if request.args:
        query = request.args.get('query')
        api = request.args.get('api')
        if not api:
        	return jsonify({ 'error': 'Missing API Key' })
        if not query or len(query) < 2:
        	return jsonify({ 'error': 'Incorrect Query' })
        suggestions = get_suggestions(country, currency, locale, query, api)
        return jsonify({ 'suggestions': suggestions })

def get_suggestions(country, currency, locale, query, api):
	suggest = requests.get(url+"autosuggest/v1.0/"+country+"/"+currency+"/"+locale+"?query="+query+"&apiKey="+api)
	suggestJSON = json.loads(suggest.text)
	return [{'PlaceId':x['PlaceId'],'PlaceName':x['PlaceName']} for x in suggestJSON['Places']]

