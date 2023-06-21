import http.server
import socketserver

# Define el puerto en el que deseas ejecutar el servidor
puerto = 8000

# Crea un manejador de solicitudes que sirva los archivos estáticos
manejador = http.server.SimpleHTTPRequestHandler

# Inicia el servidor web local
with socketserver.TCPServer(("", puerto), manejador) as httpd:
    print(f"Servidor web en ejecución en el puerto {puerto}")
    print("Presiona Ctrl+C para detener el servidor")
    httpd.serve_forever()
