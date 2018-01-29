import requests
import json
import repeatFunction
from time import sleep

# buses towards north greenwich

def getTime():

    r = requests.get('https://api.tfl.gov.uk/StopPoint/490009889Y/Arrivals?app_id=a72839fb&app_key=5c55da50cc16c2863ad401d7445d9ba1')
    json_result = r.json()
    json_result = sorted(json_result, key=lambda x: x["timeToStation"])

    my_bus=[]
    for x in json_result:
        if x['timeToStation'] / 60 <= 16:
                x = str(x['lineName']) + ' to ' + str(x['destinationName']) + ' in ' + str( x['timeToStation'] / 60)
                my_bus.append(x)


    return my_bus

def outputText(inputx):
    with open('outfile.txt', 'w') as f:
        json.dump(inputx,f,ensure_ascii=False, indent = 4, sort_keys=True)
        
def repeat():
    rt = repeatFunction.RepeatedTimer(5,getTime)
    try:
        sleep(100000)
        getTime()
    finally:
        rt.stop()
