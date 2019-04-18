import requests

API_KEY = "4184978bccfb87d8e4016668779af080"
REQ_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_info(cn):
    rp = "?q=" + cn + ",US&unit=imperial&apikey=" + API_KEY
    r = REQ_URL + rp
    response = requests.get(r)
    if response.status_code==200 :
        d = response.json()
        lat = d["coord"]["lat"]
        lon = d["coord"]["lon"]
        correct_lon = (lon * -1) #For some reason, longitude is displayed as negative in json file and positive when you google the actual longitude
        print("The latitude and longitude of {}, is ({}° N, {}° W)".format(cn, lat, correct_lon))
    else:
        print("The city you entered does not seem to come up, please make sure it is an actual city.")


if __name__ == "__main__":
    city = input("Enter the name of the city you wish to get the latitude and longitude of.")
    fetch_info(city)