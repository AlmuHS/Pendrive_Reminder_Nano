#!/bin/bash

#Script linked to 10-inhibit-shutdown polkit rule
#This script check if watchdog file exists in the system
#If don't exists, return 0 (correct)
#else return 1(error)


exists=$(/usr/bin/pendrive-reminder/aux_scripts/check_pendrive.py)

exit $exists

