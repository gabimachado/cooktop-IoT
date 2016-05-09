##How to create your own device

First of all, you need to prepare your Raspberry Pi. Using the Terminal, follow the steps below:

* Installing Django and REST Framework
<div style="text-align:center"><img src ="https://github.com/gabimachado/cooktop-IoT/blob/master/doc/django.png" /></div>

* Starting the Django Project
<div style="text-align:center"><img src ="https://github.com/gabimachado/cooktop-IoT/blob/master/doc/myapp.png" /></div>

* Django REST API - your REST API must be exactly as follows:
<div style="text-align:center"><img src ="https://github.com/gabimachado/cooktop-IoT/blob/master/doc/restapi.png" /></div>

* Run Web and Native Services
<div style="text-align:center"><img src ="https://github.com/gabimachado/cooktop-IoT/blob/master/doc/djangoserver.png" /></div>

* Log In in your Django user
<div style="text-align:center"><img src ="https://github.com/gabimachado/cooktop-IoT/blob/master/doc/admin.png" /></div>

* At the first time, post the following:
<br>
**manual** to the mode list at **http://127.0.0.1:8000/mode/**
<div style="text-align:center"><img src ="https://github.com/gabimachado/cooktop-IoT/blob/master/doc/mode.png" /></div>

**off** to the state list at **http://127.0.0.1:8000/state/**
<div style="text-align:center"><img src ="https://github.com/gabimachado/cooktop-IoT/blob/master/doc/state.png" /></div>
<br>

* Run the Controller
<div style="text-align:center"><img src ="https://github.com/gabimachado/cooktop-IoT/blob/master/doc/controller.png" /></div>

* View the app from a browser at http://127.0.0.1:8000/home 
<div style="text-align:center"><img src ="https://github.com/gabimachado/cooktop-IoT/blob/master/doc/index.png" /></div>
<br>
Now, you're able to create your own Induction Cooktop Controller prototype.
<br>
To analyze the temperature data, follow the next steps:
* Signup for ThingSpeak
<div style="text-align:center"><img src ="https://github.com/gabimachado/cooktop-IoT/blob/master/doc/thingspeak.png" /></div>

* Login to ThingSpeak
<div style="text-align:center"><img src ="https://github.com/gabimachado/cooktop-IoT/blob/master/doc/login.png" /></div>

* Create a channel for your data
<div style="text-align:center"><img src ="https://github.com/gabimachado/cooktop-IoT/blob/master/doc/channel.png" /></div>

* Name your project
<div style="text-align:center"><img src ="https://github.com/gabimachado/cooktop-IoT/blob/master/doc/proj.png" /></div>

* Update your channel

* Get an API Key
<div style="text-align:center"><img src ="https://github.com/gabimachado/cooktop-IoT/blob/master/doc/key.png" /></div>

* Modify your controller.py according to your API Key
