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



