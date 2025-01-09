import iperf3

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
                print(f"Conexión desde: {result.remote_host}")
                print(f"Throughput: {result.sent_Mbps:.2f} Mbps (enviado)")
                print(f"Throughput: {result.received_Mbps:.2f} Mbps (recibido)")
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    run_iperf3_server()
