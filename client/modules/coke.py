# -*- coding: utf-8-*-
import requests
import re

WORDS = ["COKE", "COAT"]

def handle(text, mic, profile):

    mic.say("Vending COKE")

    response = requests.post('http://4.35.101.62:2020/vendSlot/8')
    print response

def isValid(text):
    """
        Returns True if input is related to beer.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bcoke\b|\bcoat\b', text, re.IGNORECASE))
