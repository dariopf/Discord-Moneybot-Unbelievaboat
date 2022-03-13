# Librerías
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time
import pandas as pd
import colorama
from colorama import Fore, Back, Style
colorama.init()
import os, sys

#Variables MODIFICAR
user = 'YOUR EMAIL'
passwd = 'YOUR PASSWORD'
canal = 'https://discord.com/login'
hour =int(4)

#Variables
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


#MODIFY PATH
driver = webdriver.Chrome(executable_path=os.path.join(os.path.dirname(__file__), "chromedriver.exe"), options=options)
#MODIFY PATH


stop = 0
#Funciones
def titulo ():
    print(Fore.GREEN +r'''
$$$$$$$\  $$\                                               $$\       $$\      $$\                                         $$$$$$$\             $$\     
$$  __$$\ \__|                                              $$ |      $$$\    $$$ |                                        $$  __$$\            $$ |    
$$ |  $$ |$$\  $$$$$$$\  $$$$$$$\  $$$$$$\   $$$$$$\   $$$$$$$ |      $$$$\  $$$$ | $$$$$$\  $$$$$$$\   $$$$$$\  $$\   $$\ $$ |  $$ | $$$$$$\ $$$$$$\   
$$ |  $$ |$$ |$$  _____|$$  _____|$$  __$$\ $$  __$$\ $$  __$$ |      $$\$$\$$ $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$ |  $$ |$$$$$$$\ |$$  __$$\\_$$  _|  
$$ |  $$ |$$ |\$$$$$$\  $$ /      $$ /  $$ |$$ |  \__|$$ /  $$ |      $$ \$$$  $$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |$$ |  $$ |$$  __$$\ $$ /  $$ | $$ |    
$$ |  $$ |$$ | \____$$\ $$ |      $$ |  $$ |$$ |      $$ |  $$ |      $$ |\$  /$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |  $$ |$$ |  $$ |$$ |  $$ | $$ |$$\ 
$$$$$$$  |$$ |$$$$$$$  |\$$$$$$$\ \$$$$$$  |$$ |      \$$$$$$$ |      $$ | \_/ $$ |\$$$$$$  |$$ |  $$ |\$$$$$$$\ \$$$$$$$ |$$$$$$$  |\$$$$$$  | \$$$$  |
\_______/ \__|\_______/  \_______| \______/ \__|       \_______|      \__|     \__| \______/ \__|  \__| \_______| \____$$ |\_______/  \______/   \____/ 
                                                                                                                 $$\   $$ |                             
                                                                                                                 \$$$$$$  |                             
                                                                                                                  \______/                             
''')
def start():
    print(Fore.CYAN + '''Select an option:
    1.Start
    ''')
    result1 = int(input('>>'))
    #Inicio de sesión
    driver.get(canal)
    time.sleep(1)
    return(result1)

def menu1 ():
    print(Fore.CYAN + '''Select an option:
    1.Auto                     2.Manual
    ''')
    result2 = int(input('>>'))
    return(result2)

def menu_auto():
    print(Fore.CYAN + '''Select an option:
    1.Only work                2.All things
    ''')
    result3 = int(input('>>'))
    return(result3)

def menu_manual():
    print(Fore.CYAN + '''Select an option:
    1.Work               2.Crime
    3.Slut               4.Deposit all
    ''')
    result4 = int(input('>>'))
    return(result4)
#Función work auto
def work():
    msg_input = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div/div/div/div/div/div[3]/div[2]/div')
    msg_input.send_keys('$work')
    msg_input.send_keys(Keys.ENTER)
    print('Work')

def deposit():
    msg_input = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div/div/div/div/div/div[3]/div[2]/div')
    msg_input.send_keys('$deposit all')
    msg_input.send_keys(Keys.ENTER)
    print('Deposit')

def slut():
    msg_input = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div/div/div/div/div/div[3]/div[2]/div')
    msg_input.send_keys('$slut')
    msg_input.send_keys(Keys.ENTER)
    print('Slut')

def crime():
    msg_input = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div/div/div/div/div/div[3]/div[2]/div')
    msg_input.send_keys('$crime')
    msg_input.send_keys(Keys.ENTER)
    print('Crime')
#Programa
titulo()
result1 = start()
if result1 == 1:
    result2 = menu1 ()
    if result2 == 1:
        result3 = menu_auto()
        if result3 == 1:
            while 1==1:
                work()
                time.sleep(1)
                deposit()
                time.sleep(hour*3600)
        if result3 == 2:     
            while 1==1:
                work()
                slut()
                crime()
                deposit()
                time.sleep(hour*3600)
        else:
            print(Fore.RED +'ERROR')
        
            
    elif result2 == 2:
        while stop == 0:
                result4 = menu_manual()
                if result4 == 1:
                    work()
                elif result4 == 2:
                    crime()
                elif result4 == 3:
                    slut()
                elif result4 == 4:
                    deposit()
                else:
                    print(Fore.RED +'ERROR')
                print(Fore.YELLOW +'Stop the programme?')
                print(Fore.CYAN+ '1.No 2.Yes')
                stopv= int(input(Fore.CYAN +'>>'))
                if stopv == 1:
                    stop=0
                elif stopv ==2:
                    stop=1
                else:
                    print(Fore.RED +'ERROR')
    else:
        print(Fore.RED +'ERROR')
else:
    print(Fore.RED +'ERROR')

    