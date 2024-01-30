from experimental import SpotifyPlayer
import paho.mqtt.client as paho
from paho import mqtt
import time
import logging
Music = {
    "F5 D6 85 75" : '6LQf6ErCI7vw7KGKRP11zP',
    "56 20 B8 89" : '2MvwYhejHpLfBcptTEWhDL'
}
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)-8s - %(name)-14s - %(message)s')
# edge is preferred (and is now default) because reading cookies in chrome > 104.0.5112.102 needs elevation
# https://github.com/borisbabic/browser_cookie3/issues/180



client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("Burapat1729", "gtav6789")


def on_connect(self, client, userdata, rc,_):
    print("MQTT Connected.")
    self.subscribe("spotify/command")
def on_message(client, userdata,msg):
    msg = msg.payload.decode("utf-8", "strict")
    print(msg)
    msg = msg.split(';')
    print(msg)
    if (msg[0] == 'play') :
        try :
            spotifyplayer.command(spotifyplayer.play(Music[msg[1]]))
        except :
            print('err')
        time.sleep(3)
    if(msg[0]=='command') :
        if (msg[1] == 'pause'):
            spotifyplayer.command(spotifyplayer.pause)
            time.sleep(3)
        elif (msg[1] == 'resume') :
            spotifyplayer.command(spotifyplayer.resume)
            time.sleep(3)
        
try :
    spotifyplayer = SpotifyPlayer(browser='edge')
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("db720833556244658ce539317e02f7b7.s1.eu.hivemq.cloud", 8883)
    client.loop_forever()
except :
    spotifyplayer.disconnect()