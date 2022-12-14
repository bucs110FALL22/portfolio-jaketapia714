from wthr import OpenWeatherMapAPI
from sng import LastFmAPI


#Binghamton's Latitude and Longitude
lat = float(42.0893)
lon = float(-75.9699)


# Access weather api with API key
wthr = OpenWeatherMapAPI('8c03010acc35132561ef735fb1340283')

#Get the current weather for the given location
weather = wthr.get_weather(lat, lon)

# State the weather
print(f'The weather is currently: {weather["weather"][0]["description"]}')

# Use the weather data to decide which type of song to look up
if weather == "sunny": 
    song_type = "happy"
elif weather == "rainy":
    song_type = "sad"
else:
    song_type = "relaxing"

# Access music api with API key
sng = LastFmAPI('960a1e14a823499589a19a5634e8cb33')

# Use the LastFM API to search for a song of the specified type
song = sng.search(song_type)

# # Display the selected song
print(f'I recommend you listen to {song}')
