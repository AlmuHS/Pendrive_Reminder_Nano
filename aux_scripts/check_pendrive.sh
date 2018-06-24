#!/bin/bash

#Script linked to 10-inhibit-shutdown polkit rule
#This script call check_pendrive.py script, which execute a udisks query to check if there are any pendrive in the system.

#The script returns the output value gets from check_pendrive.py


exit $(/usr/bin/pendrive-reminder/aux_scripts/check_pendrive.py)

