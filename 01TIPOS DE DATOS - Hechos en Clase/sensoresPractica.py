from Clases.Sensores import *

import os
os.system('cls' if os.name == 'nt' else 'clear')

x = Sensores(False, True, True, True)
x.verificacion()

