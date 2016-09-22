import requests
import sys
import time

user = 'admin'
password = 'WelcometoCX01'
session = requests.session()
cookie = {'ZWAYSession':'ceb77ce4-953e-48bf-c747-0104a466bc31'}

delay = .25

while True:
	session.get("http://10.0.1.12:8083/ZAutomation/api/v1/devices/ZWayVDev_zway_5-0-37/command/on", cookies=cookie)
	time.sleep(delay)
	session.get("http://10.0.1.12:8083/ZAutomation/api/v1/devices/ZWayVDev_zway_5-0-37/command/off", cookies=cookie)
	time.sleep(delay)