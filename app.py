import json
import random
import datetime
import time
import requests
from requests.exceptions import HTTPError
from datetime import datetime
dateTimeObj = datetime.now()
import http.client
from random import randint, choice

#from manufacturingdevices table in ATP
PressureDeviceNames = ['JN1994', 'BB4848']
TemperatureDeviceNames = ['BB200','BB207', 'AB9191']
FlowDeviceNames = ['BB201', 'XX9888']

def getFlow():
    data = {}
    data['deviceid'] = random.choice(FlowDeviceNames)
    #data['measurement'] = random.randint(99, 105)
    data['measurement'] = choice([(random.randint(60,100)),(random.randint(101,105))])
    data['datetime'] = dateTimeObj.strftime("%Y-%m-%dT%H:%M:%SZ")
    data['parameter'] = 'Flow'
    return data
def getTemperature():
    data = {}
    data['deviceid'] = random.choice(TemperatureDeviceNames)
    #data['measurement'] = random.randint(15, 35) or random.randint(40, 45)
    data['measurement'] = choice([(random.randint(15,35)),(random.randint(36,50))])
    data['datetime'] = dateTimeObj.strftime("%Y-%m-%dT%H:%M:%SZ")
    data['parameter'] = 'Temperature'
    return data
def getPressure():
    data = {}
    data['deviceid'] = random.choice(PressureDeviceNames)
    #data['measurement'] = random.randint(50, 90) or random.randint(91, 98)
    data['measurement'] = choice([(random.randint(50,90)),(random.randint(91,105))])
    data['datetime'] = dateTimeObj.strftime("%Y-%m-%dT%H:%M:%SZ")
    data['parameter'] = 'Pressure'
    return data
# Generate each parameter's data input in varying proportions
def submitData(data):
    headers = {
        'Content-Type': "application/json",
        'Content-Transfer-Encoding': "buffered"
            }
    payload = data
    print(payload)  
    url='https://BASE_URL/ords/apexuser/deviceTimes/times'
    r = requests.request("POST", url, data=payload, headers=headers)
    print(r.status_code)
    response = requests.Session()
while True:
    time.sleep(1)
    rnd = random.random()
    if (0 <= rnd < 0.20):
        data = json.dumps(getFlow())
        submitData(data)
        print('flow data submitted')
    elif (0.20<= rnd < 0.55):
        data = json.dumps(getTemperature())
        submitData(data)
        print('temperature data submitted')
    elif (0.55<= rnd < 0.70):
        data = json.dumps(getPressure())
        submitData(data)
        print('pressure data submitted')

# inspired by https://github.com/aws-samples/sbs-iot-data-generator

        
