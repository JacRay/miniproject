# importing the module import requests
# base URL BASE_URL = "https://maps.googleapis.com/maps/api/staticmap?"
# API key API_KEY = "Your API Key"
# city CITY = "9.964339620316606, 76.28738084701202"
# zoom value
ZOOM = 20
# updating the URL
URL = BASE_URL + "center=" + CITY + "&zoom=" + str(ZOOM) + "&size = 500x500&key=" + API_KEY
# HTTP request
response = requests.get(URL)
# storing the response in a file (image)
with open('hyderabad.png', 'wb') as file:
   # writing data into the file
   file.write(response.content)
# make sure you have a valid API Key
# You will get 403 as status_code if your API Key is invalid