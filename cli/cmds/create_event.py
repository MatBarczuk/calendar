from datetime import datetime

from cli.cmds import AbsCommand
from event import Event


class CreateEvent(AbsCommand):
    name = 'Create Task'

    def execute(self):
        event_name = input('Provide event name:\n')
        event_duration = int(input('Provide event duration:\n'))
        e = Event(event_name, '22/12/20 15:30', event_duration, '', '', '')
        self.events.add_event(e)
