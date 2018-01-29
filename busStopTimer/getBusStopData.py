import requests
import json

# buses towards north greenwich

def getTime():
    r = requests.get('https://api.tfl.gov.uk/StopPoint/490009889Y/Arrivals?app_id=a72839fb&app_key=5c55da50cc16c2863ad401d7445d9ba1')
    json_result = r.json()
    my_bus=[]
    for x in json_result:
        if x['timeToStation'] / 60 <= 15:
                x = str(x['lineName']) + ' to ' + str(x['destinationName']) + ' in ' + str( x['timeToStation'] / 60)
                my_bus.append(x)

    return my_bus
    with open('outfile.txt', 'w') as f:
        json.dump(my_bus,f,ensure_ascii=False, indent = 4, sort_keys=True)

getTime()
