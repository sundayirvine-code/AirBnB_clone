from models.base_model import BaseModel

class State(BaseModel):
    """The State class inherits from BaseModel and represents a State of the application.

    Attributes:
        name (str): The name of the state.
    """
    name = ''

    def __init__(self, *args, **kwargs):
        """This method initializes the State class and calls its parent's __init__ method.

        Args:
            *args: Arguments passed to the parent's __init__ method.
            **kwargs: Keyword arguments passed to the parent's __init__ method.
        """
        super().__init__(*args, **kwargs)
