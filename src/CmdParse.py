import cmd
from src.computor import Computor


class CmdParse(cmd.Cmd):
    prompt = ">>> "

    def __init__(self):
        self.computor = Computor()
        super().__init__()

    def default(self, line):
        if line == 'EOF' or line == 'exit' or line == 'exit()':
            print()
            exit()
        self.computor.computeAndPrint(line)
