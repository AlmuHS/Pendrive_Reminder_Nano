#!/usr/bin/python3

#Script linked to 10-inhibit-shutdown polkit rule
#This script check if there are any usb mass storage device connected in the system

#To get this, the script execute a udisks2 query, using dbus and udisks2-api

#If there are any pendrive connected -> return 1 (error)
#else -> return 0 (correct)

#This value is returned to polkit using sys.exit()

#Based in https://askubuntu.com/questions/437031/finding-volume-label-of-a-usb-mass-storage-device-using-python


import dbus
import sys

def get_usb():
    devices = []
    bus = dbus.SystemBus()
    ud_manager_obj = bus.get_object('org.freedesktop.UDisks2', '/org/freedesktop/UDisks2')
    om = dbus.Interface(ud_manager_obj, 'org.freedesktop.DBus.ObjectManager')

    for k,v in om.GetManagedObjects().items():
        drive_info = v.get('org.freedesktop.UDisks2.Drive', {})

        if drive_info.get('ConnectionBus') == "usb" and drive_info.get('Removable') and drive_info.get('Size') > 0:
            return 1
    return 0


exists_pendrive = get_usb()
sys.exit(exists_pendrive)
