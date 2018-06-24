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
            return 1
    return 0


exists_pendrive = get_usb()
sys.exit(exists_pendrive)
