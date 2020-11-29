from cli.cmds import AbsCommand


class SortEvents(AbsCommand):
    name = 'Sort Events'

    def execute(self):
        self.events.sort_config = input('Provide sorting parameter/s:\n').split(', ')
        self.events.get_events()
