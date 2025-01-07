import subprocess
import json
import os
import matplotlib.pyplot as plt

def start_iperf_server():
    """
    Inicia iperf3 en modo servidor en el AP y espera conexiones.
    """
    print("Iniciando iperf3 en modo servidor...")
    process = subprocess.Popen(
        ["iperf3", "-s", "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return process

def parse_iperf_output(output):
    """
    Procesa la salida JSON de iperf3 para extraer métricas de rendimiento.
    """
    try:
        data = json.loads(output)
        
        throughput = data["end"]["sum_received"]["bits_per_second"] / 1e6  # Convertimos a Mbps
        packet_loss = data["end"]["sum_received"].get("lost_percent", 0.0)  # Porcentaje de paquetes perdidos
        jitter = data["end"]["sum_received"].get("jitter_ms", 0.0)  # Jitter (en milisegundos)
        
        return throughput, packet_loss, jitter
    except Exception as e:
        print(f"Error al procesar la salida de iperf3: {e}")
        return None, None, None

def monitor_traffic(server_process):
    """
    Monitorea el rendimiento mientras iperf3 está en modo servidor.
    """
    print("Esperando datos de rendimiento...")

    stdout, stderr = server_process.communicate(timeout=30)  # Ajusta el tiempo de espera según tus pruebas
    stdout = stdout.decode("utf-8")

    # Procesa la salida y extrae las métricas
    throughput, packet_loss, jitter = parse_iperf_output(stdout)

    print(f"Throughput: {throughput} Mbps")
    print(f"Perdida de paquetes: {packet_loss}%")
    print(f"Jitter: {jitter} ms")

    return throughput, packet_loss, jitter

def generate_report(throughput, packet_loss, jitter):
    """
    Genera un gráfico del rendimiento y lo guarda en un archivo.
    """
    print("Generando informe de rendimiento...")

    metrics = ["Throughput (Mbps)", "Packet Loss (%)", "Jitter (ms)"]
    values = [throughput, packet_loss, jitter]

    plt.figure()
    plt.bar(metrics, values, color=["blue", "orange", "green"])
    plt.title("Rendimiento de la red")
    plt.ylabel("Valores")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    report_path = "./reports/performance_report.png"
    os.makedirs("./reports", exist_ok=True)
    plt.savefig(report_path)
    print(f"Informe generado: {report_path}")

def main():
    # Inicia el servidor iperf3
    server_process = start_iperf_server()

    try:
        throughput, packet_loss, jitter = monitor_traffic(server_process)

        generate_report(throughput, packet_loss, jitter)

    except Exception as e:
        print(f"Error durante la monitorización: {e}")

    finally:
        print("Deteniendo el servidor iperf3...")
        server_process.terminate()
        server_process.wait()

if __name__ == "__main__":
    main()
