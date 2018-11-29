# se crea la clase futbolista 
class Futbolista():
	# se crea los atributos especificos de la clase
	def __init__(self, n = "", a ="", e = None, p = "" ,d = 0):
		self.nombre = n
		self.apellido = a
		self.equipo = e
		self.posicion = p
		self.dorsal = d
	# se crea los metodos para agregar nombre apellido equipo posicion dorsal del jugador 
	def setNombre(self, n):
		self.nombre = n

	def setApellido(self, a):
		self.apellido = a

	def setEquipo(self, e):
		self.equipo = e

	def setDorsal(self, d):
		self.dorsal = d

	def setPosicion(self, p):
		self.posicion = p
	# se crea los metodos para obtener nombre apellido equipo posicion dorsal del jugador	
	def getEquipo(self):
		return self.equipo

	def getNombre (self):
		return self.nombre

	def getApellido(self):
		return self.apellido

	def getPosicion(self):
		return self.posicion

	def getDorsal(self):
		return self.dorsal
	# se crea el metodo para devolver toda la informacion
	def presentarDatos(self):
		cadena = "Jugador:\n\t%s %s \n\tPertenece al equipo %s del pais %s\n\tsu posicion es %s\n\tSu dorsal es el numero %s" % (self.getNombre(),self.getApellido(),self.equipo.getNombreEquipo(),self.equipo.getPais(),self.getPosicion(),self.getDorsal())
		return cadena
# se crea la clase equipo 
class Equipo():
	# se crea los atributos especificos de la calse
	def __init__(self, n ,s):
		self.nombre = n
		self.pais = s
	# se crea los metodos para agregar en nombre y pais del equipo
	def setNombreEquipo(self, n):
		self.nombre = n

	def setPais(self, s):
		self.pais = s
	# se crea los metodos para obtener nombre y pais del equipo
	def getNombreEquipo(self):
		return self.nombre

	def getPais(self):
		return self.pais
	# este metodo enviara la informacion y se icluira en el metodo de presentar datos de la clase futbolista
	def presentarDatos():
		cadena = "\n%s %s" % (self.getNombreEquipo(),self.getPais())
		return cadena
