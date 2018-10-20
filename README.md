# PlaneAndSimple

Project for HackUPC using the skyscanner API

## Set up

### Virtualenv

`Virtualenv` helps establish an isolated Python environment. 

The environment separates project-specific dependencies and their versions from the Python modules installed locally.

```bash
virtualenv -p python3 venv
```

This creates a virtual environment called `venv`. 

To run the virtual environment, run the following:

```bash
source venv/bin/activate
```

The following command line prompt will indicate that you’re in the virtual environment:

```bash
(venv) >
```

To deactivate the virtual environment, run the following:

```
deactivate
```

## Dependencies

At the root of directory of this project, run:

```
pip install -r src/requirements.txt
```

## Origanization

Here is the file structure of the directory `./src`

```
.
├── config.py
├── requirements.txt
├── run.py
└── flight
    ├── __init__.py
    ├── models.py
    └── routes.py
```

- `config.py` defines the configuration for the Flask app to run with.
- `requirements.txt` outlines the initial module dependencies of the app
- `run.py` is the run script for the Flask app
- `flight/__init__.py` defines the Flask app instance.
- `flight/models.py` is where you should define the models of your application.
- `flight/routes.py` defines all the routes (a.k.a. endpoints) that users will be able to interact with in order to check for flights.

## API


**Get Request**

```
http://partners.api.skyscanner.net/apiservices/browseroutes/v1.0/UK/GBP/en-GG/BCN-sky/MAN-sky/2018-11-21/2018-11-21?apiKey=ha158486926168541326868639329158
```

e.g.

```
http://0.0.0.0:5000/flight/UK/GBP/en-GG/BCN-sky/MAN-sky/2018-11-21/2018-11-21?apiKey=ha158486926168541326868639329158&adults=1&children=0&infants=0&cabinClass=economy&minLayover=200
```

**Response**

```
{
    "arriveAt": "MAN-sky",
    "departFrom": "BCN-sky",
    "flightsInfo": [
        {
            "arrivalDate": "2018-11-21T16:45:00",
            "bestPrice": 1088.03,
            "deeplinkUrl": "http://partners.api.skyscanner.net/apiservices/deeplink/v2?_cje=Wa3rESSDeivD%2bgLXwmvBVxMjrxY4fRDbWgPSM81Xhyg%2b26qU8rMuHA%2bq9cLv1kvW&url=https%3a%2f%2fwww.skyscanner.net%2ftransport_deeplink%2f4.0%2fUK%2fen-GB%2fGBP%2fgtuk%2f1%2f9772.13880.2018-11-21%2fair%2ftrava%2fflights%3fitinerary%3dflight%7c-32478%7c3696%7c9772%7c2018-11-21T09%3a45%7c10141%7c2018-11-21T11%3a55%7c130%7c-%7c-%7c-%3bflight%7c-32492%7c6177%7c10141%7c2018-11-21T16%3a25%7c13880%7c2018-11-21T16%3a45%7c80%7c-%7c-%7c-%26carriers%3d-32478%2c-32492%26operators%3d-32478%3b-32478%26passengers%3d1%26channel%3ddataapi%26cabin_class%3deconomy%26facilitated%3dfalse%26ticket_price%3d1088.03%26is_npt%3dfalse%26is_multipart%3dfalse%26client_id%3dskyscanner_b2b%26deeplink_ids%3deu-west-1.prod_101ee0a97d39bba136a18c62de392a01%26commercial_filters%3dfalse%26q_datetime_utc%3d2018-10-20T14%3a03%3a00",
            "departureDate": "2018-11-21T09:45:00",
            "layoverAt": "Brussels International",
            "layoverLength": 270
        },
        {
            "arrivalDate": "2018-11-21T18:15:00",
            "bestPrice": 94.01,
            "deeplinkUrl": "http://partners.api.skyscanner.net/apiservices/deeplink/v2?_cje=Wa3rESSDeivD%2bgLXwmvBVxMjrxY4fRDbWgPSM81Xhyg%2b26qU8rMuHA%2bq9cLv1kvW&url=https%3a%2f%2fwww.skyscanner.net%2ftransport_deeplink%2f4.0%2fUK%2fen-GB%2fGBP%2fdhop%2f1%2f9772.13880.2018-11-21%2fair%2ftrava%2fflights%3fitinerary%3dflight%7c-32332%7c9441%7c9772%7c2018-11-21T09%3a35%7c11165%7c2018-11-21T11%3a55%7c140%7c-%7c-%7c-%3bflight%7c-32302%7c7216%7c11165%7c2018-11-21T17%3a30%7c13880%7c2018-11-21T18%3a15%7c105%7c-%7c-%7c-%26carriers%3d-32332%2c-32302%26operators%3d-32332%3b-32302%26passengers%3d1%26channel%3ddataapi%26cabin_class%3deconomy%26facilitated%3dfalse%26ticket_price%3d94.01%26is_npt%3dfalse%26is_multipart%3dfalse%26client_id%3dskyscanner_b2b%26deeplink_ids%3deu-west-1.prod_26045a6840c392012532eda23221ee96%26commercial_filters%3dfalse%26q_datetime_utc%3d2018-10-20T14%3a03%3a00",
            "departureDate": "2018-11-21T09:35:00",
            "layoverAt": "Dusseldorf International",
            "layoverLength": 335
        }
    ]
}
```



**GET Suggest**

```
http://0.0.0.0:5000/suggest/{country}/{currency}/{locale}?query={query}&api={apiKey}
```

e.g. 

```
http://0.0.0.0:5000/suggest/UK/GBP/EN?query=fr&api=ha158486926168541326868639329158
```

**Response**

```
{
    "suggestions": [
        {
            "PlaceId": "FR-sky",
            "PlaceName": "France"
        },
        {
            "PlaceId": "FRAN-sky",
            "PlaceName": "Frankfurt"
        }
    ]
}
```

**GET Weather**

```
http://0.0.0.0:5000/weather/{airport}/{date}
```

e.g.

```
http://0.0.0.0:5000/weather/BCN-sky/2018-11-21T16:45:00
```

**Response**

```
{
    "apparentTemperature": 14.56,
    "cloudCover": 0.5,
    "cloudCoverError": 0.11,
    "dewPoint": 8.25,
    "humidity": 0.66,
    "icon": "partly-cloudy-day",
    "precipType": "rain",
    "pressure": 1017.33,
    "pressureError": 64.5,
    "summary": "Partly Cloudy",
    "temperature": 14.56,
    "temperatureError": 3.11,
    "time": 1542815100,
    "uvIndex": 0,
    "windBearing": 250,
    "windBearingError": 75.28,
    "windSpeed": 0.92,
    "windSpeedError": 3.51
}
```

