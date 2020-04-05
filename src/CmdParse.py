import readline
import cmd
from src.computor import compute

class CmdParse(cmd.Cmd):
    prompt = ">>> "

    def default(self, line):
        if line == 'EOF' or line == 'exit' or line == 'exit()':
            print()
            exit()
        try:
            result = compute(line)
            print(result)
        except ValueError:
            pass
        except SyntaxError as error:
            print(error)
