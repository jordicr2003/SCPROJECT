#!/bin/bash

#Delete all possible auto network config
sudo airmon-ng check kill
sudo rfkill unblock all
#set ip to wireless interface
sudo dhclient enp4s0 
sudo ip link set wlp3s0 up
sudo ip addr add 192.168.2.1/24 dev wlp3s0

#Routing configuration
sudo nft add table nat
sudo nft -- add chain nat prerouting { type nat hook prerouting priority -100 \; }
sudo nft add chain nat postrouting { type nat hook postrouting priority 100 \; }
sudo nft add rule nat postrouting oifname "enp4s0" masquerade

sudo iptables -P FORWARD ACCEPT
sudo iptables -t nat -A POSTROUTING -s 192.168.2.0/24 -o enp4s0 -j MASQUERADE

sudo lsof -t -i :53 | sudo xargs kill -9
#dnsmasq conf file

sudo dnsmasq -C dnsmasq.conf

#hostapd conf file
sudo hostapd hostapd.conf



