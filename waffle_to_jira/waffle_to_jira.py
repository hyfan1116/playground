'''
Import issues from Waffle board 'Ready'
to JIRA Board Backlog
Then move the waffle tickets to 'Filed'
Keep the assignee information
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


__author__    = "Haoyang Fan"
__email__     = "haoyang@udacity.com"
__copyright__ = "Udacity (c) 2018"

GITHUB_OWNER = "udacity"
GITHUB_REPO = "robotics-nanodegree-issues"
JIRA_BOARD_KEY = "ROBND"

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

def get_github_json(args, url):
    ''' Send GET request to GitHub REST API url'''
    # Create an authenticated session to create the issue
    session = requests.Session()
    session.auth = (args.u, args.p)

    # send request to our repository
    response = session.get(url)
    if response.status_code == 200:
        json_body = json.loads(response.content)
    else:
        sys.exit("Cannot reach GitHub: " + response.content)
    return json_body

def get_github_issues(args):
    '''
    Get issues on github.com using the given parameters.
    Generate a bar chart of issues remaining.
    '''
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % \
        (GITHUB_OWNER, GITHUB_REPO)

    # to do waffle board cards
    url_filter = url + '?state=open&labels=Ready'
    issues = get_github_json(args, url_filter)
    return issues

def delete_github_issue_label(args, issue_url, label):
    ''' Delete label from an issue '''
    # Create an authenticated session to create the issue
    session = requests.Session()
    session.auth = (args.u, args.p)
    # Get intial cookies for the session
    _ = session.get('https://github.com/login')

    # Delete old label
    url = issue_url + '/labels/' + label

    # send request to our repository
    response = session.delete(url)
    if response.status_code == 200:
        print('Old label deleted') # json.loads(response.content)
    else:
        sys.exit("Cannot reach GitHub: " + str(response.status_code))

def add_github_issue_label(args, issue_url, label):
    ''' Add label to issue using issue's url '''
    # Create an authenticated session to create the issue
    session = requests.Session()
    session.auth = (args.u, args.p)
    # Get intial cookies for the session
    _ = session.get('https://github.com/login')

    # Add new label
    url = issue_url + '/labels'

    # send request to our repository
    labels = json.dumps([label])
    response = session.post(url, data = labels)
    if response.status_code == 200:
        print('New label added') # json.loads(response.content)
    else:
        sys.exit("Cannot reach GitHub: " + str(response.content))

    return

def update_github_issue_label(args, issue_url, old, new):
    ''' Update the issue's label from old to new '''
    delete_github_issue_label(args, issue_url, old)
    add_github_issue_label(args, issue_url, new)

def get_github_user_email(args, username):
    ''' Query for user email address using username '''
    url = 'https://api.github.com/users/%s' % username
    email = get_github_json(args, url)["email"]
    return email

def get_jira_username_by_email(args, email):
    ''' Get username in JIRA via email '''
    session = requests.Session()
    session.auth = (args.e, args.t)

    url = 'https://udacity.atlassian.net/rest/api/2/user/search?'
    url += 'username=' + email.replace('@', '%40')
    response = session.get(url)
    if response.status_code == 200:
        json_body = json.loads(response.content)
    else:
        sys.exit("Cannot reach JIRA: " + str(response.content))
    return json_body[0]['name']

def create_jira_ticket(args, key, title, body, assignee):
    '''Create a JIRA ticket'''
    # Create an authenticated session to create the issue
    session = requests.Session()
    session.auth = (args.e, args.t)

    url = 'https://udacity.atlassian.net/rest/api/2/issue'
    data = {
        "fields": {
           "project":
           {
              "key": key
           },
           "summary": title,
           "description": body,
           "issuetype": {
              "name": "Bug"
           },
           "labels": ["Waffle"],
           "assignee": {"name": assignee}
        }
    }

    # Add the issue to our repository
    response = session.post(url, json=data)
    if response.status_code == 201:
        json_body = json.loads(response.content)
    else:
        sys.exit("Cannot reach JIRA: " + str(response.content))

def create_jira_tickets(args, issues):
    '''Create JIRA tickets from issues'''
    # https://developer.atlassian.com/server/jira/platform/jira-rest-api-examples/
    for issue in issues:
        # check if the issues was filed
        filed_flag = False
        for label in issue['labels']:
            if label['name'] == 'filed':
                filed_flag = True
                break
        if filed_flag:
            continue

        # file the issue if the issue was not filed
        jira_title = issue["title"]
        jira_body = issue["html_url"]+'\n'+issue["body"]
        jira_assignee_email = get_github_user_email(args, issue["assignee"]["login"])
        jira_assignee = get_jira_username_by_email(args, jira_assignee_email)
        create_jira_ticket(args, JIRA_BOARD_KEY, jira_title, jira_body, jira_assignee)
        github_url = issue["url"]
        # update_github_issue_label(args, github_url, 'ready', 'in progress')
        add_github_issue_label(args, github_url, 'filed')
        print('filed issue ' + github_url)
    return

def waffle_to_jira(args):
    '''Fetch issues from Waffle (Github) then create JIRA tickets'''
    issues = get_github_issues(args)
    create_jira_tickets(args, issues)

def main():
    args = get_args()
    waffle_to_jira(args)

if __name__ == '__main__':
    main()
