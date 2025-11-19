import subprocess
import os

def tools():
    # Logo Tool
    index="""
    \033[35m --------------------------------------------------------- \033[33m

     \033[31m____             _  __  __          \033[33m_     _           
    \033[31m|  _ \ ___   ___ | |_\ \/ /\033[33m___ _ __ (_) __| | ___ _ __\033[0m 
    \033[31m| |_) / _ \ / _ \| __|\  /\033[33m/ __| '_ \| |/ _` |/ _ \ '__|\033[0m
    \033[31m|  _ < (_) | (_) | |_ /  \\\033[33m\__ \ |_) | | (_| |  __/ |   \033[0m
    \033[31m|_| \_\___/ \___/ \__/_/\_\\\033[33m___/ .__/|_|\__,_|\___|_|   \033[0m
                                  \033[33m|_|\033[0m         
              \033[45m # Hackers RootX  \033[0m         

        \033[34m[1]\033[0m Parameter XSS (\033[32mParamspider Tool\033[0m)    \033[34m[2]\033[0m Kxss

        \033[34m[3]\033[0m Payload XSS                         \033[34m[88]\033[0m Update & Upgrade  
        
        \033[34m[99]\033[0m Quit (exit)                
    """

    home="""
    \033[31m____             _  __  __          \033[33m_     _           
    \033[31m|  _ \ ___   ___ | |_\ \/ /\033[33m___ _ __ (_) __| | ___ _ __ 
    \033[31m| |_) / _ \ / _ \| __|\  /\033[33m/ __| '_ \| |/ _` |/ _ \ '__|
    \033[31m|  _ < (_) | (_) | |_ /  \\\033[33m\__ \ |_) | | (_| |  __/ |   
    \033[31m|_| \_\___/ \___/ \__/_/\_\\\033[33m___/ .__/|_|\__,_|\___|_|   
                                \033[33m|_|\033[0m     
                \033[45m # Hackers RootX  \033[0m         
        
    """

    # Def
    def xss_99():

        quit()

    def enter():
        input("Enter: ")
        tools()

    def error():
        tools()

    # [1] parameter (paramspider)
    def xss_1():

        print(home)
        print("\033[34m[99]\033[0m Quit (exit) ")
        domin = input("Domin: ")
        if domin == "99":
            xss_99()

        subprocess.call(f"paramspider -d {domin}", shell=True)
        print("-"*18)
        print("- Done")
        print("-"*18)
        enter()

    # [2] kxss
    def xss_2():

        subprocess.call(f"ls results/", shell=True)
        file = input("File Name: ")
        cat = subprocess.call(f"cat results/{file} | kxss", shell=True)
        print("-"*18)
        print("- Done")
        print("-"*18)
        enter()



    # [3] payload xss
    def xss_3():

        print("Payload: URL= \033[34m https://gist.github.com/thomashartm/841594a062aea88177b5892a2458ca7a \033[0m")
        print("Payload: URL= \033[34m https://github.com/payloadbox/xss-payload-list \033[0m")

    # [4] update & upgrade
    def xss_88():

        os.system("sudo apt update -y")
        os.system("sudo apt-get update -y")
        os.system("sudo apt upgrade -y")
        os.system("sudo apt-get upgrade -y")
        print("-"*18)
        print("- Done")
        print("-"*18)
        enter()

    # Tool
    print(index)
    number = input("Number: ")

    # IF Tools (Number)
        # [1] parameter (paramspider)
    if number == "1":
        xss_1()
        # [2] kxss
    if number == "2":
        xss_2()
        # [3] payload xss
    if number == "3":
        xss_3()
        # [4] update & upgrade
    if number == "4":
        xss_88()
    if number == "99":
        xss_99()
    else:
        error()

tools()