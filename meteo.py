from geopy.geocoders import Nominatim
import pandas as pd
from datetime import datetime, timedelta
from meteostat import Point, Daily, Stations, Hourly, Monthly
from get_coordonees import get_coordonnees
import matplotlib.pyplot as plt



#data = get_coordonnees()
#df = pd.DataFrame.from_dict(data, orient="columns")

df = pd.read_csv("coordonnees.csv", index_col=0)

start = datetime.now() - timedelta(days=7)
end = datetime.now() + timedelta(hours=12)

def weather(moment=Hourly, start=start, end=end):

    val1 = list(df.iloc[0, :])
    city = Point(val1[2], val1[3], val1[4])

    data1 = moment(city, start, end)
    data1 = data1.fetch()
    data1.insert(0, "Address", val1[0])
    data1.insert(1, "Department", val1[1])
    data1.insert(2, "Latitude", val1[2])
    data1.insert(3, "Longitude", val1[3])
    data1.insert(4, "Altitude", val1[4])


    for i in range(1, df.shape[0]):
          val = list(df.iloc[i,:])
          city = Point(val[2], val[3], val[4])

          data = moment(city, start, end)
          data = data.fetch()
          #data.drop("Région", axis=1)
          data.insert(0, "Address", val[0])
          data.insert(1, "Department", val[1])
          data.insert(2, "Latitude", val[2])
          data.insert(3, "Longitude", val[3])
          data.insert(4, "Altitude", val[4])

          data1 = data1.append(data)
          #print(data.head(5))
    return data1.sort_index().to_dict('list')



### Main
if __name__=='__main__':
    print(weather())