#!/bin/bash

SYSTEM=$1

ampy -p /dev/ttyUSB0 -b 115200 put this_config.py.$SYSTEM this_config.py
ampy -p /dev/ttyUSB0 -b 115200 put mqtt.py
ampy -p /dev/ttyUSB0 -b 115200 put main.py
ampy -p /dev/ttyUSB0 -b 115200 put boot.py
