# -*- coding: utf-8-*-
import requests

WORDS = ["BEER"]



def handle(text, mic, profile):
    """
        Reports the current time based on the user's timezone.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """

    mic.say("Here's a beer!")

    response = requests.post('http://4.35.101.62:2020/vendSlot/4')
    printText(response)


    # httpServ = httplib.HTTPConnection("http://4.35.101.62:2020", 80)
    # httpServ.connect()
    # httpServ.request('POST', '/vendSlot/4', '')

    # response = httpServ.getresponse()
    # if response.status == httplib.OK:
    #     printText (response.read())
    # httpServ.close()

def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bbeer\b', text, re.IGNORECASE))


if __name__ == "__main__":
    handle('dsf', null, null)
