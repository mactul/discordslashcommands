class Option:
    """
    Represents an option to add to a Command object
    """
    def __init__(self, name: str, description: str, type: int, required: bool):
        self.name = name
        self.description = description
        self.type = type
        self.required = required
        self.choices = []
        self._returned = False


    def add_choice(self, name, value):
        """
        add a choice to the option, name and value can be equals
        """
        self.choices += [{"name": name, "value": value}]


    def __str__(self):
        return '<Option name="'+self.name+'", description="'+self.description+'", type='+str(self.type)+', required='+str(self.required)+'>'


class ReturnedOption:
    """
    simplified option
    """
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self._returned = True


    def __str__(self):
        return str(self.value)
