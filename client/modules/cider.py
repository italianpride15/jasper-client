# -*- coding: utf-8-*-
import requests
import re

WORDS = ["CIDER"]

def handle(text, mic, profile):

    mic.say("Vending CIDER")

    response = requests.post('http://4.35.101.62:2020/vendSlot/5')
    print response

def isValid(text):
    """
        Returns True if input is related to beer.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bcider\b', text, re.IGNORECASE))
