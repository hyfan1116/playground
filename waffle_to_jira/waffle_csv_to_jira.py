#! /usr/bin/python2.7

'''
Read redshift lesson feedback and populate JIRA board
'''

# -- Standard Imports
import argparse
import json
import os

# -- Third-party Imports
import pandas as pd
import requests

# -- Local Imports


__author__    = "Haoyang Fan"
__email__     = "haoyang@udacity.com"
__copyright__ = "Udacity (c) 2018"

# -- Define Functions
def get_args():
   '''Gets the arguments from the command line'''
   parser = argparse.ArgumentParser("Populates lesson feedback to waffleboard")

   # -- Create the descriptions for the commands
   j_desc = "The JIRA board name"
   c_desc = "The path and filename to csv feedback file"
   u_desc = "The username for JIRA board"
   t_desc = "The token used to authorize JIRA board"

   # -- Create the arguments
   parser.add_argument("-j", help = j_desc)
   parser.add_argument("-c", help = c_desc)
   parser.add_argument("-u", help = u_desc)
   parser.add_argument("-t", help = t_desc, default = os.environ.get('jp', ''))

   args = parser.parse_args()

   return args

# received	given_title	nd_key	lesson_key	rating
# suggestions	content_version	received_at	account_key
def csv_row_to_issue_title(row):
    '''Parse the csv file from Redshift row to JIRA board'''
    # Indices
    INDEX           = 0
    RECEIVED        = 1
    GIVEN_TITLE     = 2
    ND_KEY          = 3
    LESSON_KEY      = 4
    RATING          = 5
    SUGGESTIONS     = 6
    CONTENT_VERSION = 7
    RECEIVED_AT     = 8
    ACCOUNT_KEY     = 9

    title = '[' + row[RATING] + ']' + row[RECEIVED]
    body = row[SUGGESTIONS]
    # no space in labels of JIRA tickets
    labels = [row[GIVEN_TITLE].replace(' ', ''), row[CONTENT_VERSION]]
    return title, body, labels

def jira_create(args, session, title, body, labels):
    '''Create a JIRA issue'''
    url = 'https://udacity.atlassian.net/rest/api/2/issue'
    data = {
        "fields": {
           "project":
           {
              "key": args.j
           },
           "summary": title,
           "description": body,
           "issuetype": {
              "name": "Bug"
           },
           "labels": labels
        }
    }

    # Add the issue to our repository
    response = session.post(url, json=data)

    #print r.text
    print json.loads(response.text)
    print response.status_code

def csv_to_jira(args):
    '''Read data from CSV file and create JIRA tickets'''
    # https://developer.atlassian.com/server/jira/platform/jira-rest-api-examples/
    session = requests.Session()
    session.auth = (args.u, args.t)

    df = pd.read_csv(args.c, delimiter="|")
    m = df.as_matrix()
    for row in m:
        # -- process each row
        title, body, labels = csv_row_to_issue_title(row)

        # Check if the first letter is P for "Positive"
        if "Positive" in title or len(body) == 0:
            continue

        jira_create(args, session, title, body, labels)

def main():
    '''Populate JIRA board using lesson feedback CSV'''
    args = get_args()
    csv_to_jira(args)

if __name__ == '__main__':
    main()
