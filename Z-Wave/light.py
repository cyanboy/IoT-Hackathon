import requests
import sys

user = 'admin'
password = 'WelcometoCX01'
session = requests.session()
cookie = {'ZWAYSession':'ceb77ce4-953e-48bf-c747-0104a466bc31'}

if len(sys.argv) > 1:
	command = sys.argv[1]

	p = session.get("http://10.0.1.12:8083/ZAutomation/api/v1/devices/ZWayVDev_zway_5-0-37/command/{}".format(command), cookies=cookie)
else:
	print("This program needs a command: (on / off)")