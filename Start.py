import os
import requests
import socket
import sys
import time

# ANSI escape sequences for colors
class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    HEADER = "\033[95m"

def clear_terminal():
    os.system('clear')

def print_header():
    clear_terminal()
    print(Colors.RED + """
    
 $$$$$$\  $$\   $$\ $$$$$$\                     $$$$$$$$\  $$$$$$\   $$$$$$\  $$\       $$$$$$\  
$$  __$$\ $$$\  $$ |\_$$  _|                    \__$$  __|$$  __$$\ $$  __$$\ $$ |     $$  __$$\ 
$$ /  \__|$$$$\ $$ |  $$ |                         $$ |   $$ /  $$ |$$ /  $$ |$$ |     $$ /  \__|
\$$$$$$\  $$ $$\$$ |  $$ |        $$$$$$\          $$ |   $$ |  $$ |$$ |  $$ |$$ |     \$$$$$$\  
 \____$$\ $$ \$$$$ |  $$ |        \______|         $$ |   $$ |  $$ |$$ |  $$ |$$ |      \____$$\ 
$$\   $$ |$$ |\$$$ |  $$ |                         $$ |   $$ |  $$ |$$ |  $$ |$$ |     $$\   $$ |
\$$$$$$  |$$ | \$$ |$$$$$$\                        $$ |    $$$$$$  | $$$$$$  |$$$$$$$$\\$$$$$$  |
 \______/ \__|  \__|\______|                       \__|    \______/  \______/ \________|\______/ 
                                                                                                 
    """ + Colors.RESET)
    print(Colors.YELLOW + "Telegram: https://t.me/MrDiiablo")
    print("Devloper: 𝕯𝖎𝖆𝖇𝖑𝖔 11:11" + Colors.RESET)
    print("-" * 50)

def auto_detect_ip():
    try:
        response = requests.get("https://ipinfo.io/json").json()
        ip = response.get("ip")
        location = response.get("city") + ", " + response.get("region") + ", " + response.get("country")
        print(Colors.CYAN + f"Detected IP: {ip}")
        print(f"Location: {location}" + Colors.RESET)
        return ip, location
    except Exception as e:
        print(Colors.RED + f"Error detecting IP: {e}" + Colors.RESET)
        return None, None

def manual_input():
    ip = input("Enter IP address: ")
    location = input("Enter location (City, Region, Country): ")
    return ip, location

def find_sni(ip):
    try:
        host = socket.gethostbyaddr(ip)
        print(Colors.GREEN + f"SNI found for {ip}: {host[0]}" + Colors.RESET)
    except Exception as e:
        print(Colors.RED + f"Error finding SNI: {e}" + Colors.RESET)

def check_sni(ip):
    try:
        response = requests.get(f"https://{ip}", timeout=5)
        if response.status_code == 200:
            print(Colors.GREEN + f"SNI {ip} is reachable." + Colors.RESET)
        else:
            print(Colors.RED + f"SNI {ip} is not reachable." + Colors.RESET)
    except Exception as e:
        print(Colors.RED + f"Error checking SNI: {e}" + Colors.RESET)

def main():
    print_header()
    
    choice = input("1. Auto-detect IP\n2. Manual input\nChoose an option: ")
    
    if choice == '1':
        ip, location = auto_detect_ip()
    else:
        ip, location = manual_input()
    
    if ip:
        print(f"\nSelected IP: {ip}")
        find_sni(ip)
        check_sni(ip)
    else:
        print(Colors.RED + "No IP provided." + Colors.RESET)

if __name__ == "__main__":
    # Full-screen mode (only the tool interface should be visible)
    os.system('clear')  # Clear screen before starting
    main()
