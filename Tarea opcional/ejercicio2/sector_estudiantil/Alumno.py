#Se importa la informacion del paquete Docente 
from personal_academico.Docente import *				
# Se crea la clase alumno con los atributos especificos de la clase 
class Alumno(object):									
	# se genera los atributos en este caso nombre es la unica nueva ya que las otras dos obtendran valores del paquete ue se importo 
	def __init__(self, n,m,s):						
		self.nombre = n 								
		self.docente_matematica = m
		self.docente_sociales = s
	# se crea los metodos para agregar los valores 
	def setNombre(self,n):								
		self.nombre=n
	# se crea los metodos para obtener los datos en el caso de los metodos de docente matematicas y sociales se obtiene los datos del metodo presentar datos  del paquete docente 
	def getNombre(self):								
		return self.nombre

	def getDocenteMatematicas(self):
		return self.docente_matematica.presentarDatos()

	def getDocenteSociales(self):
		return self.docente_sociales.presentarDatos()
	#se genera un nuevo metodo presentar datos que devuelve la informacion total requrida 	
	def presentarDatos(self):							
		cadena="\nEstudiante: %s\n\nDOCENTES:\n\tDocente de matematicas: %s\n\tDocente de docente sociales: %s\n"%(self.getNombre(),self.getDocenteMatematicas(),self.getDocenteSociales())
		return cadena

