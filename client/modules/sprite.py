# -*- coding: utf-8-*-
import requests
import re

WORDS = ["SPRITE", "SPITE", "RIGHT"]

def handle(text, mic, profile):

    mic.say("Vending SPRITE")

    response = requests.post('http://4.35.101.62:2020/vendSlot/7')
    print response

def isValid(text):
    """
        Returns True if input is related to beer.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bsprite\b|\bspite\b|\bright\b', text, re.IGNORECASE))
