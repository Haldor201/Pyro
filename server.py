import Pyro4
import os

@Pyro4.expose
class Facto(object):
    def get_facto(self, num):
        if num == 0 or num == 1:
            return 1
        else:
            factorial = 1
            for i in range(2, num + 1):
                factorial *= i
            return factorial

# Obtiene el puerto de la variable de entorno o usa un puerto por defecto (ej. 9090 para pruebas locales)
port = int(os.getenv("PORT", "9090"))

# Configura el daemon para escuchar en cualquier IP ('0.0.0.0') y el puerto asignado por Render
daemon = Pyro4.Daemon(host="0.0.0.0", port=port)

# Conectar al servidor de nombres
ns = Pyro4.locateNS()

# Registrar el objeto
uri = daemon.register(Facto)
ns.register("example.fact", uri)

print(f"Object registered with URI: {uri}")  # Para depuración
print(f"Ready. Listening on port {port}")
daemon.requestLoop()
