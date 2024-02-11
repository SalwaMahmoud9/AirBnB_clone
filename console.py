#!/usr/bin/python3
"""Console."""
import cmd




class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """Shouldn’t execute anything."""
        pass

    def quit(self, arg):
        """Quit command to exit the program."""
        return True

    def EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
