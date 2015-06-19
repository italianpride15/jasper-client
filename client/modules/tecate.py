# -*- coding: utf-8-*-
import requests
import re

WORDS = ["TECATE"]

def handle(text, mic, profile):

    mic.say("Here is a tecate")

    response = requests.post('http://4.35.101.62:2020/vendSlot/6')
    print response

def isValid(text):
    """
        Returns True if input is related to beer.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\btecate\b', text, re.IGNORECASE))
