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
        command_dict = {}
        for idx, cmd in enumerate(self.get_commands()):
            command_dict[idx + 1] = cmd
            print(f'{idx + 1}. {cmd}')

        user_command = input('Choose command\n')
        if user_command.isdigit():
            if int(user_command) in command_dict.keys():
                user_command = command_dict[int(user_command)]
        command = self.parse_command(user_command)
        command.execute()

    def run(self):
        while True:
            self.get_user_command()
