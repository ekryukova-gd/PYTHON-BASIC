import pandas as pd
import os
import sys
from io import StringIO
import xml.etree.ElementTree as ET


# read data from json files
path = os.path.join(sys.path[0], 'parsing_serialization_task', 'source_data')
spain_data = pd.DataFrame()

for city in os.listdir(path):
    for weatherfile in os.listdir(os.path.join(path, city)):
        if weatherfile.endswith('.json'):
            with open(os.path.join(path, city, weatherfile), 'r') as f:
                if ' ' in city:
                    city = '_'.join(city.split(' '))
                spain_data[city] = pd.read_json(f, orient='index')

spain_data = spain_data.transpose()

# Calculate mean, maximum, minimum temperature and wind speed for each city.

weather_summary_by_city = pd.DataFrame()

for city in spain_data.index:
    json_data = StringIO(pd.DataFrame(spain_data.loc[city]['hourly']).to_json(orient='records'))
    city_weather = pd.read_json(json_data)
    min_temp = city_weather['temp'].min()
    max_temp = city_weather['temp'].max()
    mean_temp = city_weather['temp'].mean()
    min_wind_speed = city_weather['wind_speed'].min()
    max_wind_speed = city_weather['wind_speed'].max()
    mean_wind_speed = city_weather['wind_speed'].mean()
    weather_summary_by_city[city] = {'mean_temp': mean_temp, 'mean_wind_speed': mean_wind_speed,
                                     'min_temp': min_temp, 'min_wind_speed': min_wind_speed,
                                     'max_temp': max_temp, 'max_wind_speed': max_wind_speed, }

weather_summary_by_city = weather_summary_by_city.transpose()

# Calculate mean temperature and wind speed for the whole country by using produced data before.
# Find the coldest, the warmest and the windiest cities in Spain (you must use mean values from step 2 to do that).

spain_summary = {'mean_temp': weather_summary_by_city['mean_temp'].mean(),
                 'mean_wind_speed': weather_summary_by_city['mean_wind_speed'].mean(),
                 'coldest_place': weather_summary_by_city.loc[weather_summary_by_city['mean_temp'] ==
                                                              weather_summary_by_city['mean_temp'].min()].index[0],
                 'warmest_place': weather_summary_by_city.loc[weather_summary_by_city['mean_temp'] ==
                                                              weather_summary_by_city['mean_temp'].max()].index[0],
                 'windiest_place': weather_summary_by_city.loc[weather_summary_by_city['mean_wind_speed']==
                                                              weather_summary_by_city['mean_wind_speed'].max()].index[0]}
#
# print(spain_summary)
#
# print(weather_summary_by_city.dtypes)

# Create root element <weather>

root = ET.Element("weather")
root.set("country", "Spain")
root.set("date", "2021-09-25")

# Add summary element <summary>
summary = ET.SubElement(root, "summary")
for key, value in spain_summary.items():
    if type(value) is not str:
        summary.set(key, str(round(value, 2)))
    else:
        summary.set(key, value)

# Add cities element <cities>
cities = ET.SubElement(root, "cities")

for city in weather_summary_by_city.index:
    city_name = ET.SubElement(cities, city)
    for attribute in weather_summary_by_city.columns:
        city_name.set(attribute, str(round(weather_summary_by_city.loc[city][attribute], 2)))


xml_data = ET.tostring(root)  # binary string
with open('result.xml', 'w') as f:  # Write in file as utf-8
    f.write(xml_data.decode('utf-8'))


