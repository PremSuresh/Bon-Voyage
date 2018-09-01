import requests

r = requests.put('http://api.myjson.com/bins/ph58c', json=[{"drowsybutton":0,"alarm":0,"accident":0,"sos":0}])
r.status_code
r.json()
