import socket
import time
import os
from datetime import datetime

def send_log(host, port, message):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(message.encode(), (host, port))
        print(f"Sent: {message}")
    except Exception as e:
        print(f"Error sending log: {e}")
    finally:
        sock.close()

def read_and_send_logs(log_file, host, port, delay=1):
    print(f"Starting to read logs from {log_file} and sending to {host}:{port}")

    with open(log_file, 'r') as f:
        for line in f:
            send_log(host, port, line.strip())
            time.sleep(delay)

    print("All logs have been sent")

if __name__ == "__main__":
    time.sleep(10)

    log_file = "sample_logs.txt"
    syslog_host = "rsyslog"
    syslog_port = 5514

    read_and_send_logs(log_file, syslog_host, syslog_port)
