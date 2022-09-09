import os
import time
import random
import uuid
import stdiomask
from threading import Thread

try:
    import requests
    from colorama import Fore, init
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install colorama')
    import requests
    from colorama import Fore, init

init(autoreset=True)
os.system('cls')
# os.system('clear') For Mac/Linux
r = requests.Session()

logo = f"""{Fore.LIGHTCYAN_EX}
 _____ _____ _____ _____ _____ _____ _____ 
|   __|  _  |  _  |     |     |   __| __  |
|__   |   __|     | | | | | | |   __|    -|
|_____|__|  |__|__|_|_|_|_|_|_|_____|__|__|
\n {Fore.RESET}
"""
print(
    logo
)
class InstagramSpammer:
    def __init__(self):
        pass

    def login(self, username, password):
        guid = str(uuid.uuid4())
        payload = f"username={username}&password={password}&device_id=androidJDS{random.randint(9645334, 99999999)}&guid={guid}"
        headers = {
            "User-Agent": "Instagram 85.0.0.21.100 Android (28/9; 380dpi; 1080x2147; OnePlus; HWEVA; OnePlus6T; qcom; en_US; 146536611)",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        response = r.post('https://i.instagram.com/api/v1/accounts/login/', headers=headers, data=payload)

        r.cookies = response.cookies

        if response.status_code == 200:
            print(f"\n{Fore.LIGHTCYAN_EX}[+] Successfully Logged In{Fore.RESET}")
            time.sleep(2)
        else:
            print(f"\n{Fore.LIGHTRED_EX}[-] Wrong Username/Password{Fore.RESET}")
            time.sleep(3)
            exit()

        os.system('cls')

    def spammer(self, thread_id, msg):
        count = 0

        url = "https://i.instagram.com/api/v1/direct_v2/threads/broadcast/text/"

        headers = {
            "user-agent": "Instagram 85.0.0.21.100 Android (28/9; 380dpi; 1080x2147; OnePlus; HWEVA; OnePlus6T; qcom; en_US; 146536611)",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = f"thread_ids=[{thread_id}]&text={msg}"

        os.system('cls')
        # os.system('clear') For Mac/Linux
        
        spamming_logo = f"""{Fore.LIGHTCYAN_EX}
         _____ _____ _____ _____ 
        |   __|  _  |  _  |     |
        |__   |   __|     | | | |
        |_____|__|  |__|__|_|_|_|
        \n {Fore.RESET}            
        """

        print(spamming_logo)

        while True:
            time.sleep(1)
            response = r.post(url, headers=headers, data=data)
            count += 1
            if response.status_code == 200:
                print(f"[{Fore.LIGHTRED_EX} + {Fore.RESET}] Messages Sent: {Fore.LIGHTRED_EX}{count}{Fore.RESET}",end='\r')
            else:
                print(f"[{Fore.LIGHTRED_EX} ERROR {Fore.RESET} ]{Fore.LIGHTRED_EX} YOU ARE RATE LIMITED!")
                break

spammer = InstagramSpammer()
def main():
    username = input(f"[{Fore.LIGHTRED_EX} + {Fore.RESET}] Username: ")
    password = stdiomask.getpass(prompt=f"[{Fore.LIGHTRED_EX} + {Fore.RESET}] Password: ", mask='*')

    spammer.login(username=username, password=password)
    os.system('cls')
    # os.system('clear') For Mac/Linux

    data_logo = f"""{Fore.LIGHTCYAN_EX}
     ____  _____ _____ _____ 
    |    \|  _  |_   _|  _  |
    |  |  |     | | | |     |
    |____/|__|__| |_| |__|__|
    \n {Fore.RESET}
    """

    print(data_logo)

    thread_id = input(f"[{Fore.LIGHTRED_EX} + {Fore.RESET}] Thread ID: ")
    msg = input(f"[{Fore.LIGHTRED_EX} + {Fore.RESET}] Message: ")
    
    threads = int(input(f"[{Fore.LIGHTRED_EX} + {Fore.RESET}] Threads: "))
    workers = []
    
    for _ in range(threads):
        t = Thread(target=spammer.spammer, args=[thread_id, msg])
        t.start()
        workers.append(t)

    for worker in workers:
        worker.join()
    
    spammer.spammer(thread_id=thread_id, msg=msg)

if __name__ == '__main__':
    main()
