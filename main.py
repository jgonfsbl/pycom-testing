import uos
import sys
import machine
import network
import pycom
from network import LTE
from network import WLAN
from network import Bluetooth
from network import LoRa


print('Device: ' + uos.uname().machine)
print('Firmware: ' + uos.uname().release)
print('Python: ' + sys.version)
print('MicroPython: ' + str(sys.implementation.version[0]) + '.' + str(sys.implementation.version[1]) + '.' + str(sys.implementation.version[2]))
print('===============================================================================')

print('Switching off Heartbeat')
pycom.heartbeat(False)
pycom.rgbled(0x000022)

print('Switching off WLAN')
wlan = network.WLAN()
wlan.deinit()

print('Switching off Server')
server = network.Server()
server.deinit()

print('Switching off Bluetooth')
bt = Bluetooth()
bt.deinit()

print('Switching off LoRa')
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868, power_mode=LoRa.SLEEP)

if (uos.uname().sysname == 'FiPy'):

    print('Switching off LTE')
    lte = network.LTE()
    quit = False
    while quit == False:
        try:
            lte.deinit()
        except OSError:
            print('  Exception occured, retrying...')
            pass
        else:
            quit = True

    print('Switching off Sigfox')
    # sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

print('Switching off RGB Led')
pycom.rgbled(0x000000)

print('===============================================================================')

print('Now entering idle... ')
while True:
    machine.idle()# Nothing
