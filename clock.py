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

# from praytimes import PrayTimes
# from datetime import datetime

# def get_pakistan_prayer_time(prayer_name, date, city):
#     # Pakistan coordinates (example cities)
#     locations = {
#         'karachi': (24.8607, 67.0011),
#         'lahore': (31.5204, 74.3587),
#         'islamabad': (33.6844, 73.0479),
        
#     }
    
#     pt = PrayTimes('Karachi')  # Using Karachi University method
#     pt.adjust({'asr': 'Hanafi'})  # Common in Pakistan
    
#     times = pt.getTimes(date, locations[city.lower()], 5)  # Pakistan UTC+5
#     return times[prayer_name.lower()]


# print(get_pakistan_prayer_time('fajr', (2024, 3, 15), 'islamabad'))


# from praytimes import PrayTimes
# from datetime import datetime

# # Pakistan ke major cities ke coordinates
# CITIES = {
#     "karachi": (24.8607, 67.0011),
#     "lahore": (31.5204, 74.3587),
#     "islamabad": (33.6844, 73.0479)
# }

# def get_prayer_time(city, prayer_name, date):
#     """Pakistan ke kisi shehar ka namaz ka time batata hai"""
    
#     # 1. Prayer time calculator setup karein
#     pt = PrayTimes('Karachi')  # Pakistan ke liye suitable method
#     pt.adjust({'asr': 'Hanafi'})  # Pakistan mein Asr Hanafi hisab se
    
#     # 2. Date ko tuple format mein convert karein (YYYY, MM, DD)
#     date_tuple = (date.year, date.month, date.day)
    
#     # 3. Shehar ka location nikalain
#     latitude, longitude = CITIES[city.lower()]
    
#     # 4. Namaz ka time calculate karein
#     times = pt.getTimes(date_tuple, (latitude, longitude), 5)  # UTC+5 for PKT
    
#     # 5. Required namaz ka time return karein
#     return times[prayer_name.lower()]

# # Example usage
# city = input("Shehar chunain (Karachi/Lahore/Islamabad): ")
# prayer = input("Namaz ka naam (Fajr/Dhuhr/Asr/Maghrib/Isha): ")
# date_str = input("Tareekh (YYYY-MM-DD): ")

# # Date string ko datetime object mein convert karein
# selected_date = datetime.strptime(date_str, "%Y-%m-%d")

# # Result show karein
# print(f"\n{city.title()} mein {date_str} ko:")
# print(f"{prayer} ka waqt: {get_prayer_time(city, prayer, selected_date)}")
