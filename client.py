# saved as client.py
import Pyro4
import sys

try:
    num = int(input("Escribe un número entero: "))
except ValueError:
    print("Ingresa un número válido.")
    sys.exit()

# Configurar el nombre del servidor
Pyro4.config.NS_HOST = "pyro-euq6.onrender.com"  # Cambia esto por la URL de tu naming server
Pyro4.config.NS_PORT = 9090  # Asegúrate de que este puerto sea el correcto

try:
    getFactClass = Pyro4.Proxy("PYRONAME:example.fact")  # Buscar el objeto remoto
    print(getFactClass.get_facto(num))
except Pyro4.errors.CommunicationError as e:
    print(f"Error de comunicación: {e}")
except Pyro4.errors.NamingError as e:
    print(f"Error de nombres: {e}")
except Exception as e:
    print(f"Se produjo un error: {e}")

