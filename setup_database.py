from app import verificar_y_crear_tablas
import os
import socket

try:
    # Intenta resolver el nombre del host para verificar la conectividad
    hostname = os.getenv('DATABASE_URL').split('@')[1].split(':')[0]
    socket.gethostbyname(hostname)
    print(f"Conectividad al host {hostname} verificada.")
except Exception as e:
    print(f"Error de conexión al host {hostname}: {e}")


if __name__ == "__main__":
    verificar_y_crear_tablas()
