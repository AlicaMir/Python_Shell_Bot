import sys
import os
from shutil import copy2, move


class Shell:


    def __init__(self):
        self.shellOn = True
        self.path = os.getcwd()
        
        
    def run(self):
        print("The shell is on!")
        while(self.shellOn):
            command = input().split()
            try:
            	getattr(Shell, command[0])(self, command[1:])
            except AttributeError:
            	print("There is no such command in this shell realization")
            except Exception as e:
                print("An exception occured: " + str(e))
            
            
    def hello(*args):
        print("Hello")
        
        
    def exit(self, *args):
        self.shellOn = False
        
        
    def pwd(self, *args):
        print(self.path)
        
        
    def ls(self, *args):
        for data in os.listdir(self.path):
            print(data, end = ' ')
        print()
        
        
    def mkdir(self, name):
        if len(name) != 1:
            print("Wrong parametrs are given")
        elif name[0] not in os.listdir(self.path):
            os.mkdir(self.path + '/' + name[0])
        else:
            print("The directory with such name already exists")
            
            
    def rmdir(self, name):
        if len(name) != 1:
            print("Wrong parametrs are given")
        elif name[0] in os.listdir(self.path):
            if len(os.listdir(self.path + '/' + name[0])) == 0:
                os.rmdir(self.path + '/' + name[0])
            else:
                print('This directory is not empty')
        else: 
            print("There is no directory named " + name[0])
            
            
    def rm(self, name):
        if len(name) != 1:
            print("Wrong parametrs are given")
        elif name[0] in os.listdir(self.path):
            os.remove(self.path + '/' + name[0])
        else: 
            print("There is no file named " + name[0])
            
            
    def touch(self, name):
        if len(name) != 1:
            print("Wrong parametrs are given")
        else:
            open(self.path + '/' + name[0], 'w')
            
            
    def cd(self, newPath):
        if len(newPath) != 1:
            print("Wrong parametrs are given")
        else:
            try:
                os.chdir(newPath[0])
                self.path = os.getcwd()
            except:
                print("Such directory does not exist")
                
                
    def cp(self, names):
        if len(names) != 2:
            print("Wrong parametrs are given")
        elif names[0] in os.listdir(self.path):
            copy2(names[0], names[1])
        else: 
            print("There is no file named " + names[0])
            
            
    def mv(self, names):
        if len(names) != 2:
            print("Wrong parametrs are given")
        elif names[0] in os.listdir(self.path):
            move(names[0], names[1])
        else: 
            print("There is no file named " + names[0])
            
            
    def echo(self, message):
        print(*message)
            
                
if __name__ == '__main__':
    shell = Shell()
    shell.run()
        
