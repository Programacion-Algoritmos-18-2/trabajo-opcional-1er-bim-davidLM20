# se importa la informacion de mipaquete
from mipaquete.modelo import *					

garante = Garante("Luiz","fonzi",540)		# se crea un objeto garante se le añade la informacion 			
primero = Prestamo("Paul Suarez",546,15000,12, 6,garante) # se crea el objeto Prestamo y se le añade la informacion de garante
segundo = PrestamosAutomovil("Carlos Viteri",8006,13000,12,7,garante,"Auto","corvet",Garante("Angel","Lopez",2344))	# Se crea el objeto PrestamoAutomovil 

print(primero.presentarDatos())		# se presenta la informacion del objeto primero 	

print(segundo.presentarDatos())		# se presenta la informacion del objeto segundo