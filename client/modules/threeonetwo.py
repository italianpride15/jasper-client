# -*- coding: utf-8-*-
import requests
import re

WORDS = ["THREE ONE TWO", "ONE", "TWO", "THREE", "THREE-ONE-TWO", "3-1-2"]

def handle(text, mic, profile):

    mic.say("Here is a three one two")

    response = requests.post('http://4.35.101.62:2020/vendSlot/3')
    print response

def isValid(text):
    """
        Returns True if input is related to beer.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bthree\b|\bone\b|\btwo\b|\bthree\-one\-two\b|\b3\-2\-1\b', text, re.IGNORECASE))
