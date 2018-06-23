#!/usr/bin/python3

import dbus
import sys

def get_usb():
    devices = []
    bus = dbus.SystemBus()
    ud_manager_obj = bus.get_object('org.freedesktop.UDisks2', '/org/freedesktop/UDisks2')
    om = dbus.Interface(ud_manager_obj, 'org.freedesktop.DBus.ObjectManager')

    for k,v in om.GetManagedObjects().items():
        drive_info = v.get('org.freedesktop.UDisks2.Block', {})
        if drive_info.get('IdUsage') == "filesystem" and not drive_info.get('HintSystem') and not drive_info.get('ReadOnly'):
            device = drive_info.get('Device')
            device = bytearray(device).replace(b'\x00', b'').decode('utf-8')
            devices.append(device)

    if len(devices) > 0:
        return 1
    else:
        return 0 


print(get_usb())
sys.exit(get_usb())
