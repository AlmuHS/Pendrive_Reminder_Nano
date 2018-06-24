# Pendrive_Reminder_Nano
Little tool to avoid accidentally pendrive forgets, for GNU/Linux

Based in [Pendrive Reminder](https://github.com/AlmuHS/Pendrive_Reminder)

## About

This is a reimplementation of [Pendrive Reminder](https://github.com/AlmuHS/Pendrive_Reminder), with a simpler structure.

In this version, the UDev rules are replaced by a simple UDisks query.
As this form, we can check the pendrive existence easily that the original implementation, and detect more problematic situation than before

## Disadvantages

  -  This version don't supports polkit < 0.106
  -  It's a little less efficient than previous version

## Advantages
	
  - Supports more usecase than previous version
     - Now we can detect the pendrive connection made before system start.
     - Don't matter when and how the desktop session is started: the dbus client will be always available 

## Requirements

  - GNU/Linux
  - polkit >= 0.106
  - udisks2
  - libnotify
  - dbus
  - Python 3
    - python-dbus
    - pygobject
  - gettext

## Installation

To install this tool, simply download this repository and execute `install.sh` as root.

Also, can be necessary to install the dependencies.

- **Fedora**:

      sudo dnf install dbus-python pygobject3 python3-gobject at libnotify

- **Arch Linux**:

      sudo pacman -S python-dbus python-gobject at libnotify

- **Gentoo**:

      sudo emerge -a dev-python/dbus-python dev-python/pygobject sys-process/at x11-libs/libnotify

- **Debian**:
  Debian offers polkit 0.105 as default, but It's possible to install polkit 0.114 from experimental repository, following this steps 
  
  https://github.com/AlmuHS/Pendrive_Reminder/wiki/Instalar-Polkit-0.114-en-Debian
  
  To install another dependencies, you can to use:
  
      sudo apt install libnotify-bin policykit-1


### Installation locations

The scripts and the dbus client will be copied in `/usr/bin/pendrive-reminder/`

The polkit rule will be copied in `/usr/share/polkit-1/rules.d/`

The locale files will be copied in `/usr/share/locale`, in the directories from each language.

The desktop launcher will be copied in `/etc/xdg/autostart`
