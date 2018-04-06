import pynmea2
import serial
import array

def get_gps_rmc_string():
    serialport = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)

    uart_array = array.array('c',)
    in_char = ''

    while True:
        while in_char != '$':
            in_char = serialport.read()

        for x in range(5):
            uart_array.append(serialport.read())
            print str(uart_array)
            string_to_cond = uart_array.tostring()
            print "done " + str(string_to_cond)
            if string_to_cond == "GPRMC":
                while in_char != '\n':
                    in_char = serialport.read()
                    uart_array.append(in_char)
                rmc_string = uart_array.tostring()
                end_flag = 1
                return rmc_string
                #print str(rmc_string)
