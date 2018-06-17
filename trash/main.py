#!/usr/bin/env python

from requests import get
from tempfile import NamedTemporaryFile
from icalendar import Calendar
from icalendar import vDatetime
from itertools import groupby
from collections import namedtuple
from datetime import datetime
import locale

from trash.config import get_config

Event = namedtuple('Event', 'start description')
locale.setlocale(locale.LC_ALL, '')

def main():
    """ A tool to show the dates of garbage pickups """
    with NamedTemporaryFile() as temp:
        config = get_config()
        url = config['main']['ical_source']
        download(url, temp.name)
        events = read_events(temp.name)
        for start, summary in group_by_date(events):
            print('{}: {}'.format(start.strftime("%a %d.%m.%Y"), summary))


def download(url, file_name):
    """ Downloads a file from an url and 
        writes the content to a temporary file 
    """
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)


def read_events(file_name):
    """ Reads all events from an ics file """
    events = []
    with open(file_name, 'rb') as file:
        gcal = Calendar.from_ical(file.read())
        for vevent in gcal.walk('VEVENT'):
            event = Event(start=vevent['dtstart'].dt,
                          description=str(vevent['summary']))
            events.append(event)
    return events


def group_by_date(events):
    """ Groups a list of events by their start date and
        aggregates their descriptions into a summary
    """
    # to use groupby the list of events must be sorted first
    events.sort(key=lambda x: x.start)
    # group events by date
    grouped_events = []
    for key, group in groupby(events, lambda x: x[0]):
        summary = ' und '.join([event.description for event in group])
        grouped_events.append((key, summary))
    return grouped_events


if __name__ == '__main__':
    main()