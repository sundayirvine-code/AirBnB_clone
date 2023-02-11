from models.base_model import BaseModel

class User(BaseModel):
    """
    This class defines the User object and its attributes.
    It inherits the `BaseModel` class and adds the email, password,
    first_name, and last_name attributes.
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """
        Constructor for the User class
        Calls the parent (BaseModel) class's constructor
        """
        super().__init__(*args, **kwargs)
