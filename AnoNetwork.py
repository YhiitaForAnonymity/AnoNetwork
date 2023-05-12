import time 
import os
import os.path
import pathlib
import pyfiglet
import colorama
from colorama import *

def loop():
    text = pyfiglet.figlet_format(text="AnoNetwork",
    font="slant")
    os.system("cls") 
    print(Fore.BLUE + """  
    """)
    print(text)


    print(Fore.YELLOW + """
    [+]AnoNetwork V1
    [+]Creator:XYZ Universe
    [+]Secure Internet Connection
    [+]All links ending with .xyz
    [+]Example help.xyz""")
     
    
    print(Fore.GREEN + """ ==============================================================""")
    print(Style.RESET_ALL)
    def track():
        data = input()
        if os.path.exists(data):
            Site = open(data, 'r')
            os.system("cls")
    
            time.sleep(0.2)
            print ("Reading file please wait...")
            time.sleep(0.3)
            os.system("cls")
    
            data = Site.read()
            print (data)
        else:
            os.system("cls")      
            print("Error: File not found  (3)")
            time.sleep(1)
            os.system("cls")
            print("Error: File not found  (2)")
            time.sleep(1)
            os.system("cls")
            print("Error: File not found  (1)")
            time.sleep(1)
            os.system("cls")
            loop()
    track()
    print(Fore.YELLOW + """
    """)
    cont = input("Do you want to keep up searching ? [yes/no]")
   if cont.lower() in {'yes', 'y'}:
    loop()
else:
    exit()
loop()
