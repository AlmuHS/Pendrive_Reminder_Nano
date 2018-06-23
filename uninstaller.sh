#!/bin/bash

#If script is executed as non-root user, reject
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
else
	#Remove scripts folder
	if test -d /usr/bin/pendrive-reminder
	then
		rm -rf /usr/bin/pendrive-reminder
	fi

	#Remove locale files
	find /usr/share/locale/ -name "preminder*" -delete

	#Remove polkit rules and policy file	
	rm /usr/share/polkit-1/rules.d/10-inhibit-shutdown.rules

	#Remove xdg autostart entrt
	rm /etc/xdg/autostart/preminder.desktop
	
fi
