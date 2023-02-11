from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Class Amenity defines the amenities provided by the Place
    
    Attributes:
        name (str): the name of the Amenity
    """
    name = ''

    def __init__(self, *args, **kwargs):
        """
        Initializes the Amenity class and its attributes.
        
        Args:
            *args: variable length argument list
            **kwargs: Arbitrary keyword arguments
        
        Returns:
            None
        """
        super().__init__(*args, **kwargs)