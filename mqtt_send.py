from __future__ import print_function
import paho.mqtt.publish as publish
import psutil
import string
import random

def send_data_to_cloud(latitude, longitude, var1, var2):

    channelID = "464861"
    writeAPIKey = "4IZ9QOGWUHLXIFJS"
    mqttHost = "mqtt.thingspeak.com"
    mqttUsername = "TSMQTTRpiDemo"
    mqttAPIKey = "TAF0GHYL9DZF6RJN"
    tTransport = "websockets"
    tPort = 80
    topic = "channels/" + channelID + "/publish/" + writeAPIKey
    clientID = "ToporAuto"

    payload = "field1=" + str(latitude) + "&field2=" + str(longitude) + "&field5=" + str(var1) + "&field6=" + str(var2)

    try:
        publish.single(topic, payload, hostname=mqttHost, transport=tTransport, port=tPort,
                       auth={'username': mqttUsername, 'password': mqttAPIKey})
        print(" Published Latitude =", latitude, " Longitude = ", longitude, " var1 = ", var1, " var2 =", var2)

    except:
        print("There was an error while publishing the data.")




#send_data_to_cloud(-23, 45, 123,45)
