from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime


# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'gcal_client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def get_cohort_calendar_id(service, cohort):
    '''Get deadline calendar id for cohort'''
    calendar_id = ''
    page_token = None
    while True:
        calendar_list = service.calendarList().list(pageToken=page_token).execute()
        for calendar_list_entry in calendar_list['items']:
            if(calendar_list_entry['summary'].lower().startswith(cohort)): # id: knowlabs.com
                calendar_id = calendar_list_entry['id']
        page_token = calendar_list.get('nextPageToken')
        if not page_token:
            break
    return calendar_id

def get_events(service, calendar_id, cohort):
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

    try:
        # print('Getting the upcoming 10 events in '+cohort)
        result = 'Getting the upcoming 10 events in ' + cohort + '\n'
        eventsResult = service.events().list(
            calendarId=calendar_id, timeMin=now, maxResults=10, singleEvents=True,
            orderBy='startTime').execute()
        events = eventsResult.get('items', [])

        if not events:
            #print('No upcoming events found.')
            result = 'No upcoming events found.'
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            #print(start, event['summary'])
            result += start + ' ' + event['summary'] + '\n'
        return result[:-1]

    except Exception as e:
        return 'Cannot connect to Google Calendar'


def list_events(cohort):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    calendar_id = get_cohort_calendar_id(service, cohort)
    return get_events(service, calendar_id, cohort)

def main():
    """Shows basic usage of the Google Calendar API."""
    list_events('RSEND Term 1 January')


if __name__ == '__main__':
    main()
