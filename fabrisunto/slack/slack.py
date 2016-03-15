# -*- coding: UTF-8 -*-
import os, requests, json, time

class Slack:
    '''Common Class for notifcation objects'''

    def __init__(self, url):
        self.url = url
        
    def genSlackMsg(msg,channel,emoji): 
        smsg = {"text": msg, "channel": channel,"icon_emoji": emoji}
        return smsg

    def notifySlack(url,msg):
        payload=msg
        r = requests.post(url, json=payload)
