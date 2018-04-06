#!/usr/bin/pytjjhon

from LIS3DH import LIS3DH
from time import sleep
from gps_nmea import get_gps_rmc_string
import pynmea2
from mqtt_send import send_data_to_cloud
from acc_data_process_15 import Acc_data

def trans_rmc_string_to_object(income_str):
    msg = pynmea2.parse(income_str)
    return msg



#def clickcallback(channel):
    # interrupt handler callback
#    print("Interrupt detected")
#    click = sensor.getClick()
#    print("Click detected (0x%2X)" % (click))
#    if (click & 0x10):
#        print(" single click")
#    if (click & 0x20):
#        print(" double click")


if __name__ == '__main__':
    sensor = LIS3DH(debug=True,datarate=LIS3DH.DATARATE_400HZ)
    sensor.setRange(LIS3DH.RANGE_8G)
    #sensor.setClick(LIS3DH.CLK_DOUBLE, 200, mycallback=clickcallback)

    # second accelerometer
    # s2 = LIS3DH(address=0x19, debug=True)

    print("Starting stream")
    acc_data = Acc_data()
    while True:

        x = sensor.getX()
        y = sensor.getY()
        z = sensor.getZ()

        item = {'x':x,'y':y,'z':z}
        # create ACC_DATA_PROC
        if(acc_data.process(item)):
            data_1, data_2 = acc_data.stat_get()
            rmc_obj = trans_rmc_string_to_object(get_gps_rmc_string())
            #print "Lalala !!!"
            send_data_to_cloud(rmc_obj.latitude, rmc_obj.longitude,data_1, data_2)
            #print str(rmc_obj.latitude) + " " + str(rmc_obj.longitude)

        print(item)
        #print("\rX: %.6f\tY: %.6f\tZ: %.6f" % (x, y, z))
        sleep(0.01)

    # click sensor if polling & not using interrupt
    #        click = sensor.getClick()
    #        if (click & 0x30) :
    #            print "Click detected (0x%2X)" % (click)
    #            if (click & 0x10): print " single click"
#            if (click & 0x20): print " double click"
