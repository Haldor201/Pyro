import Pyro4
import sys

try:
    num = int(input("Escribe un número entero: "))
except ValueError:
    print("Ingresa un número válido.")
    sys.exit()

# Usa el URI del servidor de nombres en Render
# Asegúrate de cambiar 'pyro-euq6.onrender.com' al nombre correcto de tu servicio
getFactClass = Pyro4.Proxy("PYRONAME:example.fact@pyro-euq6.onrender.com:9090")

try:
    print(getFactClass.get_facto(num))
except Pyro4.errors.CommunicationError as e:
    print("Error de comunicación:", e)
except Exception as e:
    print("Ocurrió un error:", e)
