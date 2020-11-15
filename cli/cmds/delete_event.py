from cli.cmds import AbsCommand


class DeleteEvent(AbsCommand):
    name = 'Delete Event'

    def execute(self):
        idx = int(input("Provide task index:\n"))
        self.events.delete_event(idx)
