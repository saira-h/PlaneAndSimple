import socket
import requests

apiKey = "ha158486926168541326868639329158"

departFrom = "BCN-sky"
arriveAt = "MAN-sky"
cabinClass = "Economy";

flyOn = "2018-11-02"

noOfPassengers = 1
noOfChildren = 0
noOfInfants = 0

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

createSession = requests.post("http://partners.api.skyscanner.net/apiservices/pricing/v1.0", data=payload, headers=head)

while True:
    r = requests.get(createSession.headers.get("Location"),
                     params={"apikey": "ha158486926168541326868639329158"})
    if r.json().get("Status") != "UpdatesPending":
        break

print(r.json())
