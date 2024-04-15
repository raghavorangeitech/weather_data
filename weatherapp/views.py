 
from django.shortcuts import render, HttpResponse
import requests
import datetime
import csv

def home(request):
    if request.method == 'POST':
        city = request.POST.get('city', 'City')
        request.session['city'] = city
    else:
        #city = request.session.get('city', 'City')
        city = "City"
    weather_api_key = 'e8ac3f63a84bcd2fa10440af0944e09e'
    map_api_key = 'c396ebac202ea101a20fdb95bd7d31b3'

    # Weather data API URL
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c396ebac202ea101a20fdb95bd7d31b3'
    weather_params = {'units': 'metric'}

    # Weather map API URL (requires latitude and longitude)
    # Replace latitude and longitude with actual coordinates
    latitude = 0.0
    longitude = 0.0
    map_url = f'http://maps.openweathermap.org/maps/2.0/weather/?appid=c396ebac202ea101a20fdb95bd7d31b3'

    try:
        # Fetch weather data
        weather_data = requests.get(weather_url, params=weather_params).json()

        description = weather_data['weather'][0]['description']
        icon = weather_data['weather'][0]['icon']
        temp = weather_data['main']['temp']
        sunset = weather_data['sys']['sunset']
        sunrise = weather_data['sys']['sunrise']
        cloud_cover = weather_data.get('clouds', {}).get('all', 'N/A')
        visibility = weather_data.get('visibility', 'N/A')
        current_date = datetime.datetime.now().date()
        country = weather_data['sys']['country']
        wind_speed = weather_data['wind']['speed']
        humidity = weather_data['main']['humidity']
        pressure = weather_data['main']['pressure']
        temp_max = weather_data['main']['temp_max']
        temp_min = weather_data['main']['temp_min']
        feels_like = weather_data['main']['feels_like']
        uv_index = weather_data.get('uv_index', 'N/A')
        sunrise_time = datetime.datetime.fromtimestamp(sunrise).strftime('%H:%M:%S')
        sunset_time = datetime.datetime.fromtimestamp(sunset).strftime('%H:%M:%S')
        return render(request, 'index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'sunset': sunset_time,
            'sunrise': sunrise_time,
            'cloud_cover': cloud_cover,
            'visibility': visibility,
            'city': city,
            'country': country,
            'current_date': current_date,
            'wind_speed': wind_speed,
            'humidity': humidity,
            'pressure': pressure,
            'temp_max': temp_max,
            'temp_min': temp_min,
            'feels_like': feels_like,
            'uv_index': uv_index,
            'latitude': latitude,
            'longitude': longitude,
        })
    except requests.RequestException:
        # Handle API request failure (e.g., network error)
        return HttpResponse("Error fetching weather data. Please try again later.")
def team_view(request):
    return render(request, 'team.html')
# Created a function for download data in csv.

def download_csv(request): 
    city = request.session.get('city', 'City')
         
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c396ebac202ea101a20fdb95bd7d31b3' 
    
    # Data fetched from website.
    weather_data = requests.get(weather_url).json()

    description = weather_data['weather'][0]['description']
    icon = weather_data['weather'][0]['icon']
    temp = weather_data['main']['temp']
    sunset = weather_data['sys']['sunset']
    sunrise = weather_data['sys']['sunrise']
    cloud_cover = weather_data.get('clouds', {}).get('all', 'N/A')
    visibility = weather_data.get('visibility', 'N/A')
    current_date = datetime.datetime.today().date()
    country = weather_data['sys']['country']
    wind_speed = weather_data['wind']['speed']
    humidity = weather_data['main']['humidity']
    pressure = weather_data['main']['pressure']
    temp_max = weather_data['main']['temp_max']
    temp_min = weather_data['main']['temp_min']
    feels_like = weather_data['main']['feels_like']
    uv_index = weather_data.get('uv_index', 'N/A')
    sunrise_time = datetime.datetime.fromtimestamp(sunrise).strftime('%H:%M:%S')
    sunset_time =  datetime.datetime.fromtimestamp(sunset).strftime('%H:%M:%S')

    # Set response content type
    response = HttpResponse(content_type='text/csv')
    # Set file name for download
    response['Content-Disposition'] = f'attachment; filename="{city}_data.csv"'

    # Create CSV writer
    writer = csv.writer(response)
    # Write CSV header
    writer.writerow(["City", "current_date", "description", "icon", "temp", "sunset", "sunrise", "cloud_cover", "visibility", "country", "wind_speed", "humidity", "pressure", "temp_max", "temp_min", "feels_like", "uv_index"])
    
    # Write CSV data rows
    writer.writerow([city, current_date, description, icon, temp, sunset_time, sunrise_time, cloud_cover, visibility, country, wind_speed, humidity, pressure, temp_max, temp_min, feels_like, uv_index])
        
    return response
