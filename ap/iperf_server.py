import iperf3
import matplotlib.pyplot as plt
import os

def run_iperf3_server():
    """
    Configura y ejecuta un servidor iperf3 en modo bloqueante.
    """
    server = iperf3.Server()

    server.bind_address = '192.168.1.72'  
    server.port = 5201                   

    print(f"Servidor iperf3 iniciado en {server.bind_address}:{server.port}. Esperando conexiones...")

    try:
        while True:
            result = server.run() 

            if result.error:
                print(f"Error en el servidor: {result.error}")
            else:
                
                client_ip=result.remote_host
                intervals = result.intervals
                times = [interval['sum']['start'] for interval in intervals]
                client_folder = f"reports/{client_ip}"
                os.makedirs(client_folder, exist_ok=True)
                
                throughputs = [interval['sum']['bits_per_second'] / 1e6 for interval in intervals] #MBPS
                packet_loss = [interval['sum']['lost_percent'] for interval in intervals]  # %
                delays = [interval['sum']['jitter_ms'] for interval in intervals]  # ms (en UDP)

                #Graphic 1
                plt.figure(figsize=(10, 5))
                plt.plot(times, throughputs, marker='o', label='Throughput (Mbps)')
                plt.xlabel('Time (s)')
                plt.ylabel('Throughput (Mbps)')
                plt.title(f"Throughput of {client_ip}")
                plt.legend()
                plt.grid(True)
                plt.savefig(f"{client_folder}/throughput.png") 
                plt.close()


                #Graphic 2
                plt.figure(figsize=(10, 5))
                plt.plot(times, packet_loss, marker='o', label='Packet loss (%)')
                plt.xlabel('Time (s)')
                plt.ylabel('Packet loss (%)')
                plt.title(f"Packet loss of {client_ip}")
                plt.legend()
                plt.grid(True)
                plt.savefig(f"{client_folder}/packet_loss.png") 
                plt.close()


                #Graphic 3
                plt.figure(figsize=(10, 5))
                plt.plot(times, delays, marker='o', label='Jitter (ms)')
                plt.xlabel('Time (s)')
                plt.ylabel('Jitter (ms)')
                plt.title(f"Delay of {client_ip}")
                plt.legend()
                plt.grid(True)
                plt.savefig(f"{client_folder}/delay.png") 
                plt.close()

    except KeyboardInterrupt:
        print("\nServer stopped.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    run_iperf3_server()
