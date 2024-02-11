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
        exit(1)
        return True

    def EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        exit(1)
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
