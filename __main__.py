from cli import Cli
from cli.cmds import CreateEvent, UpdateEvent, ShowEvents, DeleteEvent
from events import Events

cmds = (CreateEvent, ShowEvents, UpdateEvent, DeleteEvent)
cli = Cli(cmds)

cli.run()
