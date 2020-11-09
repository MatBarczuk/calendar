from event import Event
from events import Events
from user import User
from random import randint


user = User('Mateusz', 'mateusz@gmail.com')
print(user)

# event = Event('meeting', '5/11/21 15:00', 30, '', '', '')
# print(event)

events = Events()
for idx in range(50):
    event = Event(f'kebab {idx}', f'{randint(1, 25)}/{randint(1, 11)}/21 {randint(1, 23)}:30', randint(6, 200), '',
                  '', '')
    events.add_event(event)

# for event in events.get_events():
#     print(event)
# print(events.delete_event(6))
# events.update_event(6, {'name': 'kolor'})
# events.update_event(6, {'duration': 25})
# # TODO add support for multiple updates
# print(events.get_event(6))
events.sort_config = ['duration']
for event in events.sort_event():
    print(event)
