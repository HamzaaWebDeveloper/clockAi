from praytimes import PrayTimes
from datetime import datetime

cities = {
    "karachi": (24.8607, 67.0011),
    "lahore": (31.5204, 74.3587),  
    "islamabad": (33.6844, 73.0479)
}

def namaztime(city, namaz_name, date):
    pt = PrayTimes('Karachi') 
    pt.adjust({'asr': 'Hanafi'})

    date_tuple = (date.year, date.month, date.day)
    
   
    latitude, longitude = cities[city.lower()]
    
    times = pt.getTimes(date_tuple, (latitude, longitude), 5)
    return times[namaz_name.lower()]


city = input("Sheher Ka Naam Chunain (Karachi,Lahore,Islamabad): ")
prayer = input("Namaz ka naam chunain (Fajr,Dhuhr,Asr,Maghrib,Isha): ")
date_str = input("Tareekh Chunain (YYYY-MM-DD): ")


selected_date = datetime.strptime(date_str, "%Y-%m-%d")

print(f"\n{city.title()} main {date_str} ko:")
print(f"{prayer} ka waqt : {namaztime(city, prayer, selected_date)}")


