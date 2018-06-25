#!/usr/bin/python3

import dbus
import sys

def get_usb():
    devices = []
    bus = dbus.SystemBus()
    ud_manager_obj = bus.get_object('org.freedesktop.UDisks2', '/org/freedesktop/UDisks2')
    om = dbus.Interface(ud_manager_obj, 'org.freedesktop.DBus.ObjectManager')

    counter = 0;

    for k,v in om.GetManagedObjects().items():
        drive_info = v.get('org.freedesktop.UDisks2.Drive', {})

        if drive_info.get('ConnectionBus') == "usb" and drive_info.get('Removable') and drive_info.get('Size') > 0:
            return 1
    return 0


exists_pendrive = get_usb()
sys.exit(exists_pendrive)
