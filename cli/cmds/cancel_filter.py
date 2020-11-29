from cli.cmds import AbsCommand


class CancelFilter(AbsCommand):
    name = 'Cancel Filter'

    def execute(self):
        self.events.filter_config = {}
