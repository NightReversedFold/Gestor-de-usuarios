from packages import tabulate

tabulate = tabulate.tabulate

class Usuario:
    def __init__(self,nombre,telefono,correo,direccion):
        self._nombre = nombre 
        self._telefono = telefono
        self._correo = correo
        self._direccion = direccion
    
    def Coincide(self,info):
        return self.nombre == info or self.telefono == info or self.correo == info
    
    def __str__(self):
        lista = [['Nombre','Telefono','Correo','Direccion']]
        lista.append([self.nombre,self.telefono,self.correo,self.direccion])
        
        return tabulate(lista, headers="firstrow", tablefmt="grid")
    
    @property
    def nombre(self):
        return self._nombre
    @property
    def telefono(self):
        return self._telefono
    @property
    def correo(self):
        return self._correo
    @property
    def direccion(self):
        return self._direccion
    
    @nombre.setter
    def nombre(self,nuevoNombre):
        self._nombre = nuevoNombre
    @telefono.setter
    def telefono(self,nuevoTelefono):
        self._telefono = nuevoTelefono
    @correo.setter
    def correo(self,nuevoCorreo):
        self._correo = nuevoCorreo
    @direccion.setter
    def direccion(self,nuevaDireccion):
        self._direccion = nuevaDireccion