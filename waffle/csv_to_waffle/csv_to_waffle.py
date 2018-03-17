#! /usr/bin/python2.7

'''
Read redshift lesson feedback and populate waffleboard
'Make an issue on github using API V3 and Python'
https://gist.github.com/JeffPaine/3145490
'''

# -- Standard Imports
import json
import os
import requests
import argparse

# -- Third-party Imports
import pandas as pd

# -- Local Imports


__author__    = "Haoyang Fan"
__email__     = "haoyang@udacity.com"
__copyright__ = "Udacity (c) 2018"

# -- Define Functions
def get_args():
   '''Gets the arguments from the command line'''
   parser = argparse.ArgumentParser("Populates lesson feedback to waffleboard")

   # -- Create the descriptions for the commands
   o_desc = "The repo owner (e.g. Udacity)"
   o_name = "udacity"

   r_desc = "The repo name"

   u_desc = "The username to connect to waffle.io"

   p_desc = "The password to connect to waffle.io"

   c_desc = "The path and filename to csv feedback file"

   # -- Create the arguments
   parser.add_argument("-o", help= o_desc, default = o_name)
   parser.add_argument("-r", help= r_desc)
   parser.add_argument("-u", help= u_desc)
   parser.add_argument("-p", help= p_desc, default = os.environ.get('wp', ''))
   #parser.add_argument("-p", help= p_desc, default = "robond2018")
   parser.add_argument("-c", help= c_desc)
   args = parser.parse_args()

   return args

# received	given_title	nd_key	lesson_key	rating
# suggestions	content_version	received_at	account_key
def csv_row_to_issue_title(row):
    '''parse the csv file from Redshift row to Github Issue'''
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
    labels = [row[GIVEN_TITLE], row[CONTENT_VERSION]]
    return title, body, labels

def make_github_issue(args, title, body=None, labels=[]):
    '''Create an issue on github.com using the given parameters.'''
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % (args.o, args.r)

    # Create an authenticated session to create the issue
    session = requests.Session()
    session.auth = (args.u, args.p)

    # Create our issue
    issue = {'title': title,
             'body': body,
             'labels': labels}

    # Add the issue to our repository
    r = session.post(url, json.dumps(issue))
    if r.status_code == 201:
        print 'Successfully created Issue {0}'.format(title)
    else:
        print 'Could not create Issue {0}'.format(title)
        print 'Response:', r.content
    return

def csv_to_issue(args):
    df = pd.read_csv(args.c, delimiter="|")
    m = df.as_matrix()
    for row in m:
        # -- process each row
        title, body, labels = csv_row_to_issue_title(row)

        if "Positive" in title or len(body) == 0:
            continue

        make_github_issue(args, title, body, labels)

def main():
    args = get_args()
    csv_to_issue(args)

if __name__ == '__main__':
    main()
