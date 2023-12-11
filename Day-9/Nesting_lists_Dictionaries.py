#Nesting Dictionary in a Dictionary

travel_log =[
    {
        "country":"France",
        "visits":12,
        "cities": ["Paris" , "Lille" , "Dijon"]
    },
    
    {
        "country":"Germany",
        "visits":5,
        "cities": ["Berlin" , "Hamburg" , "Stuttgart"]   
    },
    
    {
        "country":"England",
        "visits":6,
        "cities": ["London" , "Liverpool" , "Manchester"]
    }
    
]
  
def add_new_country(country_visited , time_visited , cities_visted):
    new_country = {}
    new_country["country"] = country_visited
    new_country["total_visits"] = time_visited
    new_country["cities_visited"] = cities_visted
    travel_log.append(new_country)

add_new_country("Russia" , 2 , ["Moscow", "Saint Petersbut"])
print(travel_log)