from tools import logos, myip, checkip, scanports, shownetdevice, monitormodeon,figlet
from subprocess import run
from os import system, getcwd, chdir
import os
import sys


# تنظيف الشاشة
system("cls||clear") 
logos.code_logo()

# الحلقة الرئيسية لتنفيذ الأوامر
while True:
    # أخذ المدخل من المستخدم
    directorynow = os.getcwd()
    command = input("\033[1;31m  #\033[1;33mBatByte-tool\033[1;31m ( \033[1;32m" + directorynow +  " \033[1;31m) : \033[1;32m  ")

    # الخروج من الحلقة
    if command.lower() == "exit":
        break


    if command.lower().startswith("cd "): 
        new_directory = command[3:].strip()  
        try:
            chdir(new_directory) 
        except FileNotFoundError:
            print("")
            print(f"{new_directory}' Not found.")
        except PermissionError:
            print(f"Operation not permitted'{new_directory}'.")


    if command.lower() == "whattools":
        print("""
    
    \033[1;31m|---Network Tools:
    \033[1;32m1. \033[1;33mscanport\033[1;32m      To scan websites ports
    2. \033[1;33mshndevice\033[1;32m     To display devices connected to the network
    3. \033[1;33mnetmonitor\033[1;32m    To change network interface mode

    \033[1;31m|---IP Address Tools  
    \033[1;32m1. \033[1;33mmyip  \033[1;32m        To display your device's IP address
    2. \033[1;33mcheckip   \033[1;32m    To view details about an IP address

    
    \033[1;31m|---Edit Text Tools:
    \033[1;32m1.\033[1;33m texter   \033[1;32m     Change the text format to ASCII Art
              
        """)



    if command.lower() == "myip":
        logos.myip_logo()
        myip.myip()
    elif command.lower() == "checkip":
        logos.checkip_logo()
        checkip.check_another_ip()
    elif command.lower() == "scanport":
        logos.scanport_logo()
        scanports.scanport()
    elif command.lower() == "shndevice":
        logos.shndevice()
        shownetdevice.show()
    elif command.lower() == "netmonitor":
        logos.netmonitor()
        monitormodeon.monitor()
    elif command.lower() == "texter":
        logos.figlet()
        figlet.figlet()
    else:
        try:
            run(command, shell=True, check=True)
        except Exception as e:
            print()
