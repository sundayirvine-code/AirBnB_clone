#!/usr/bin/python3
""" Tests class console """
import unittest
from unittest.mock import patch
from io import StringIO
import os
import console
from console import HBNBCommand


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

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd('')
            self.assertEqual('', f.getvalue())

    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd('help')
            mv = f.getvalue()
            self.assertIn('Documented commands (type help <topic>):', mv)

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd('create State')
            self.assertNotEqual('', f.getvalue().strip())

    def test_create_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd('create')
            self.assertEqual('** class name missing **\n', f.getvalue())

    def test_create_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd('create SomeNonexistentClass')
            mv = f.getvalue()
            self.assertEqual('** class doesn\'t exist **\n', mv)

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd('create State')
            obj_id = f.getvalue().strip()
            f.truncate(0)
            console.onecmd('show State {}'.format(obj_id))
            self.assertNotEqual('', f.getvalue().strip())

    def test_show_missing_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd('show')
            self.assertEqual('** class name missing **\n', f.getvalue())

    def test_show_nonexistent_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd('show SomeNonexistentClass 123')
            mv = f.getvalue()
            self.assertEqual('** class doesn\'t exist **\n', mv)

    def test_show_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd('show State')
            self.assertEqual('** instance id missing **\n', f.getvalue())

    def test_show_nonexistent_instance(self):
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd('show State 123')
            self.assertEqual('** no instance found **\n', f.getvalue())

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            console = HBNBCommand()
            console.onecmd('create State')
            obj_id = f.getvalue().strip()
            f.truncate(0)
            console.onecmd('destroy State {}'.format(obj_id))
            self.assertEqual('', f.getvalue())
            f.truncate(0)
            console.onecmd('show State {}'.format(obj_id))
