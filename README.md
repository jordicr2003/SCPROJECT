# SCPROJECT

github: https://github.com/jordicr2003/SCPROJECT/tree/version1

Prerequisites
The device acting as the access point (AP) must have the following network interfaces:
eth1 (Ethernet interface)
wl1 (Wireless interface)
Ensure Python 3 is installed on the AP device.
Install any required dependencies.

Instructions
1. Setting Up the Access Point (AP)
Run the following command on the device you want to configure as the AP:
	ython3 main.py
This starts the application in the terminal and waits for client connections.

2. Measuring Network Performance
To analyze delay, packet loss, and throughput on the AP device:
Run the iperf_server.py script:
	python iperf_server.py
The script will wait for a client to connect.

3. Client Setup
On the client device:
Connect to the AP by executing:
	./connect_to_ap.sh
This script establishes a direct connection to the AP.
Measure network performance statistics by running:
	./run_iperf_client.sh
This generates two output files containing statistics related to delay, packet loss, and throughput.

4. Viewing Results
Once the client connects and performance data is recorded, the AP device will generate graphics visualizing:
-Delay
-Packet loss
-Throughput
These graphics will help analyze the quality of the connection.