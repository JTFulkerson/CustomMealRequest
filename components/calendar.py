# ----------------------------------------------------------------------------
# Created By: John Fulkerson
# Created Date: 4/29/2023
# ----------------------------------------------------------------------------

from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta


def create_calendar_event(start_time, end_time, location, notes):
    # Load credentials from a service account file
    credentials = service_account.Credentials.from_service_account_file(
        'service_account.json')

    # Build the calendar API client
    service = build('calendar', 'v3', credentials=credentials)

    # Define the event details
    event = {
        'summary': 'New event',
        'location': location,
        'description': notes,
        'start': {
            'dateTime': start_time,
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'UTC',
        },
        'reminders': {
            'useDefault': True,
        },
    }

    # Call the Calendar API to create the event
    event = service.events().insert(calendarId='primary', body=event).execute()

    print(f'Event created: {event.get("htmlLink")}')


# Example usage: create an event for 3pm on April 19th, 2023 at the Googleplex in Mountain View, CA with a note
start_time = datetime(2023, 4, 19, 15, 0, 0).isoformat()
end_time = (datetime(2023, 4, 19, 15, 0, 0) + timedelta(hours=1)).isoformat()
location = 'Googleplex, Mountain View, CA'
notes = 'Meet with the Google Calendar team to discuss the API'

create_calendar_event(start_time, end_time, location, notes)
