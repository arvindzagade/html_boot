#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import json
import requests
url='..../rfid'

reader = SimpleMFRC522.SimpleMFRC522()

try:
        id, text = reader.read()
        print(id)
        print(text)
        ret = requests.post(url,data = {'Number':id})
finally:
        GPIO.cleanup()