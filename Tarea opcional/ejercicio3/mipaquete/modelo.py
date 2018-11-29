# se crea la clase garante a esta clase se la puede considerar como una clase general 
class Garante(object):	
	# se crea los atributos especificos de la clase						
	def __init__(self, n, a, s):			
		self.nombre = n 					
		self.apellido = a
		self.sueldo = s
	# se crea los metodos para agregar los datos nombrte apellido y sueldo 	
	def setNombre(self, n):					
		self.nombre = n

	def setApellido(self, a):
		self.apellido = a

	def setSueldo(self, s):
		self.sueldo = s
	# se crea los metodos para obtener los datos nombre apellido y sueldo 
	def getNombre(self):				
		return self.nombre

	def getApellido(self):
		return self.apellido

	def getSueldo(self):
		return self.sueldo
	# se crea el metodo presentar datos este sera el encargado de enviar la informacion que se requiere a las demas clases 
	def presentarDatos(self):					
		cadena="Garante:\nNombre: %s %s\nSueldo: %s"%(self.getNombre(),self.getApellido(),self.getSueldo())
		return cadena

# se crea el metodo preseta este funcionara como una super clase 
class Prestamo(object):						
	# se crea los atributo especificos de la clase
	def __init__(self, b, s, p, i, t, g):			
		self.nombreBeneficiario = b 			
		self.sueldo = s
		self.montoPrestamo = p
		self.interes = i
		self.tiempo = t
		self.garante1= g
	# se crea los metodos para agregar el nombre sueldo monto interes el tiempo y garante
	def setNombreBeneficiario(self, b):			
		self.nombreBeneficiario = b
		
	def setSueldo(self, s):
		self.sueldo = s

	def setmontoPrestamo(self, p):
		self.montoPrestamo = p

	def setInteres(self,i):
		self.interes = i

	def setTiempo(self,t):
		self.tiempo = t

	def setGarante1(self,g):
		self.garante1 = g

	def getNombreBeneficiario(self):		
		return self.nombreBeneficiario
	# se crea los metodos para obtener o devolver la informacion nombre sueldo monto interes el tiempo y garante
	def getSueldo(self):
		return	self.sueldo

	def getMontoPrestamos(self):
		return self.montoPrestamo

	def getInteres(self):
		return self.interes

	def getTiempo(self):
		return self.tiempo

	def getGarante1(self):
		return self.garante1.presentarDatos()
	# se crea un nuevo metodo presentar datos 
	def presentarDatos(self):												
		cadena = "\nPRESTAMO:\nNombre del Beneficiario: %s\nSueldo: %d\nMonto Prestamos: %s\nInteres: %s\nTiempo: %d\n%s"%(self.getNombreBeneficiario(),self.getSueldo(),self.getMontoPrestamos(),self.getInteres(),self.getTiempo(),self.getGarante1())
		return cadena
# se crea la clase prestamos automovil esta sera hija de la super clase prestamo
class PrestamosAutomovil(Prestamo):									
	# se crea los tributos especificos y se le añade los atributos de la clse hija
	def __init__(self, b, s, p, i, t, g, tv, mv, gs):						
		super(PrestamosAutomovil, self).__init__(b , s, p , i, t, g) # se hereda los atributos
		self.tipoVehiculo = tv 								
		self.marcaVehiculo = mv
		self.garante2 = gs
	# se grea los metodos para agregar el tipo marca garante
	def setTipoVehiculo(self,tv):		
		self.tipoVehiculo= tv

	def setMarcaVehiculo(self,mv):
		self.marcaVehiculo = mv

	def setGarante2(self,gs):
		self.garante2 = gs
	# se crea los metodos para devolver u obtener la informacion
	def getTipoVehiculo(self):				
		return self.tipoVehiculo

	def getMarcaVehiculo(self):
		return self.marcaVehiculo

	def getGarante2(self):
		return self.garante2.presentarDatos()
	# se crea el metodo para presentar 
	def presentarDatos(self):			
		cadena = "\nPRESTAMO AUTOMOVIL :\nNombre del Beneficiario: %s\nSueldo: %d\nMonto Prestamos: %d\nInteres: %d\nTiempo: %d\nTipo de Vehiculo: %s\nMarca Vehiculo: %s\n%s\n"%(self.getNombreBeneficiario(),self.getSueldo(),self.getMontoPrestamos(),self.getInteres(),self.getTiempo(),self.getTipoVehiculo(),self.getMarcaVehiculo(),self.getGarante2())
		return cadena