# dog-cam
RasPi camera project to make time-lapse video of dog walks.

Raspberry Pi Zero W running Raspbian Buster Lite and official camera.

The Pi runs on a power bank with 2a output and a 1a output powers a WiFi dongle. The process will monitor the SSID so that caamera capture only occurs when the Pi connects to the mobile WiFi.

Apache2 installed.
Python code will control the camera capture and update the default web page on the Pi. This allows monitoring the process whilst mobile.

The project uses the picamera package which gives a pure Python interface to the camera:

python3-picamera installed. https://picamera.readthedocs.io/
