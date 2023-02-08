import cmd

class HBNBCommand(cmd.Cmd):
    """A simple Air BnB command-line interface."""
    
    prompt = '(hbnb) '
        
    def do_clear(self, args):
        """Clear the terminal.
        """
        print("\033c", end="")
        
    def do_quit(self, args):
        """Quit command to exit the program. 
        """
        return True
    
    def do_EOF(self, args):
        """Exit the command-line interface.
        """
        return True    

    def default(self, line):
        """Handle unknown commands.
        """
        print("Unknown command:", line)

    def emptyline(self):
        """Print an empty line.
        """
        print(end='')



if __name__ == '__main__':
    HBNBCommand().cmdloop()
