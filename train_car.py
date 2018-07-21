
from firebase import firebase

firebase = firebase.FirebaseApplication('https://metronome-nyc.firebaseio.com', None)


train_car = 'first train!!'

result = firebase.post('/history', train_car)
print result