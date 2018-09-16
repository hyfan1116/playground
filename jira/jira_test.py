#! /usr/bin/python2.7

'''
Read redshift lesson feedback and populate JIRA board
'''

# -- Standard Imports
import argparse
import json
import os
import sys

# -- Third-party Imports
import pandas as pd
import requests

# -- Local Imports


__author__    = "Haoyang Fan"
__email__     = "haoyang@udacity.com"
__copyright__ = "Udacity (c) 2018"

JIRA_Token = os.environ("jt")

def jira_search(session):

    # https://www.atlassian.com/blog/jira-software/jql-the-most-flexible-way-to-search-jira-14
    # query JIRA using jql
    url = 'https://udacity.atlassian.net/rest/api/2/search'
    data = {"jql":'project = GLADOS AND status = "In Progress"'}

    # Send the request
    r = session.post(url, json=data) # json.dumps(data)

    #print r.text
    print json.loads(r.text)
    print r.status_code

def jira_create(session):
    '''Create a JIRA issue'''
    url = 'https://udacity.atlassian.net/rest/api/2/issue'
    data = {
        "fields": {
           "project":
           {
              "key": "GLADOS"
           },
           "summary": "REST ye merry gentlemen.",
           "description": "Creating of an issue using project keys and issue type names using the REST API",
           "issuetype": {
              "name": "Bug"
           }
        }
    }

    # Add the issue to our repository
    r = session.post(url, json=data) # json.dumps(data)

    #print r.text
    print json.loads(r.text)
    print r.status_code

def main():
    # https://developer.atlassian.com/server/jira/platform/jira-rest-api-examples/
    username = 'haoyang@udacity.com'
    token = JIRA_Token

    session = requests.Session()
    session.auth = (username, token)
    #jira_search(session)
    jira_create(session)


if __name__ == '__main__':
    main()
