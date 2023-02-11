### Project: 0x00. AirBnB clone  

#### Intro:  
The goal of the project is to deploy on your server a simple copy of the AirBnB website.  
Its a web application composed of:  
- `A command interpreter` to manipulate data without a visual interface, like in a Shell
- `A website` (the front-end) that shows the final product to everybody: static and dynamic
- `A database` or `files` that store data (data = objects)
- `An API` that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)  

#### Project Description  
The first step in building the clone is to put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of future instances. The serialization/deserialization process will have a simple flow:  
`Instance <-> Dictionary <-> JSON string <-> file`.  

#### CLASSES
Next, we create all the classes used for the AirBnB that inherit from the `BaseModel`. They include:  
- User
- State
- City
- Place
- Review
- Amenity

All our models are located in the `AirBnB/ models` directory.  

##### BaseModel  
Serves as a base model for other classes in the project. The class contains common attributes and methods for all subclasses.  
The `__init__` method initializes the `id`, `created_at` and `updated_at` attributes If no arguments are passed  
A unique `id` is generated using the `uuid` library and the current datetime is used as the value for both `created_at` and `updated_at`. The instance is then saved to the storage.  
The `__str__` method returns a string representation of the object.  
The `save` method updates the `updated_at` attribute with the current datetime and saves the object to the storage.  
The `to_dict` method returns a dictionary representation of the object. The values of `updated_at` and `created_at` are converted to string in ISO format and the key `__class__` is added with the value being the class name.  

##### User  
Defines a class `Use`r that inherits from the `BaseModel` class. The User class contains attributes for `email`, `password`, `first name`, and `last name`.  

##### State  
Defines a class `State` that inherits from the `BaseModel` class. The State class contains a single attribute for the `name` of the state.  

##### Review  
Defines a class `Review` that inherits from the `BaseModel` class. The `Review` class contains attributes for `place id`, `user id`, and `text` of the review.  


##### Place  
Defines a class `Place` that inherits from the `BaseModel` class. The Place class contains attributes for: 
- city id 
- user id 
- name 
- description 
- number of rooms 
- number of bathrooms 
- maximum number of guests 
- price per night 
- latitude 
- longitude
- list of amenity ids  

##### City  
Defines a class `City` that inherits from the `BaseModel class`. The `City` class contains attributes for `state id` and `name`.

##### Amenity  
Defines a class `Amenity` that inherits from the `BaseModel` class. The `Amenity` class contains an attribute for `name`.  

##### N/B:  
The `__init__` method of all derived classes calls the `__init__` method of the parent class `BaseModel` using the `super()` function, which initializes the `id`, `created_at` and `updated_at` attributes. This ensures that all the attributes and methods defined in the BaseModel class are also available in the derived classes as well.  

#### FILE STORAGE  
We then create the  first abstracted storage engine of the project.  
It is located in the file `Air_BnB_clone/models/engine/file_storage.py`  
This is a well-structured implementation of a file storage system that can serialize instances of classes into a JSON file and deserialize the JSON file back into instances.  
The `FileStorage` class has methods for adding new objects to the storage, saving the storage to a file, reloading the storage from a file, and retrieving the entire storage.  
It uses a dictionary `__objects` to store the instances, where the keys are strings in the format of `<class_name>.<id>` and the values are the instances.   
The location of the JSON file is specified by the `__file_path` class attribute, which is set to "file.json".  
The `new` method sets a new object in the storage, by creating a string key for the object using its class name and ID, and setting the object as the value.  
The `save` method serializes the objects in the storage into a JSON file.  
The `reload` method deserializes the JSON file back into the storage, creating instances of the appropriate class based on the name stored in the key of each object in the file.  
The `all` method simply returns the `__objects` dictionary.   


#### THE LINK  
The `__init__.py` file located in `AirBnB_clone/models/__init__.py` links our storage engine `Air_BnB_clone/models/engine/file_storage.py` to all our `BaseModel` and `console`.  
It creates an instance of the `FileStorage`class, which provides an interface to save and load instances to and from a JSON file.    
With the `reload` method, the file storage will attempt to deserialize the JSON file and populate the `__objects` dictionary with the deserialized instances. This will allow you to access your instances in the future without having to create them again.  


#### THE CONSOLE  
We then create a custom  CLI for the AirBnB project, allowing users to interact with the program through a terminal.  
It is located at `AirBnB_clone/console.py`.  
It implements several functionalities in the class `HBNBCommand` which is a subclass of `cmd.Cmd`. These functionalities include:
- creating a new instance 
- showing an instance 
- destroying an instance
- displaying all instances.  

The `do_create` method creates a new instance of a class and saves it.  
The `do_show` method displays a string representation of an instance based on its class name and id.  
The `do_destroy` method deletes an instance based on its class name and id.  
The `do_all` method prints all string representations of instances, filtered by class name if provided.  
The `do_update` method updates an instance with new attributes, or creates a new attribute if it doesn't exist.

