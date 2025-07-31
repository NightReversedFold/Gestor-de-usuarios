from packages import tabulate

tabulate = tabulate.tabulate

class Usuario:
    def __init__(self,nombre,telefono,correo,direccion):
        self.nombre = nombre 
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
    
    def Coincide(self,info):
        return self.nombre.lower() == info.lower() or self.telefono == info or self.correo.lower() == info.lower()
    
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
        nuevoNombre = str(nuevoNombre).strip()
        
        self._nombre = 'Campo vacio.' if nuevoNombre == '' else nuevoNombre
    @telefono.setter
    def telefono(self,nuevoTelefono):
        nuevoTelefono = str(nuevoTelefono).strip()
        
        self._telefono = 'Campo vacio.' if nuevoTelefono == '' else nuevoTelefono
    @correo.setter
    def correo(self,nuevoCorreo):
        nuevoCorreo = str(nuevoCorreo).strip()
        
        self._correo = 'Campo vacio.' if nuevoCorreo == '' else nuevoCorreo
    @direccion.setter
    def direccion(self,nuevaDireccion):
        nuevaDireccion = str(nuevaDireccion).strip()
        
        self._direccion = 'Campo vacio.' if nuevaDireccion == '' else nuevaDireccion