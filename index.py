from cmd import Cmd
# import os.path
from os import path,system,SEEK_END

class MyCLi(Cmd):
    prompt = "ccwc? "
    intro = "Coding challenge cli. type help for more info"
    def do_hello(self,line):
        print("welcome to CLI")
    def do_quit(self, line):
        print(self,line)
        return True
    def do_read(self, line):
       if(path.isfile(f"{line}")):
        f =  open(f"{line}", "r")
        for x in f:
           print(x)
       elif(f"{line}" == ""):
          print("please provide a file")
       else:
          print("Invalid")
    def do_clear(self,line): 
       system("clear")
    def do_size(self,line):
       t = open(f"{line}", "r")
       t.seek(0, SEEK_END)
       print(t.tell(), 'bytes')
    def do_line(self,line):
       b = open(f"{line}", "r")
       count = len(b.readlines())
       print(count)
                 
        




if __name__  == "__main__":
    MyCLi().cmdloop()