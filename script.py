import os
import subprocess

def print_banner():
    banner = """
    Welcome Soldier!, You can test reachable internal servers from here 
               
                                                
                      * **# ***                 
                    *************               
                  ******    ********            
                 *#** **      ******            
    *           *                 ***      *    
    **         *****                *     **    
     ***       **#     *** *       * *   **     
      **** **           ******* *    ** **      
       **  * *****    #* ******* *  * * *       
   **  *        **  *  #*  * *********     **   
    ****     ******  #*   * ** *******  ****    
      ***  ***   **         *  *** **  ***      
     *                       ****#**      *     
       ******      * **     *  ** * ***#**      
                   ***        *                 
         ****#**   ***          #******         
              ****  ***   **   **               
                *    *****  * **                
                 * ** ***  **                   
                   *#      *                    
                                                                                                                            
    """
    print(banner)

def help_menu():
    """Display the help menu."""
    help_text = """
Available Commands:
    ping <IP/hostname> - Ping a Server.
    about              - Display information about this script.
    help               - Show this help menu.
    hint               - Get a hint on how to get the flag.
    exit               - Exit the shell.
"""
    print(help_text)

def execute_ping(target):
    try:
        arguments = f"ping -c 4 {target}" 
        subprocess.run(arguments, shell=True, check=True) 
    except Exception as e:
        print(f"Error executing ping: {e}")

def exploit_hint():
    print("Try to bypass and exploit a simple command injection vulnerability and get your flag at /flag.txt")

def about_script():
    print("Made with ♡ for LegionOffsec by DesTny #SecuritySundays")

def main():
    print_banner()

    while True:
        command = input(">>> ")

        if command == "exit":
            print("Exiting the shell...")
            break

        elif command == "help":
            help_menu()

        elif command == "about":
            about_script()

        elif command == "hint":
            exploit_hint()

        elif command.startswith("ping "):
            target = command.split(" ", 1)[1]
            execute_ping(target)

        else:
            print("Unknown command. Type 'help' for a list of available commands.")

if __name__ == "__main__":
    main()