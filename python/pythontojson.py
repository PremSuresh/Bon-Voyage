#!/usr/bin/python
from urllib.request import urlopen
import json
import os
import requests
import threading

def drowsy ():
        os.system('{} {}'.format('python', cwd))

def SOS ():
        os.system('{} {}'.format('python', crd))
        
url = 'https://api.myjson.com/bins/ph58c'
cwd = os.path.join(os.getcwd(), "final.py --shape-predictor shape_predictor_68_face_landmarks.dat --alarm alarm.wav")
crd = os.path.join(os.getcwd(), "send_sms.py")
while True:
	response = urlopen(url)
	json_obj = json.load(response)
	print(json_obj)
	for i in json_obj:

		if i['drowsybutton'] ==1:
			print('Clicked')
			r = requests.put(url, json=[{"drowsybutton":0,"alarm":0,"accident":0,"sos":0}])
			t = threading.Thread(target = drowsy, name = 'thread1')
			t.start()
			break
			
		elif i['drowsybutton'] ==0:	
			print('Not Clicked')

		if i['sos']==0:
			print('Safe')
		elif i['sos']==1:
			print('SOS!!')
			r = requests.put(url, json=[{"drowsybutton":0,"alarm":0,"accident":0,"sos":0}])
			t = threading.Thread(target = SOS, name = 'thread2')
			t.start()
			break
