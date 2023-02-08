import uuid 
from datetime import datetime

class BaseModel:
    """A base class to be inherited by subsequent classes"""

    def __init__(self):
        """Initializes the id, created_at, and updated_at attributes."""

        # Generate a random UUID using uuid4 and convert it to a string
        self.id = str(uuid.uuid4())

        # Get the current time and store it as a datetime object
        now = datetime.now()
        self.created_at = now
        self.updated_at = now

    def __str__(self):
        """Returns a string representation of the object."""

        return f"[{self.__class__.__name__}]({self.id}) {self.__dict__}>"

    def save(self):
        """Updates the updated_at attribute with the current datetime."""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the object."""

        my_dict = self.__dict__.copy()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict

