from cli import Cli
from cli.cmds import CreateEvent, UpdateEvent, ShowEvents, DeleteEvent, SortEvents, FilterEvents, CancelFilter
from events import Events

cmds = (CreateEvent, ShowEvents, UpdateEvent, SortEvents, FilterEvents, CancelFilter, DeleteEvent)
cli = Cli(cmds)

cli.run()
