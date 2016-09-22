import requests
import sys
import re
import os

user = 'admin'
password = 'WelcometoCX01'
session = requests.session()
cookie = {'ZWAYSession':'ceb77ce4-953e-48bf-c747-0104a466bc31'}

if len(sys.argv) > 1:
	command = sys.argv[1]

	if sys.argv[1] == 'get':
		res = session.get("http://10.0.1.12:8083/ZAutomation/api/v1/devices/ZWayVDev_zway_5-0-37", cookies=cookie).text
		print(re.findall(r"level(.*)", res)[0][3:5])
	else:
		session.get("http://10.0.1.12:8083/ZAutomation/api/v1/devices/ZWayVDev_zway_5-0-37/command/{}".format(command), cookies=cookie)

		if command == "on":
			os.system("say get up you lazy bastard")
		elif command == "off":
			os.system("say thank you")
else:
	print("This program needs a command: (on / off)")