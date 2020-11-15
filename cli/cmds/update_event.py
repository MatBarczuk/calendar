from cli.cmds import AbsCommand


class UpdateEvent(AbsCommand):
    name = 'Update Event'

    def execute(self):
        idx = int(input("Provide task index:\n"))
        config = input('Provide changes:\n')
        config_dict = {
            key: int(val) if val.isdigit() else val for key, val in [item.split(': ') for item in config.split(', ')]
        }
        self.events.update_event(idx, config_dict)
