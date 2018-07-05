# -*- coding: iso-8859-1 -*-
import sys, time, serial

serialPort = '/dev/ttyACM1'


def infoSerial():
    print('\nComunication details')
    # Serial Connection
    arduinoPort = serial.Serial(serialPort, 9600, timeout=1)

    # Reset Arduino manual
    arduinoPort.setDTR(False)
    time.sleep(0.3)
    # Delete data from the buffer
    arduinoPort.flushInput()
    arduinoPort.setDTR()
    time.sleep(0.3)

    print('\nPort state: %s ' % (arduinoPort.isOpen()))
    print('Device name: %s ' % (arduinoPort.name))
    print('Configuration Dump:\n %s ' % (arduinoPort))
    print('\n###############################################\n')
    # Close connection
    arduinoPort.close()


if __name__ == '__main__':
    infoSerial()

