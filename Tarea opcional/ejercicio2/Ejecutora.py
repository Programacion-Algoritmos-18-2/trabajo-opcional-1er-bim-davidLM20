# se importa la informacion de los dos paquetes Docente y Alumno
from personal_academico.Docente import *			
from sector_estudiantil.Alumno import *		
# se pide la informacion para el primer objeto docente 
ndm = input("Nombre del Docente de Matematicas: ")# se pide el nombre			
adm = input("Apellido del Docente de Matematicas: ")#se pide el apellido
t = input("Titulo del Docente: ")#se pide el titulo 
add1 = Docente(ndm, adm,t)#se añade la informacion al objeto docente									

# se pide la informacion para el segundo objeto docente 
nds = input("Nombre del Docente Sociales: ")# se pide el nombre		
ads = input("Apellido del Docente Sociales: ")# se pide el apellido
t1 = input("Titulo del Docente: ")#se pide el titulo 
add2 = Docente(nds, ads, t1)# se añade la informacion al objeto docente

# se pide el nombre del alumno
n = input("Nombre del Alumno: ")					
a = Alumno(n, add1, add2)# se añade la informacion al objeto tipo alumno								

# se presenta la informacion
print(a.presentarDatos())						