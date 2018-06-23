#!/bin/bash

#If script is executed as non-root user, reject
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
else
	#If polkit version is >= 0.106
	if test $(pkaction --version | cut -d " " -f 3 | cut -d "." -f 2) -ge 106
	then	

		INSTALL_DIR="/usr/bin/pendrive-reminder"

		#Copy auxiliar scripts
		mkdir $INSTALL_DIR 2>/dev/null
		cp -r aux_scripts/ $INSTALL_DIR
		chmod +x $INSTALL_DIR/aux_scripts/*

		#Copy locale files
		cp -r locale/* /usr/share/locale/

		#Copy polkit rules
		#copy rules file	
		cp polkit-rules/10-inhibit-shutdown.rules /usr/share/polkit-1/rules.d/

		#copy dbus-client
		cp -r dbus-client/ $INSTALL_DIR
		chmod ugo+x $INSTALL_DIR/dbus-client/client.py

		#Copy xdg launcher for dbus client
		cp xdg-launcher/preminder.desktop /etc/xdg/autostart

	else
		echo "This polkit version is not supported by Pendrive Reminder Nano. Download Pendrive Reminder from https://github.com/AlmuHS/Pendrive_Reminder"
	fi
fi
