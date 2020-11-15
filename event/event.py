from datetime import datetime
from helpers.helpers import uuid


class Event:
    def __init__(self, name, start_time, duration, location, owner, participants):
        self.id = uuid()
        self._name = name
        self._start_time = datetime.strptime(start_time, "%d/%m/%y %H:%M")
        self._duration = duration
        self._location = location
        self.owner = owner
        self.participants = participants
        self.created = datetime.now()

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, val):
        if val <= 5:
            raise ValueError(f"Meeting duration under 5 minutes doesn't make sense ({val}).")
        self._duration = val

    @property
    def time_to_event(self):
        time = self.start_time - datetime.now()
        days = time.days
        hours, remainder = divmod(time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f'{days} days, {hours} hours, {minutes} minutes.'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, new_start_time):
        self._start_time = datetime.strptime(new_start_time, "%d/%m/%y %H:%M")

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, new_location):
        self._location = new_location

    def __str__(self):
        return f'class Event(id: {self.id}, name: {self.name}, start time: {self.start_time}, ' \
               f'created: {self.created}, time to event: {self.time_to_event}, duration: {self._duration}, ' \
               f'location: {self.location}, owner: {self.owner})'
