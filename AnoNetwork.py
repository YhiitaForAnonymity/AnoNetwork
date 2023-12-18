import time 
import os
import os.path
import pathlib
import pyfiglet
import colorama
import requests

def isWebsitePublic(url: str):
    response = requests.get(url)
    return response.status_code == 200

def isFileAccessible(path: str):
    return os.path.exists(path)

def clearConsole():
    os.system("cls")

def loadingAnimation(sleep, repitions, states):
    for i in range(0, repitions):
        for state in states:
            print(state)
            time.sleep(sleep)
            clearConsole()



def checkWebsite(url: str):

    isValid = isWebsitePublic(url)
    
    if isValid:
        Site = requests.get(url).content
        loadingAnimation(sleep=0.2, repitions=1, states=[
            "Fetching website please wait ",
            "Fetching website please wait .",
            "Fetching website please wait ..",
            "Fetching website please wait ..."
        ])
    
    if not isValid:
        loadingAnimation(sleep=1, repitions=1, states=[
            "Website not found (3)",
            "Website not found (2)",
            "Website not found (1)",
        ])

    return isValid




def checkFile(path: str):

    isValid = isFileAccessible()

    if isValid:
        file = open(data, 'r')
        data = file.read()
        loadingAnimation(sleep=0.2, repitions=1, states=[
            "Reading file please wait ",
            "Reading file please wait .",
            "Reading file please wait ..",
            "Reading file please wait ..."
        ])
        print (data)

    if not isValid:
        loadingAnimation(sleep=1, repitions=1, states=[
            "File not found (3)",
            "File not found (2)",
            "File not found (1)",
        ])

    return isValid


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
    [+]Every public website supported
    [+]Example help.xyz""")
     
    
    print(Fore.GREEN + """ ==============================================================""")
    print(Style.RESET_ALL)
    def track():
        data = input()

        print("Check if file exists")
        fileExists = checkFile(data)

        print("Check if website exists")
        websiteExists = checkWebsite(data)

        if not fileExists and not websiteExists:
            loop()


        
    track()
    print(Fore.YELLOW + """
    """)
    cont = input("Do you want to keep up searching ? [yes/no]")
    if cont == "Yes" or cont == "yes":
        loop()
    else:
        exit()
loop()