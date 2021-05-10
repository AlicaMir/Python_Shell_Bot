import sys
import os
from traceback import format_exc
from io import StringIO
from shutil import copy2, move
from pathlib import Path
from shell_replics import *


class Shell:
    def __init__(self):
        self.shell_on = True
        self.path = Path.cwd()

    def handler(self, command):
        parameters = command.split()[1:]
        command = command.split()[0]
        try:
            ans = getattr(Shell, command)(self, parameters)
        except AttributeError:
            ans = no_such_command
        except Exception as e:
            ans = exception_occured.format(str(e))
        return ans

    def run(self):
        print(greetings_line)
        command = input()
        while command != "exit":
            ans = self.handler(command)
            if ans != None:
                print(ans)
            command = input()

    def hello(*args):
        return hello_line

    def pwd(self, *args):
        return self.path

    def ls(self, args):
        answer = ""
        if len(args) == 0:
            args = [""]
        for path in args:
            path = self.path / Path(path)
            if not path.is_dir():
                answer += "\n" + no_dir.format(path)
                continue
            answer += "\n".join(os.listdir(path))
        return answer

    def mkdir(self, arg):
        if len(arg) != 1:
            return wrong_params
        path = self.path / Path(arg[0])
        if path.is_dir():
            return dir_exists
        path.mkdir()

    def rmdir(self, arg):
        if len(arg) != 1:
            return wrong_params
        path = self.path / Path(arg[0])
        if not path.is_dir():
            return dir_not_exist
        if len(os.listdir(path)) != 0:
            return dir_not_empty
        path.rmdir()

    def rm(self, arg):
        if len(arg) != 1:
            return wrong_params
        path = self.path / Path(arg[0])
        if not path.exists() or path.is_dir():
            return no_file.format(path)
        path.unlink()

    def touch(self, arg):
        if len(arg) != 1:
            return wrong_params
        path = self.path / Path(arg[0])
        path.touch()

    def cd(self, new_path):
        if len(new_path) != 1:
            return wrong_params
        new_path = self.path / Path(new_path)
        if not new_path.is_dir():
            return dir_not_exist
        self.path = new_path

    def cp(self, args):
        if len(args) != 2:
            return wrong_params
        from_path = Path(args[0])
        to_path = Path(args[1])
        if not from_path.exists():
            return no_file.format(path)
        copy2(from_path, to_path)

    def mv(self, args):
        if len(args) != 2:
            return wrong_params
        from_path = Path(args[0])
        to_path = Path(args[1])
        if not from_path.exists():
            return no_file.format(path)
        move(from_path, to_path)

    def echo(self, message):
        return " ".join(message)

    def python(self, arg):
        if len(arg) != 1:
            return wrong_params
        path = self.path / Path(arg[0])
        if not path.exists() or path.is_dir():
            return no_file.format(path)
        with path.open() as File:
            old_stdout = sys.stdout
            redirected_output = sys.stdout = StringIO()
            try:
                exec(File.read())
            except Exception as e:
                print(exception_occured.format(str(e)))
            finally:
                sys.stdout = old_stdout
            return redirected_output.getvalue()

    def cat(self, arg):
        if len(arg) != 1:
            return wrong_params
        path = self.path / Path(arg[0])
        if not path.exists() or path.is_dir():
            return no_file.format(path)
        with path.open() as File:
            return File.read()


if __name__ == "__main__":
    shell = Shell()
    shell.run()
