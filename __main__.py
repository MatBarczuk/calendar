from datetime import datetime

from event import Event
from events import Events
from user import User
from random import randint


def make_calendar():
    user = User('Mateusz', 'mateusz@mail.com')
    print(user)

    events = Events()
    for idx in range(50):
        event = Event(f'kebab {idx}', f'{randint(1, 25)}/{randint(1, 11)}/21 {randint(1, 23)}:30', randint(6, 200),
                      'Kraków', f'{user}', '')
        events.add_event(event)

# for event in events.get_events():
#     print(event)
# print(events.delete_event(6))

# print(events.get_event(6))
    events.sort_config = ['start_time']

    events.filter_config = {
     'duration': {'min': None, 'max': 50},
     'start_time': {'min': datetime.strptime('1.2.21', '%d.%m.%y'), 'max': datetime.strptime('31.10.21', '%d.%m.%y')}
    }

    for event in events.get_events():
        print(event)
    print(len(list(events.get_events())))


if __name__ == '__main__':
    make_calendar()
