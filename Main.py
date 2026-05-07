import os
import time
import keyboard
import sys
import msvcrt
from UnOfficialAPIs.SubDomainFinder import find_subdomains
from UnOfficialAPIs.AdminPageFinder import GetAdminPage

Logo = """                                                                                        
                                  ▒▒                  ▒▒                                
                                ▒▒██▒▒              ▒▒██▒▒                              
                                ▒▒██▒▒              ▒▒██▒▒                              
                            ▒▒  ▒▒██▒▒              ▒▒██▒▒  ▒▒                          
                          ▒▒██▒▒▒▒██▒▒              ▒▒██▒▒▒▒██▒▒                        
                          ▒▒██▒▒▒▒▒▒██▒▒  ▒▒  ▒▒  ▒▒██▒▒▒▒▒▒██▒▒                        
                            ▒▒██▒▒▒▒██▒▒▒▒██▒▒██▒▒▒▒██▒▒▒▒██▒▒                          
                            ▒▒██▒▒▒▒██▒▒▒▒██▒▒██▒▒▒▒██▒▒▒▒██▒▒                          
                            ▒▒██▒▒▒▒▒▒██▒▒██████▒▒██▒▒▒▒▒▒██▒▒                          
                              ▒▒██▒▒▒▒▒▒██████████▒▒▒▒▒▒██▒▒                            
                                ▒▒██████████████████████▒▒                              
                                  ▒▒▒▒▒▒██████████▒▒▒▒▒▒                                
                                ▒▒██████▒▒██████▒▒██████▒▒                              
                              ▒▒██▒▒▒▒▒▒██████████▒▒▒▒▒▒██▒▒                            
                            ▒▒██▒▒▒▒▒▒██████████████▒▒▒▒▒▒██▒▒                          
                            ▒▒██▒▒▒▒██▒▒██████████▒▒██▒▒▒▒██▒▒                          
                          ▒▒██▒▒▒▒██▒▒████▒▒▒▒▒▒████▒▒██▒▒▒▒██▒▒                        
                          ▒▒██▒▒▒▒██▒▒██████▒▒██████▒▒██▒▒▒▒██▒▒                        
                          ▒▒██▒▒▒▒██▒▒██████▒▒██████▒▒██▒▒▒▒██▒▒                        
                            ▒▒▒▒▒▒██▒▒████▒▒▒▒▒▒████▒▒██▒▒▒▒▒▒                          
                              ▒▒██▒▒  ▒▒██████████▒▒  ▒▒██▒▒                            
                              ▒▒██▒▒    ▒▒██████▒▒    ▒▒██▒▒                            
                              ▒▒██▒▒      ▒▒██▒▒      ▒▒██▒▒                            
                              ▒▒██▒▒        ▒▒        ▒▒██▒▒                            
                                ▒▒                      ▒▒         

                            The Void Crawler - Web Scraper Tool                     
"""

Menu = """                                                                                        
          ▒▒                  ▒▒                                
        ▒▒██▒▒              ▒▒██▒▒                              
        ▒▒██▒▒              ▒▒██▒▒                              
    ▒▒  ▒▒██▒▒              ▒▒██▒▒  ▒▒                          
  ▒▒██▒▒▒▒██▒▒              ▒▒██▒▒▒▒██▒▒                        
  ▒▒██▒▒▒▒▒▒██▒▒  ▒▒  ▒▒  ▒▒██▒▒▒▒▒▒██▒▒                        
    ▒▒██▒▒▒▒██▒▒▒▒██▒▒██▒▒▒▒██▒▒▒▒██▒▒                          
    ▒▒██▒▒▒▒██▒▒▒▒██▒▒██▒▒▒▒██▒▒▒▒██▒▒                          
    ▒▒██▒▒▒▒▒▒██▒▒██████▒▒██▒▒▒▒▒▒██▒▒                          
      ▒▒██▒▒▒▒▒▒██████████▒▒▒▒▒▒██▒▒             1. Find Subdomains               
        ▒▒██████████████████████▒▒               2. Find Admin Page               
          ▒▒▒▒▒▒██████████▒▒▒▒▒▒                 3. Exit                                
        ▒▒██████▒▒██████▒▒██████▒▒                              
      ▒▒██▒▒▒▒▒▒██████████▒▒▒▒▒▒██▒▒             > CHOISEOFTHEUSER              
    ▒▒██▒▒▒▒▒▒██████████████▒▒▒▒▒▒██▒▒                          
    ▒▒██▒▒▒▒██▒▒██████████▒▒██▒▒▒▒██▒▒                          
  ▒▒██▒▒▒▒██▒▒████▒▒▒▒▒▒████▒▒██▒▒▒▒██▒▒                        
  ▒▒██▒▒▒▒██▒▒██████▒▒██████▒▒██▒▒▒▒██▒▒                        
  ▒▒██▒▒▒▒██▒▒██████▒▒██████▒▒██▒▒▒▒██▒▒                        
    ▒▒▒▒▒▒██▒▒████▒▒▒▒▒▒████▒▒██▒▒▒▒▒▒                          
      ▒▒██▒▒  ▒▒██████████▒▒  ▒▒██▒▒                            
      ▒▒██▒▒    ▒▒██████▒▒    ▒▒██▒▒                            
      ▒▒██▒▒      ▒▒██▒▒      ▒▒██▒▒                            
      ▒▒██▒▒        ▒▒        ▒▒██▒▒                            
        ▒▒                      ▒▒         
                     
"""

def EditMenu():
    os.system("cls")
    print(Menu.replace("> CHOISEOFTHEUSER", "> " + Choise))

Choise = ""
last_key = None

def press_once(key):
    global last_key
    if keyboard.is_pressed(key):
        if last_key != key:
            last_key = key
            return True
    else:
        if last_key == key:
            last_key = None
    return False

def flush_input():
    while msvcrt.kbhit():
        msvcrt.getch()

def safe_input(prompt):
    flush_input()
    return input(prompt)

if __name__ == "__main__":
    OnMenu = True

    print(Logo)
    time.sleep(2)
    os.system("cls")

    print(Menu.replace("> CHOISEOFTHEUSER", "> "))

    while OnMenu:

        for key in "1234567890":
            if press_once(key):
                Choise += key
                EditMenu()

        if press_once("backspace"):
            Choise = Choise[:-1]
            EditMenu()

        if press_once("enter"):
            OnMenu = False

            keyboard.unhook_all()
            time.sleep(0.2)
            os.system("cls")

        time.sleep(0.01)

    if Choise == "1":
        domain = safe_input("Enter the domain to find subdomains: ")
        print(find_subdomains(domain))
        safe_input("\nPress Enter...")

    elif Choise == "2":
        domain = safe_input("Enter the domain to find admin pages: ")
        print(GetAdminPage(domain))
        safe_input("\nPress Enter...")

    elif Choise == "3":
        print("Exiting...")
        time.sleep(1)
        exit()

    else:
        print("Invalid choice!")
        time.sleep(1)