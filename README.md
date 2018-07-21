*Winner of the Google Tech Intern Hackathon*

# Metronome

**Improving the train riding experience for all New Yorkers, one Raspberry Pi at a time!**

Metronome deploys low-power IoT devices that monitor and report the number of train riders on a per-car basis. Metronome then integrates with smart displays and indicator lights at stations' platforms to indicate to subway riders which cars are less crowded.

![Metronome display showing train arriving at the Times Square station](https://github.com/wassgha/metronome/blob/master/static/display.png?raw=true)

## Development

Install the following python requirements (you can use virtualenv):
```
sudo pip install requests
sudo pip install python-firebase
sudo pip install flask
sudo pip install flask_socketio
```

Run the server
```
cd server && python main.py
```

On metro surveillance cameras, run
```
python train_car.py
```
(uses Raspberry Pi Camera)

## Future work

Possible integration with existing feeds (MTA and Google Transit) sketched below

![Google Maps Train Capacity and Usage Sketch](https://github.com/wassgha/metronome/blob/master/static/maps.png?raw=true)
