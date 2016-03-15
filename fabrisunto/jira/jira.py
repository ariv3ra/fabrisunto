# -*- coding: UTF-8 -*-
import os, requests, json, time

class Jira:
    '''Common Class for Jira objects'''

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    def qryJira(qry, usr, pwd):
        jira = requests.get(self.url+'search', params=qry, auth=(usr,pwd))

        return jira.json()

    def addJiraComment(projID, msg, usr, pwd):
        body = {"body": msg}
        jc = requests.post(self.url+'issue/'+projID+'/comment', json=body, auth=(usr,pwd))
        
    def startJiraIssue(projID, transID, usr, pwd):
        trans ={"transition":{"id":transID}}
        jt = requests.post(self.url+'issue/'+projID+'/transitions', json=trans, auth=(usr,pwd))
