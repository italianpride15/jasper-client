# -*- coding: utf-8-*-
import requests
import re

WORDS = ["MODELO", "MODE", "DELL", "MOAT"]

def handle(text, mic, profile):

    mic.say("Vending MODELO")

    response = requests.post('http://4.35.101.62:2020/vendSlot/2')
    print response

def isValid(text):
    """
        Returns True if input is related to beer.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bmodelo\b|\bmode\b|\bdell\b|\bmoat\b', text, re.IGNORECASE))