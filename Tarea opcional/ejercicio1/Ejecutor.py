# se imprta la informacion de mi paquete
from mipaquete.modelo import *

f = Futbolista("Antonio","Valencia") # se crea un objeto de tipo futbolista 
e = Equipo("Manchester United","Inglaterra")# se cre un objeto de tupo equipo
f.setEquipo(e)# se agrega el equipo a el primer obejto futbolista
f.setDorsal(25)# se agrega el equipo al objeto futbolista
f.setPosicion("LATERAL") # se agrega la posioin al objeto futbolista
print(f.presentarDatos()) # se presenta toda la informacion del primer futbolista
e2 = Equipo("nexaca","Mexico")# se crea un nuevo objeto tipo equipo para el futbolista 2
f2 = Futbolista("Alex", "Aguinaga",e2, "MEDIOCENTRO")# se crea un nuevo objeto futbolista 
f2.setDorsal(7)# se agregar el dorsal del futbolista 2
print(f2.presentarDatos()) # se presenta la informacion del segundo futbolista
e3 = Equipo("lazio","Italia")# se crea un nuevo objeto tipo equipo 
f3 = Futbolista("Felipe", "Caicedo",e3)# se crea un objeto tipo futbolista
f3.setDorsal(32)# se agrega el dorsal al futbolista 3
f3.setPosicion("DELANTERO") # se le agrega una posocion al futbolista 3 
print(f3.presentarDatos())# se presenta los datos del furtbolita 3