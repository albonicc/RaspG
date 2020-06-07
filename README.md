#RaspG#

RaspG is the combination of "Raspberry" and "Garden". It is an automatized watering system that includes four sensors: temperature, air humidity, soil humidity and luminosity. These sensors are connected to an Arduino Nano who is responsible of gathering the data of those sensors. Later the Arduino sends all the data to a Raspberry Pi 3 Model B+, who is in charge of displaying the data in three differents ways: A GUI made with Electron, an 0.98 in OLED display and in a Wia Dashboard (https://www.wia.io/). 

##Prerequisites##

In order to run the application, it is necessary to install the following Node Modules using NPM:

```
npm install electron
```
```
npm install electron-reload
```
````
npm install python-shell
````
It is also necessary to download the DHT.h library for the Arduino code and to use Python 3.


