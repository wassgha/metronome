
from firebase import firebase
import time

# constants
TRAIN_ID = 10011
CAR_ID = 7
CAR_NUMBER = 0

STATION_LIST = [0,1,2,3]

firebase = firebase.FirebaseApplication('https://metronome-nyc.firebaseio.com', None)


# this is the current station it's on
station_index = 1


train_car = {
	'timestamp' : time.time(),
	'train_id' : TRAIN_ID,
	'car_id' : CAR_ID,
	'how_full' : 0,
	'station_id' : STATION_LIST[station_index]
}

result = firebase.post('/history', train_car)
print result


