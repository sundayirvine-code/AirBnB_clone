#!/usr/bin/python3
"""Script that implements a custom CLI for AirBnB project"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.__init__ import storage
import shlex
import re

class_map = {
    'BaseModel': BaseModel,
    'User': User,
    'Place': Place,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Review': Review,
}


class HBNBCommand(cmd.Cmd):
    """A simple Air BnB command-line interface."""

    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program.
        """
        return True

    def do_EOF(self, args):
        """Exit the command-line interface.
        """
        return True

    def emptyline(self):
        """Do not execute anything when an empty line is inputted.
        """
        pass

    def do_create(self, class_name):
        """Create a new instance of the specified class and save it.
            Args:
            class_name (str): The name of the class to create an instance of.

            Returns:
            None: If the class name is missing or does not exist.
            str: The instance id of the created object.
        """
        if not class_name:
            print('** class name missing **')

        elif class_name not in class_map:
            print("** class doesn't exist **")

        else:
            obj = class_map[class_name]()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """Display string representation of an instance
           based on the class name and id.
            Args:
            line (str): A string with class name and id separated by a space.

            Returns:
            None: If class name or instance id is missing, or class
            doesn't exist, or instance is not found.
            str: The string representation of the instance.
        """

        args = shlex.split(line)
        class_name, id = (args + [None, None])[:2]

        if not class_name:
            print("** class name missing **")
            return

        elif class_name not in class_map:
            print("** class doesn't exist **")
            return

        elif not id:
            print("** instance id missing **")
            return

        id = f"{class_name}.{id}"
        all_objs = storage.all()
        obj = all_objs.get(id, None)

        if obj:
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
            Args:
            line (str): The class name and id separated by a space.

            Returns:
            None: If class name is missing or class doesn't exist or
            instance id is missing or instance not found.
            None: Deletes the instance and saves the change in the JSON file.
        """
        args = shlex.split(line)
        # add each argument to the begining
        # of the list and pick the first two
        class_name, id = (args + [None, None])[:2]

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in class_map:
            print("** class doesn't exist **")
            return

        if not id:
            print("** instance id missing **")
            return

        id = f"{class_name}.{id}"
        all_objs = storage.all()

        obj = all_objs.get(id, None)

        if obj:
            # delete from dictionary
            del all_objs[id]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representations of all instances,
           filtered by class name if provided.

            Args:
            line (str): A string that may contain the name of a class to
            filter the instances by.

            Returns:
            None: If the class name is missing or does not exist.
            List[str]: A list of str rep. of all instances that match
            the class name, or all instances if no class name is provided.
        """
        args = shlex.split(line)
        class_name = (args + [None])[0]

        all_objs = storage.all()

        # class_name provided
        if class_name:
            if class_name not in class_map:
                print("** class doesn't exist **")
                return
            else:
                class_objects = [
                    value.__str__() for key, value in all_objs.items()
                    if key.startswith(f"{class_name}.")
                ]

                if len(class_objects) == 0:
                    print("** no instance found **")
                    return
                print(class_objects)

        # no argument provided
        else:
            all_class_objects =\
                [value.__str__() for value in all_objs.values()]
            if len(all_class_objects) == 0:
                print("** no instance found **")
                return
            print(all_class_objects)

    def do_update(self, line):
        """Updates an instance based on the class name and id
           by adding or updating attribute.
            Args:
            line (str): contains the parameters for the update command.

            Returns:
            None

            Raises:
            None
        """
        args = shlex.split(line)
        argc = len(args)
        class_name, id, attribute_name, attribute_value =\
            (args + [None, None, None, None])[:4]

        if not class_name:
            print("** class name missing **")
            return
        if class_name not in class_map:
            print("** class doesn't exist **")
            return

        if not id:
            print("** instance id missing **")
            return

        id = f"{class_name}.{id}"
        all_objs = storage.all()
        obj = all_objs.get(id, None)

        if obj is None:
            print("** no instance found **")
            return

        if not attribute_name:
            print("** attribute name missing **")
            return

        if not attribute_value:
            print("** value missing **")
            return

        if attribute_name in ['id', 'created_at', 'updated_at']:
            print("Cant update {}".format(attribute_name))
            return

        # Check if the attribute exists in the instance
        value = getattr(obj, attribute_name, None)
        if value:
            # get the type and then typecast the value to e stored
            t = type(value)
            setattr(obj, attribute_name, t(attribute_value))
            storage.save()

        else:
            # creating new attribute
            setattr(obj, attribute_name, attribute_value)
            storage.save()

    def default(self, line):
        """Handle unknown commands.
        """
        class_name, command = line.split('.')
        '''print(class_name, command)
        print()'''
        if class_name in class_map:
            if command == "all()":
                # Call the all command
                HBNBCommand.do_all(self, class_name)
            elif command == "count()":
                all_objs = storage.all()
                class_objects = [
                    value.__str__() for key, value in all_objs.items()
                    if key.startswith(f"{class_name}.")
                ]
                print(len(class_objects))
            elif command.startswith("show"):
                # Retrieve the Id
                pattern = r'\((.*?)\)'
                match = re.search(pattern, command)
                id = match.group(1)

                # Call the show command
                HBNBCommand.do_show(self, f"{class_name} {id}")

            elif command.startswith("destroy"):
                # Retrieve the Id
                pattern = r'\((.*?)\)'
                match = re.search(pattern, command)
                id = match.group(1)

                # Call the show command
                HBNBCommand.do_destroy(self, f"{class_name} {id}")

            elif command.startswith("update"):
                pattern = r'\((.*?)\)'
                match = re.search(pattern, command)
                id, attribute, value = match.group(1).split(',')
                s = f"{class_name} {id} {attribute} {value}"
                HBNBCommand.do_update(self, s)
            else:
                print("Unknown command:", line)
        else:
            print("Unknown command:", line)
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
