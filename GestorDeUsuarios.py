import json

from packages import tabulate

tabulate = tabulate.tabulate

from Usuario import Usuario

class GestorDeUsuarios:
    def __init__(self):
        self._Usuarios = []
        self.__inicializarBaseDeDatos()
    
    def __inicializarBaseDeDatos(self):
        try:
            with open('BDUsuarios.json','r') as ar:
                datos = json.load(ar)
                self.__cargarUsuarios(datos)
        except PermissionError:
            print("No tienes permiso para escribir en esta ubicación.")
        except IsADirectoryError:
            print("Se intentó abrir una carpeta como archivo.")
        except OSError as e:
            print(f"Error de sistema: {e}")
                        
    def __cargarUsuarios(self,listaDeUsuarios):
        print(listaDeUsuarios)
        for usuario in listaDeUsuarios:
            self.Usuarios = (usuario['nombre'],usuario['telefono'],usuario['correo'],usuario['direccion'])
    
    def guardarUsuarios(self):
        usuariosOrdenadosParaJSON = []
        
        for usuario in self.Usuarios:
            usuariosOrdenadosParaJSON.append({
                "nombre": usuario.nombre,
                "telefono": usuario.telefono,
                "correo": usuario.correo,
                "direccion": usuario.direccion,  
            })
        
        try:
          with open('BDUsuarios.json','w') as ar:
            json.dump(usuariosOrdenadosParaJSON,ar,indent = 4)
        except FileNotFoundError:
            print("La ruta no existe o una carpeta intermedia falta.")
        except PermissionError:
            print("No tienes permiso para escribir en esta ubicación.")
        except IsADirectoryError:
            print("Se intento abrir una carpeta como archivo.")
        except OSError as e:
            print(f"Error de sistema: {e}")
    
    def buscarUsuarios(self,info):
        coincidencias = []
        
        for usuario in self.Usuarios:
            if usuario.Coincide(info):
                coincidencias.append(usuario)
                
        return coincidencias
    
    def eliminarUsuario(self,usuario:Usuario):
        if usuario in self.Usuarios:
            self.Usuarios.remove(usuario)
            self.guardarUsuarios() 
                
                
    def obtenerListaImprimibleDeUsuarios(self,listaUsuarios:list[Usuario]):
        lista = [['Nombre','Telefono','Correo','Direccion','Presionar']]
        
        for i,usuario in enumerate(listaUsuarios):
            lista.append([usuario.nombre,usuario.telefono,usuario.correo,usuario.direccion,i+1])
            
        return  lista
    
    def obtenerListaDeListasDeUsuarios(self):
        lista = [['Nombre','Telefono','Correo','Direccion']]
        
        for usuario in self.Usuarios:
            lista.append([usuario.nombre,usuario.telefono,usuario.correo,usuario.direccion])
             
        return lista
    
    def __str__(self):
        return tabulate(self.obtenerListaDeListasDeUsuarios(), headers="firstrow", tablefmt="grid")
    
    @property
    def Usuarios(self):
        return self._Usuarios
    
    @Usuarios.setter
    def Usuarios(self,info):
        nombre,telefono,correo,direccion = info
        self._Usuarios.append(Usuario(nombre,telefono,correo,direccion))
        self.guardarUsuarios()
        
        
      