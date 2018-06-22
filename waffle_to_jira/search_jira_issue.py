'''
Import issues from Waffle board 'Ready' to JIRA Board Backlog
'''

# -- Standard Imports
import argparse
import datetime
import json
import os
import sys

# -- Third-party Imports
import numpy as np
import pandas as pd
import requests

# -- Local Imports


# -- Define Functions
def get_args():
   '''Gets the arguments from the command line'''
   parser = argparse.ArgumentParser("Populates lesson feedback to waffleboard")

   # -- Create the descriptions for the commands
   u_desc = "The username to connect to waffle.io"
   p_desc = "The password to connect to waffle.io"
   e_desc = "The email address to sign in JIRA"
   t_desc = "The token used to sign in JIRA"

   # -- Create the arguments
   parser.add_argument("-u", help = u_desc, default = 'haoyang-f')
   parser.add_argument("-p", help = p_desc, default = os.environ.get('wp', ''))
   parser.add_argument("-e", help = e_desc, default = 'haoyang@udacity.com')
   parser.add_argument("-t", help = t_desc, default = os.environ.get('jt', ''))
   args = parser.parse_args()

   return args

def get_jira(args, url, jql):
    ''' Send GET request to JIRA '''
    # Create an authenticated session to create the issue
    session = requests.Session()
    session.auth = (args.e, args.t)

    response = session.get(url+jql)
    if response.status_code == 200:
        json_body = json.loads(response.content)
        return json_body
    else:
        sys.exit("Cannot reach JIRA: " + response.content)

def search_jira_ticket(args):
    '''Create a JIRA ticket'''
    url = 'https://udacity.atlassian.net/rest/api/2/search?jql='
    #jql = 'project=GLADOS&maxResults=2'
    jql = 'assignee=haoyang&maxResults=2'
    
    results = get_jira(args, url, jql)
    # print(results['issues'][0])
    print(results['total'])
    print(len(results['issues']))

def main():
    args = get_args()
    search_jira_ticket(args)

if __name__ == '__main__':
    main()
