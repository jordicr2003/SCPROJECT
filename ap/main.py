import os #write configuration files



#setup hostapd conffiile
def setup_hostapd(interface,ssid,channel):
    hostapd_config = f"""
interface={interface}
ssid={ssid}
hw_mode=g
channel={channel}
ignore_broadcast_ssid=0
"""
    with open('hostapd.conf','w') as file:
        file.write(hostapd_config)

#setup exec file to configure all the interfaces and routing mechanism
def setup_bash(i_ethernet,i_wireless):
    bash_config = f"""#!/bin/bash
sudo airmon-ng check kill
sudo rfkill unblock all
# Set IP to wireless interface
sudo dhclient {i_ethernet}
sudo ip link set {i_wireless} up
sudo ip addr add 192.168.2.1/24 dev {i_wireless}

sudo nft add table nat
sudo nft -- add chain nat prerouting {{ type nat hook prerouting priority -100 \; }}
sudo nft add chain nat postrouting {{ type nat hook postrouting priority 100 \; }}
sudo nft add rule nat postrouting oifname "{i_ethernet}" masquerade

sudo iptables -P FORWARD ACCEPT
sudo iptables -t nat -A POSTROUTING -s 192.168.2.0/24 -o {i_ethernet} -j MASQUERADE

sudo lsof -t -i :53 | sudo xargs kill -9

sudo dnsmasq -C dnsmasq.conf
sudo hostapd hostapd.conf
"""
    with open("./run.sh",'w') as file:
        file.write(bash_config)
    os.chmod("./run.sh",0o755) #add permisions

    

setup_hostapd("wlp3s0","test",6)
setup_bash("enp4s0","wlp3s0")