# Pendrive_Reminder_Nano
Little tool to avoid accidentally forgetting connected pendrives

Based in [Pendrive Reminder](https://github.com/AlmuHS/Pendrive_Reminder)

## About

This is a reimplementation of [Pendrive Reminder](https://github.com/AlmuHS/Pendrive_Reminder), with a simpler structure.

In this version, the UDev rules are replaced by a simple UDisks query.
This way It can check the pendrive existence more easily than the original implementation, and detect more key cases than this.

## Disadvantages

  -  This version does not support polkit < 0.106
  -  Less efficient than previous version
  -  There is no notification to advice when a device has been connected or disconnected.


## Advantages
	
  - Supports more usecase than previous version
     - Now It detects the pendrive connection made before system start.
     - It's doesn't matter when and how many desktop sessions is started: the dbus client will be always available 

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

Also, It can be necessary to install some dependencies.

- **Fedora**:

      sudo dnf install dbus-python pygobject3 python3-gobject libnotify

- **Arch Linux**:

      sudo pacman -S python-dbus python-gobject libnotify

- **Gentoo**:

      sudo emerge -a dev-python/dbus-python dev-python/pygobject x11-libs/libnotify

- **Debian**:

  Debian install polkit 0.105 by default, so this program will not work there.
  However, It's possible to install polkit 0.114 from experimental repository, following these steps:
  
  https://github.com/AlmuHS/Pendrive_Reminder/wiki/Instalar-Polkit-0.114-en-Debian
  
  After install polkit 0.114, you need to install the other dependencies:
  
      sudo apt install libnotify-bin policykit-1 python-gobject python3-dbus


### Installation locations

The scripts and the dbus client will be copied in `/usr/bin/pendrive-reminder/`

The polkit rule will be copied in `/usr/share/polkit-1/rules.d/`

The locale files will be copied in `/usr/share/locale`, in the directories for each language.

The desktop launcher will be copied in `/etc/xdg/autostart`

## Uninstallation

To uninstall it, simply execute `uninstaller.sh` as root.

The uninstaller will delete the app directory, the polkit rule, and the locale files.

The program can be uninstalled while it is running, even if there is any lock enabled.

The uninstaller will also break all locks that have been set in the system, allowing a correctly shutdown.

This uninstaller will not remove the dependency packages previously installed.
