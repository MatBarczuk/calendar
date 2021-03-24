from cli import Cli
from cli.cmds import CreateEvent, UpdateEvent, ShowEvents, DeleteEvent, SortEvents, FilterEvents, CancelFilter

cmds = (CreateEvent, ShowEvents, UpdateEvent, SortEvents, FilterEvents, CancelFilter, DeleteEvent)
cli = Cli(cmds)

cli.run()
