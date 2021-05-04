import sys
import os
from shutil import copy2, move

class Shell:

    def __init__(self):
        self.shell_on = True
        self.path = os.getcwd()
    
    def handler(self, command):
        command = command.split()
        ans = None
        try:
        	ans = getattr(Shell, command[0])(self, command[1:])
        except AttributeError:
        	ans = "There is no such command in this shell realization"
        except Exception as e:
            ans = "An exception occured: " + str(e)
        return ans      
    
    def run(self):
        print("The shell in on!")
        command = input()
        while(command != "exit"):
            ans = self.handler(command)
            if ans != None:
                print(ans)
            command = input()
            
    def hello(*args):
        return "Hello"

    def pwd(self, *args):
        return self.path

    def ls(self, args):
        if len(args) > 1:
            return "Wrong parametrs are given"
        answer = ''
        path = '' if len(args)==0 else args[0]
        for data in os.listdir(os.getcwd() + '/' + path):
            answer += (str(data) + '\n')
        return answer

    def mkdir(self, name):
        if len(name) != 1:
            return "Wrong parametrs are given"
        elif name[0] not in os.listdir(self.path):
            os.mkdir(self.path + '/' + name[0])
            return
        return "The directory with such name already exists"

    def rmdir(self, name):
        if len(name) != 1:
            return "Wrong parametrs are given"
        elif name[0] in os.listdir(self.path):
            if len(os.listdir(self.path + '/' + name[0])) == 0:
                os.rmdir(self.path + '/' + name[0])
            return 'This directory is not empty'
        return "There is no directory named " + name[0]

    def rm(self, name):
        if len(name) != 1:
            return "Wrong parametrs are given"
        elif name[0] in os.listdir(self.path):
            os.remove(self.path + '/' + name[0])
            return
        return "There is no file named " + name[0]

    def touch(self, name):
        if len(name) != 1:
            return "Wrong parametrs are given"
        open(self.path + '/' + name[0], 'w')

    def cd(self, new_path):
        if len(new_path) != 1:
            return "Wrong parametrs are given"
        try:
            os.chdir(new_path[0])
            self.path = os.getcwd()
        except:
            return "Such directory does not exist"

    def cp(self, names):
        if len(names) != 2:
            return "Wrong parametrs are given"
        elif names[0] in os.listdir(self.path):
            copy2(names[0], names[1])
            return
        return "There is no file named " + names[0]

    def mv(self, names):
        if len(names) != 2:
            return "Wrong parametrs are given"
        elif names[0] in os.listdir(self.path):
            move(names[0], names[1])
            return
        return "There is no file named " + names[0]

    def echo(self, message):
        return ' '.join(message)

    def python(self, name):
        if len(name) != 1:
            return "Wrong parametrs are given"
        elif name[0] in os.listdir(self.path):
            with open(self.path + '/' + name[0], 'r') as File:
                global print
                original_print = print
                logger = []
                print = lambda x : logger.append(x)
                exec(File.read())
                print = original_print
                answer = ''
                for data in logger:
                    answer += (str(data) + '\n')
                return answer
        return "There is no file named " + name[0]
        
    def cat(self, name):
        if len(name) != 1:
            return "Wrong parametrs are given"
        if name[0] in os.listdir(self.path):
            with open(self.path + '/' + name[0], 'r') as File:
                return File.read()
        return "There is no file named " + name

if __name__ == '__main__':
    shell = Shell()
    shell.run()
