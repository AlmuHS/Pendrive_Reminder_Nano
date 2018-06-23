# Pendrive_Reminder_Nano
Little tool to avoid accidentally pendrive forgets, for GNU/Linux

Based in [Pendrive Reminder](https://github.com/AlmuHS/Pendrive_Reminder)

## About

This is a reimplementation of [Pendrive Reminder](https://github.com/AlmuHS/Pendrive_Reminder), with a simpler structure.

In this version, the UDev events are replaced by a simple UDisks query.
As this form, we can check the pendrive existence easily that the original implementation, and detect more problematic situation than before

## Disadvantages

  -  This version don't supports polkit < 0.106
  -  It's a little less efficient than previous version

## Advantages
	
  - Supports more usecase than previous version
     - Now we can detect the pendrive connection made before system start.
     - Don't matter when and how the desktop session is started: the dbus client will be always available 


