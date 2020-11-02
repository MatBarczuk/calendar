from event import Event
from user import User
from random import randint


user = User('Mateusz', 'mateusz@gmail.com')
print(user)

# event = Event('meeting', '5/11/21 15:00', 30, '', '', '')
# print(event)

events_list = []

for idx in range(50):
    event = Event(f'kebab {idx}', f'{randint(1, 25)}/{randint(1, 11)}/21 {randint(1, 23)}:30', {randint(6, 200)}, '',
                  '', '')
    events_list.append(event)

for event in events_list:
    print(event)
