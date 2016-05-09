# Induction Cooktop

The aim of this project was to control an induction cooktop from a web application.

The proposed solution was to design a home automation system that has two modes - Auto and Manual. In the Manual mode, the user will choose a temperature level and the LEDs will switch on to emulate the corresponding heating intensity. In the Auto mode, the web application will display the current temperature and the system will automatically switch the LED lights to represent the level of heating being measured. Real time temperature analysis is made on ThingSpeak.

## Device sketch

<div style="text-align:center"><img src ="https://github.com/gabimachado/cooktop-IoT/blob/master/doc/cooktop_sketch.jpg" /></div>

## IoT Level
<div style="text-align:center"><img src ="https://github.com/gabimachado/cooktop-IoT/blob/master/doc/iot_level.jpg" /></div>

## Hardware

 - Raspberry Pi 2 Model B
 - DS18B20 Digital Temperature Sensor
 - 3 light-emitting diode (LED)
 - GPIO Extension Board
 - Breadboard
 - Resistors and wires

## Software

  - Native controller in Python 
  - Web server based on Django REST framework
  - SQLite3
  - ThingSpeak
  - ThingView

## Network

  The Raspberry Pi 2 uses a WIFI dongle to post data to the server through WAN. The ThingSpeak API stores and retrieves data using HTTP over the internet. On ThingView app it is possible to visualize the logged data from the temperature sensor on any Android 4.X.X Smartphone

## Process Model

<div style="text-align:center"><img src ="https://github.com/gabimachado/cooktop-IoT/blob/master/doc/process_model.png" /></div>

## Visualization
  
  Using the ThingSpeak and ThingView applications, the user can access the latest readings from the sensor.
  
  <div style="text-align:center"><img src ="https://github.com/gabimachado/cooktop-IoT/blob/master/doc/ThingView_re.png" /></div>
  
## References

  - Professor Kevin W. Lu's [GitHub] (https://github.com/kevinwlu/iot)
  - Rafael Bezerra's [GitHub] (https://github.com/rafaelbezerra-dev/)
  - EE - 800 L - Special Problems in EE - Professor Kevin W. Lu class notes 
  - [Australian Robotics] (http://www.australianrobotics.com.au/news/how-to-talk-to-thingspeak-with-python-a-memory-cpu-monitor)
  - [Adafruit] (https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/ds18b20)
  
  



