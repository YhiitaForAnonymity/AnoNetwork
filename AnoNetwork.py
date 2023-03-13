import time 
import os
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
        Site = open(data, 'r')
        os.system("cls")
    
        time.sleep(0.2)
        print ("Reading file please wait...")
        time.sleep(0.3)
        os.system("cls")
    
        data = Site.read()
        print (data)
    track()
    print(Fore.YELLOW + """
    """)
    cont = input("Do you want to keep up searching ? [yes/no]")
    if cont == "Yes" or cont == "yes":
        loop()
    else:
        exit()
loop()