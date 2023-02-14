#!/usr/bin/python3
""" Tests class console """
import unittest
from unittest.mock import patch
from io import StringIO
import os
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """ Tests console """

    @classmethod
    def setUpClass(cls):
        """ Creates an instance """
        cls.console = HBNBCommand()

    @classmethod
    def teardown(cls):
        """ Deletes the instance """
        del cls.console

    def tearDown(self):
        """ Removes the JSON file """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_docstrings(self):
        """ Checks methods for docstrings """
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_empty(self):
        """ Tests the emptyline method """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual('', f.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        console = HBNBCommand()
        console.onecmd('')
        self.assertEqual('', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_help(self, mock_stdout):
        console = HBNBCommand()
        console.onecmd('help')
        mv = mock_stdout.getvalue()
        self.assertIn('Documented commands (type help <topic>):', mv)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        console = HBNBCommand()
        console.onecmd('create State')
        self.assertNotEqual('', mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_missing_class_name(self, mock_stdout):
        console = HBNBCommand()
        console.onecmd('create')
        self.assertEqual('** class name missing **\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_nonexistent_class(self, mock_stdout):
        console = HBNBCommand()
        console.onecmd('create SomeNonexistentClass')
        mv = mock_stdout.getvalue()
        self.assertEqual('** class doesn\'t exist **\n', mv)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        console = HBNBCommand()
        console.onecmd('create State')
        obj_id = mock_stdout.getvalue().strip()
        mock_stdout.truncate(0)
        console.onecmd('show State {}'.format(obj_id))
        self.assertNotEqual('', mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_missing_class_name(self, mock_stdout):
        console = HBNBCommand()
        console.onecmd('show')
        self.assertEqual('** class name missing **\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_nonexistent_class(self, mock_stdout):
        console = HBNBCommand()
        console.onecmd('show SomeNonexistentClass 123')
        mv = mock_stdout.getvalue()
        self.assertEqual('** class doesn\'t exist **\n', mv)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_missing_id(self, mock_stdout):
        console = HBNBCommand()
        console.onecmd('show State')
        self.assertEqual('** instance id missing **\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_nonexistent_instance(self, mock_stdout):
        console = HBNBCommand()
        console.onecmd('show State 123')
        self.assertEqual('** no instance found **\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        console = HBNBCommand()
        console.onecmd('create State')
        obj_id = mock_stdout.getvalue().strip()
        mock_stdout.truncate(0)
        console.onecmd('destroy State {}'.format(obj_id))
        self.assertEqual('', mock_stdout.getvalue())
        mock_stdout.truncate(0)
        console.onecmd('show State {}'.format(obj_id))
        # self.assertEqual('** no instance found **\n', mock_stdout.getvalue())
