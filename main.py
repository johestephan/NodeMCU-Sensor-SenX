import esp
from machine import Pin, ADC
import machine
from time import sleep
import dht
from mqtt import MQTTClient
import this_config as TiCo

def sub_cb(topic, msg):
   print(msg)

def sendData(data):
    client = MQTTClient(TiCo.id, TiCo.broker_url, user=TiCo.user, password=TiCo.password, port=1883)
    client.set_callback(sub_cb)
    client.connect()
    #client.subscribe(topic=TiCo.topic)
    print(data)
    client.publish(topic=TiCo.topic, msg=str(data))


def readDHT():
    d = dht.DHT11(machine.Pin(2))
    d.measure()
    humid = d.humidity()
    temp = d.temperature()
    return {"temperature" : temp, "humidity" : humid}

def readMoist():
    pot = ADC(0)
    moist = pot.read()
    return {"Moisture" : moist}

def wifiConnect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(TiCo.ssid, TiCo.wifipass)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

def run():
    wifiConnect()
    data = {"d" : { "DHT" : readDHT(), "Soil" : readMoist()}}
    sendData(data)
    #esp.deepsleep(0)

run()
