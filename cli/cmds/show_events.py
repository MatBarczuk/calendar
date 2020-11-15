from cli.cmds import AbsCommand


class ShowEvents(AbsCommand):
    name = 'Show Events'

    def execute(self):
        for event in self.events.get_events():
            print(event)
