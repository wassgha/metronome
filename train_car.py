import argparse
import picamera
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw
from firebase import firebase
import time

TRAIN_ID = 10011
CAR_ID = 7
CAR_NUMBER = 0

STATION_LIST = [0,1,2,3]

print(firebase)

firebase = firebase.FirebaseApplication('https://metronome-nyc.firebaseio.com', None)

def takephoto():
    camera = picamera.PiCamera()
    camera.capture('image.jpg')

def detect_face(face_file, max_results=4):
    client = vision.ImageAnnotatorClient()

    content = face_file.read()
    image = types.Image(content=content)

    return client.face_detection(image=image).face_annotations


def highlight_faces(image, faces, output_filename):
    im = Image.open(image)
    draw = ImageDraw.Draw(im)

    for face in faces:
        box = [(vertex.x, vertex.y)
               for vertex in face.bounding_poly.vertices]
        draw.line(box + [box[0]], width=5, fill='#00ff00')

    im.save(output_filename)

takephoto()
static_index = 1

with open('image.jpg', 'rb') as image:
    faces = detect_face(image, 50)
    print('Found {} face{}'.format(
        len(faces), '' if len(faces) == 1 else 's'))

    print('Writing to file {}'.format('output.jpg'))

    image.seek(0)
    # highlight_faces(image, faces, 'output.jpg')
    train_car = {
            'timestamp' : time.time(),
            'train_id' : TRAIN_ID,
            'car_id' : CAR_ID,
            'how_full' : len(faces),
            'station_id' : STATION_LIST[station_index]
    }

    result = firebase.post('/history', train_car)
    print result




