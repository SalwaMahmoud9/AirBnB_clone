#!/usr/bin/python3
"""Console."""
import cmd




class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    def do_quit(self, args):
        '''Quit command to exit the program
        '''
        quit()
        return True

    def do_EOF(self, args):
        '''Handles end of file'''
        return True

    def emptyline(self):
        '''dont execute anything when user
           press enter an empty line
        '''
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
