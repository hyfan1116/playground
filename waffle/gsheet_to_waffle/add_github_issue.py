'''
Make an issue on github using API V3 and Python
https://gist.github.com/JeffPaine/3145490
'''

import os
import json
import requests

# Authentication for user filing issue (must have read/write access to
# repository to add issue to)
USERNAME = 'haoyang-f'
PASSWORD = os.environ('gp')

# The repository to add this issue to
REPO_OWNER = 'udacity'
REPO_NAME = 'robotics-beta-test-issues'

def make_github_issue(title, body=None, labels=[]):
    '''Create an issue on github.com using the given parameters.'''
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
    # Create an authenticated session to create the issue
    session = requests.Session()
    session.auth = (USERNAME, PASSWORD)
    # Create our issue
    issue = {'title': title,
             'body': body,
             'labels': labels}
    # Add the issue to our repository
    r = session.post(url, json.dumps(issue))
    if r.status_code == 201:
        print ('Successfully created Issue "%s"' % title)
    else:
        print ('Could not create Issue "%s"' % title)
        print ('Response:', r.content)

make_github_issue('test script')
