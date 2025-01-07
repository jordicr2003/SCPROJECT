#!/bin/bash

nmcli dev wifi connect "Project"
sudo dhclient wlo1
echo "Cliente conectado al AP."
