# ARDUINO-DJANGO LED TOGGLE
## This is a Public repo created for the purpose of learning to integrate Arduino with Django app

## How to demo:
* Upload the code provided on [ino file](./arduino_django_led.ino) to the arduino with necessary adjustments being done.
* Connect the Arduino to a COM port. 
* Start the django server 
    - Create a Virtual Environment 
        ``` 
        py -m venv .venv
        ```
    - Install dependencies 
        ```
        pip install -r requirements.txt
        ```

    - rename ```.env-sample``` to ```.env``` and fill in the values according to your configuration 

    - Runserver
        on machine only
        ``` 
        py manage.py runserver 
        ```
        or on the network
        ```
        py manage.py runserver 0.0.0.0:8000
        ```
    - goto ```http://localhost:8000/``` or ```http:<host's ip>:8000/```


### ABOUT :
    Created by @hehenischal on github, not my proudest repo.

### CONTACT: 
    https://nishallamichhane.com.np


