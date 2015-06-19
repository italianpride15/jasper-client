# -*- coding: utf-8-*-
import requests
import re
import random

WORDS = ["BEER", "BEING"]

def handle(text, mic, profile):
    """
        Distributes a random beer.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """

    mic.say("Here's a beer!")

    slot = random.randint(2, 9)
    print slot

    response = requests.post('http://4.35.101.62:2020/vendSlot/' + str(slot))
    print response

def isValid(text):
    """
        Returns True if input is related to beer.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bbeer\b|\bbeing\b', text, re.IGNORECASE))
