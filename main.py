import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "f956584ba970b6dbdb1cd4dc7bed2309"
weather_params = {
    "lat": 25.572491,
    "lon": 91.310760,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}
account_sid = "AC225f377542424bbd11b1751f61ed9fda"
auth_token = "630cdbe9db5ac3957bdf964347924db7"

will_rain = False
connection = requests.get(OWM_Endpoint, params=weather_params)
connection.raise_for_status()
data = connection.json()["hourly"][:23]
for hour_data in data:
    weather_id = hour_data["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Its going to rain today, Bring an Umbrella",
        from_='+15624185294',
        to='+91 70731 68466'
    )
    print(message.sid)
