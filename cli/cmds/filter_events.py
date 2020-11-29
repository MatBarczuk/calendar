from cli.cmds import AbsCommand


class FilterEvents(AbsCommand):
    name = 'Filter Events'

    def execute(self):
        parameter = input('Provide parameter:\n')
        min_val = input(f'Provide min value of chosen parameter ({parameter}):\n')
        max_val = input(f'Provide max value of chosen parameter ({parameter}):\n')
        if parameter == 'duration':
            min_val = int(min_val)
            max_val = int(max_val)
        self.events.filter_config = {parameter: {'min': min_val, 'max': max_val}}
