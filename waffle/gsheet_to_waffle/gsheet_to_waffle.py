# http://gspread.readthedocs.io/en/latest/
# https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
# alternate: https://github.com/nithinmurali/pygsheets
import gspread
from oauth2client.service_account import ServiceAccountCredentials
'''share the sheet to: haoyang@spreadsheet2waffle.iam.gserviceaccount.com'''

#Make an issue on github using API V3 and Python
#https://gist.github.com/JeffPaine/3145490
import json
import requests


# Authentication for user filing issue (must have read/write access to
# repository to add issue to)
USERNAME = 'haoyang-f'
PASSWORD = os.environ('gp')

# The repository to add this issue to
REPO_OWNER = 'udacity'
REPO_NAME = 'robotics-beta-test-issues'

# Google Sheet information
SHEETNAME = 'Term 2 beta testing localization feedback'
SHEETLABELINISSUE = 'Localization'

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

def gsheet_to_issue_title(row):
    '''parse the Google Sheet row to Github Issue'''
    title = row[2] + ' | ' + row[4] + ' | ' + row[5]
    body = row[0] + '\n' + row[1] + '\n' + row[3] + '\n' + row[6]
    label = SHEETLABELINISSUE
    return title, body, [label]

def main():
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('google_secret.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open(SHEETNAME).sheet1

    # Extract and print all of the values
    #list_of_hashes = sheet.get_all_records()
    #print(list_of_hashes)

    with open("gsheet_to_waffle.txt") as file:
        row_last = int(file.readline())

    row_count = sheet.row_count #10

    row = sheet.row_values(row_last)
    if(row[0] != ''):
        index = row_last
        while (row[0] != '') and (index <= row_count):
            title, body, labels = gsheet_to_issue_title(row)
            make_github_issue(title, body, labels)

            index += 1
            row = sheet.row_values(index)

    print (index)

    if(index != row_last):
        # store new row_last in the txt file
        with open("gsheet_to_waffle.txt","w") as file:
            file.write(str(index))

if __name__ == '__main__':
    main()
