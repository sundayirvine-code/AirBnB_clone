### Project: 0x00. AirBnB clone  

#### Intro:  
The goal of the project is to deploy on your server a simple copy of the AirBnB website.  
Its a web application composed of:  
- `A command interpreter` to manipulate data without a visual     interface, like in a Shell
- `A website` (the front-end) that shows the final product to everybody: static and dynamic
- `A database` or `files` that store data (data = objects)
- `An API` that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)  

#### Project Description  
The first step in building the clone is to put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of future instances. The serialization/deserialization process will have a simple flow:  
`Instance <-> Dictionary <-> JSON string <-> file`.  

Next, we create all the classes used for the AirBnB that inherit from the `BaseModel`. They include:  
- User
- State
- City
- Place
- Review
- Amenity

We then create the  first abstracted storage engine of the project: `File storage`.
