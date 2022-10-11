from geopy.geocoders import Nominatim
import pandas as pd
from datetime import datetime, timedelta
from meteostat import Point, Daily, Stations, Hourly
import matplotlib.pyplot as plt

data = {"Adresse Complète": [],
        "Département": [],
        "Latitude": [],
        "Longitude": [],
        "Altitude": []
        }

departements = [
    "Dakar", "Guédiawaye", "Pikine", "Rufisque", "Keur Massar",
    "Bambey", "Diourbel", "Mbacké",
    "Fatick", "Foundiougne", "Gossas",
    "Kaolack", "Guinguinéo", "Nioro du Rip",
    "Kolda", "Vélingara", "Médina Yoro Foulah",
    "Kébémer", "Linguère", "Louga",
    "Kanel", "Matam", "Ranérou",
    "Dagana", "Podor", "Saint-Louis",
    "Bakel", "Koumpentoum", "Tambacounda", "Goudiry",
    "Mbour", "Thiès", "Tivaouane",
    "Bignona", "Oussouye", "Ziguinchor",
    "Birkelane", "Kaffrine", "Malem-Hodar", "Koungheul",
    "Kédougou", "Salemata", "Saraya",
    "Bounkiling", "Goudomp", "Sédhiou"
]


def get_coordonnees(list_dpt=departements):
    for dpt in list_dpt:
        loc = Nominatim(user_agent="GetLoc")

        getLoc = loc.geocode(dpt + " departement, Sénégal")

        adress = getLoc.address.split(",")
        data.setdefault("Adresse Complète", []).append(getLoc.address)
        data.setdefault("Département", []).append(dpt)
        data.setdefault("Longitude", []).append(getLoc.longitude)
        data.setdefault("Latitude", []).append(getLoc.latitude)
        data.setdefault("Altitude", []).append(getLoc.altitude)

    return data


#data = get_coordonnees(departements)
#df = pd.DataFrame.from_dict(data, orient="columns")