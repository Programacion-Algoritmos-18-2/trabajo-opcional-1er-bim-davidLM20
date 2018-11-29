#Clase docente de esta clase se embiara los atributos que corresponde hacia el paquete Alumno
class Docente(object):
	#se crea los atributos especificos de la clase						
	def __init__(self,n,a,t):		
		self.nombre = n      
		self.apellido = a
		self.titulo = t
	#Se genera los metodos para agregar datos 	nombre apellido y titulol
	def setNombre(self,n):						
		self.nombre = n

	def setApellido(self,a):
		self.apellido = a

	def setTitulo(self,t):
		self.titulo = t
	# se genera los metodos para la obtencion de datos nombre apellido y titulo 
	def getNombre(self):							
		return self.nombre

	def getApellido(self):
		return self.apellido

	def getTitulo(self):
		return self.titulo
	# se genera el metodo presentar datos esta se enviara al siguiente paquete llevando los datos que se requiren 
	def presentarDatos(self):						
		cadena = "%s %s\n\tTitulo: %s"%(self.getNombre(),self.getApellido(),self.getTitulo())
		return cadena

		