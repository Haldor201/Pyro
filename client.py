# saved as greeting-client.py
import Pyro4
import sys
try:
    num = int(input("write a int number "))
except:
    print("ingresa un numero valido")
    sys.exit()

getFactClass = Pyro4.Proxy("PYRONAME:example.fact")    # use name server object lookup uri shortcut
print(getFactClass.get_facto(num))