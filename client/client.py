import os

def generate_connect_to_ap_script(ssid, interface):
    """Genera el script connect_to_ap.sh para conectarse al AP."""
    script_content = f"""#!/bin/bash

nmcli dev wifi connect "{ssid}"
sudo dhclient {interface}
echo "Client connected to "{ssid}"."
"""

    with open("./connect_to_ap.sh", "w") as file:
        file.write(script_content)

    os.chmod("./connect_to_ap.sh", 0o755) 


def generate_run_iperf_client_script(ap_ip):
    """Genera el script run_iperf_client.sh para ejecutar iperf3 en modo cliente."""
    script_content = f"""#!/bin/bash

iperf3 -c {ap_ip} -t 10
echo "iperf3 done in client mode."
"""

    with open("./run_iperf_client.sh", "w") as file:
        file.write(script_content)

    os.chmod("./run_iperf_client.sh", 0o755)


def main():

    ssid = "Project"
    interface="wlo1"
    ap_ip = "192.168.2.1"

    generate_connect_to_ap_script(ssid, interface)
    generate_run_iperf_client_script(ap_ip)


if __name__ == "__main__":
    main()