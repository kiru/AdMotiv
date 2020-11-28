import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class CalendarAccess:

    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/calendar.events']
        self.service = self.connect()


    def connect(self):
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('../resources/secrets/token.pickle'):
            with open('../resources/secrets/token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    '../resources/secrets/credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('../resources/secrets/token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)
        return service

    def get_events(self, max_num = 10):
        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = self.service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=max_num, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        return events

    def get_event_start_time(self, event):
        return event['start'].get('dateTime', event['start'].get('date'))

    def get_all_events_start_time(self, events):
        return [self.get_event_start_time(event) for event in events]

    def get_event_description(self, event):
        return event["summary"]

    def get_all_events_description(self, events):
        return [self.get_event_description(event) for event in events]

    def get_event_end_time(self, event):
        return event['start'].get('dateTime', event['end'].get('date'))

    def get_all_events_end_time(self, events):
        return [self.get_event_end_time(event) for event in events]
