import socket
import time
from time import strptime

import requests
from datetime import datetime, timedelta


def getData(departFrom, arriveAt, flyOn, noOfPassengers, noOfChildren, noOfInfants, cabinClass, minLayover):
    payload = {"country": "UK",
               "currency": "GBP",
               "locale": "en-GB",
               "originplace": departFrom,
               "destinationplace": arriveAt,
               "adults": noOfPassengers,
               "locationSchema": "iata",
               "children": noOfChildren,
               "infants": noOfInfants,
               "cabinclass": cabinClass,
               "outbounddate": flyOn,
               "apikey": "ha158486926168541326868639329158"
               }

    head = {"Content-Type": "application/x-www-form-urlencoded",
            "X-Forwarded-For": socket.gethostbyname(socket.gethostname()),
            "Accept": "application/json"}

    createSession = requests.post("http://partners.api.skyscanner.net/apiservices/pricing/v1.0",
                                  data=payload, headers=head)

    while True:
        r = requests.get(createSession.headers.get("Location"),
                         params={"apikey": "ha158486926168541326868639329158"})
        if r.json().get("Status") != "UpdatesPending":
            break

    return filterResults(r.json(), minLayover)


def filterResults(json, minLayover):
    segmentIDs = []
    legs = json.get("Legs")
    for leg in legs:
        if len(leg.get("SegmentIds")) == 2:
            segmentIDs.append([leg.get("SegmentIds"), leg.get("Id")])

    segments = json.get("Segments")
    journeys = []

    for journey in segmentIDs:
        bothFlights = []
        for segment in segments:
            if segment.get("Id") == journey[0][0]:
                bothFlights.append(segment)
            if segment.get("Id") == journey[0][1]:
                bothFlights.append(segment)
        journeys.append([bothFlights, journey[1]])

    applicableLegID = []
    for trip in journeys:
        arrival = strptime(trip[0][0].get("ArrivalDateTime"), "%Y-%m-%dT%X")
        departure = strptime(trip[0][1].get("DepartureDateTime"), "%Y-%m-%dT%X")

        if time.localtime(time.mktime(arrival) + minLayover*60) < departure:
            applicableLegID.append(trip[1])

    applicableItineraries = []
    for id in applicableLegID:
        for itinerary in json.get("Itineraries"):
            if itinerary.get("OutboundLegId") == id:
                applicableItineraries.append(itinerary)

    print(applicableItineraries)
