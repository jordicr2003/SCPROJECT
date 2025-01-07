#!/bin/bash

echo "Iniciando iperf3 en modo cliente..."
iperf3 -c 192.168.2.1 -t 10  # IP del AP
echo "Pruebas completadas."
