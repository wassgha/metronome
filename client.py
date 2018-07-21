from socketIO_client import SocketIO, LoggingNamespace

def on_connect():
    print('connect')

def on_disconnect():
    print('disconnect')

def on_reconnect():
    print('reconnect')

def on_triggerCamera(*args):
    print('trigger_camera received', args)

socketIO = SocketIO('127.0.0.1', 8000, LoggingNamespace)
socketIO.on('connect', on_connect)
socketIO.on('disconnect', on_disconnect)
socketIO.on('reconnect', on_reconnect)

# Listen only once
socketIO.once('trigger_camera', on_triggerCamera)

