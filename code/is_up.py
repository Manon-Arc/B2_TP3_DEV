from os import system
from sys import argv
if system("ping " + argv[1]) == 0:
    print("UP !")
else:
    print("DOWN !")