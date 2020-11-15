from cli.cmds import NoCommand


class Cli:
    def __init__(self, cmds):
        self.cmds = cmds

    def get_commands(self):
        return {cls.name: cls for cls in self.cmds}

    def parse_command(self, cmd):
        cmds = self.get_commands()
        command = cmds.setdefault(cmd, NoCommand)
        return command(cmd)

    def get_user_command(self):
        for idx, cmd in enumerate(self.get_commands()):  # TODO choose by number and names
            print(f'{idx + 1}. {cmd}')

        user_command = input('Choose command\n')
        command = self.parse_command(user_command)
        command.execute()

    def run(self):
        while True:
            self.get_user_command()

# TODO complete CLI
