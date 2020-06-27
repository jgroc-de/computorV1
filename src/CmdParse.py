import readline
import cmd
from src.computor import main

class CmdParse(cmd.Cmd):
    prompt = ">>> "

    def default(self, line):
        if line == 'EOF' or line == 'exit' or line == 'exit()':
            print()
            exit()
        main(line)
