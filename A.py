#!/usr/bin/python3
import cmd

class MyCLI(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """
    prompt = '>> '
    intro = 'Welcome to MyCLI. Type "help" for available commands.'

    def do_hello(self, line):
        """Print a greeting."""
        eval(f"self.do_EOF")()
        print("Hello, World!")
        print(line)

    def do_EOF(self, line):
        """nnn"""
        return True

    def do_quit(self, line):
        """Exit the CLI."""
        return True

if __name__ == '__main__':
    MyCLI().cmdloop()