import Usuario 

import os
import sys

from packages import tabulate

tabulate = tabulate.tabulate

tablaDeOpciones = [
    ["", "Presionar"],
    ["Agregar  Usuario", 1],
    ["Editar   Usuario", 2],
    ["Eliminar Usuario", 3],
    ["Obtener  Usuario", 4],
    ["Obtener  Usuarios", 5],
    ["Salir", 6],
]

tablaDeOpciones_EditarUsuario = [
    ["Presionar"],
    ["Nombre   ",   1],
    ["Telefono ", 2],
    ["Correo   ",   3],
    ["Direccion",4]
]

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')
    
class manejador():
    def __init__(self,gestor):
        self.Gestor = gestor
        
        self.Opciones = {
            1:self.AgregarUsuario,
            2:self.EditarUsuario,
            3:self.EliminarUsuario,
            4:self.ObtenerUsuario,
            5:self.ObtenerUsuarios,
            6:self.Salir
        }
        
        self.PantallaPrincipal()
            
    def PantallaPrincipal(self):
        clean()
        
        print('\n\tGestor de usuarios \n',tabulate(tablaDeOpciones, headers="firstrow", tablefmt="grid"),'\n')
        
        try:
            opcionSeleccionada = int(input())
        except ValueError:
            print('La opcion que elejiste no existe.\n\n')
            input()
            self.PantallaPrincipal()
            return
        
        if opcionSeleccionada in self.Opciones:
            self.Opciones[opcionSeleccionada]()
        else:
            print('Esa opcion no existe.\n\n')
            input('Presiona enter para vovler a la pantalla principal.')

            self.PantallaPrincipal()
            
         
    def AgregarUsuario(self):
        clean()
        
        try:
           telefono = int(input('Introduce el telefono del usuario\n'))
        except ValueError:
            print('El valor que introdujiste no es un numero de telefono valido.\n\n')
            input('Presiona enter para vovler a la pantalla principal.')

            self.AgregarUsuario()
            return 
         
        for usuario in self.Gestor.Usuarios:
            if usuario.telefono == telefono:
                print('Ya hay un usuario con el mismo numero de telefono.')
                self.PantallaPrincipal()
                return
        
        nombre = input('Introduce el nombre del usuario\n')
        correo = input('Introduce el correo del usuario\n')
        direccion = input('Introduce la direccion del usuario\n')
        
        self.Gestor.Usuarios = (nombre,telefono,correo,direccion)
        
        print('Usuario registrado exitosamente.\n\n')
        
        input('Presiona enter para vovler a la pantalla principal.')
        
        yn = input('Deseas agregar otro usuario? y/n\n')
        
        self.AgregarUsuario() if yn == 'y' else self.PantallaPrincipal()        

    def EditarUsuario(self):

        def editar(usuario:Usuario):
            clean()

            print(f'\n\tSelecciona que quieres editar del usuario {usuario.nombre}\n',tabulate(tablaDeOpciones_EditarUsuario, headers="firstrow", tablefmt="grid"),'\n')
            
            try:
                opcion = int(input())
            except ValueError:
                print('La opcion que elejiste no es valida.\n\n')
                input('Presiona enter para volver a intentarlo')
                editar(usuario)
                return
                
            match opcion:
               case 1:
                   nombre = input('Introduce el nuevo nombre \n')
                   usuario.nombre = nombre
               case 2:
                   telefono = input('Introduce el nuevo telefono \n')
                   usuario.telefono = telefono
               case 3:
                   correo = input('Introduce el nuevo correo \n')
                   usuario.correo = correo
               case 4:
                   direccion = input('Introduce el nuevo direccion \n')
                   usuario.direccion = direccion
               case _:
                   print('No existe esa opcion.\n\n')
                   input('Presiona enter para volver a intentarlo.')
                   
                   clean()
                   editar(usuario)
                   return
               
            self.Gestor.guardarUsuarios()
               
            opcion = input('Quieres editar otra propiedad del usuario? y/n\n')
            editar(usuario) if opcion == 'y' else self.PantallaPrincipal() 
       
        self.manejadorDeSeleccionDeUsuarios(self,editar)
            
    
    def EliminarUsuario(self):
            
        def eliminar(usuario:Usuario):
           clean()

           opcion = input(f'Estas seguro que quieres eliminar al usuario {usuario.nombre}? y/n\n')
           opcion == 'y' and self.Gestor.eliminarUsuario(usuario)

           self.PantallaPrincipal()
                
        self.manejadorDeSeleccionDeUsuarios(self,eliminar)
    
    def ObtenerUsuario(self):
        def imprimir(usuario:Usuario):
            clean()
             
            print(usuario,'\n')
            input('Presiona enter para vovler a la pantalla principal.')

            self.PantallaPrincipal() 
               
        self.manejadorDeSeleccionDeUsuarios(self,imprimir)
            
    def ObtenerUsuarios(self):
        clean()
        print(self.Gestor)
        input('Presiona enter para vovler a la pantalla principal.')
        self.PantallaPrincipal() 
    
    def Salir(self):
        clean()
        sys.exit()
    
    class manejadorDeSeleccionDeUsuarios():
        def __init__(self,manejadorDeVentana,callBack):
            self.callBack = callBack
            self.manejadorDeVentana = manejadorDeVentana
            
            self.__manejar()
            
        def __manejar(self):
            clean()
            
            info = input('Introduce el nombre, correo o telefono del usuario.\n')
            
            coincidencias = self.manejadorDeVentana.Gestor.buscarUsuarios(info)
        
            if len(coincidencias) >= 1:
                                    
                if len(coincidencias) > 1:
                    def seleccion():
                        clean()
                        imprimible = self.manejadorDeVentana.Gestor.obtenerListaImprimibleDeUsuarios(coincidencias)
                        
                        print('\tElije a que usuario quieres seleccionar\n\n',tabulate(imprimible, headers="firstrow", tablefmt="grid"),'\n')
                        
                        try:
                            opcion = int(input())
                        except ValueError:
                            print('Ese valor no es valido.\n\n')
                            input('Presiona enter para volver a intentarlo')
                            seleccion()
                            return 
                            
                        
                        for infoUsuario in imprimible:
                            if opcion == infoUsuario[-1]:
                                self.callBack(coincidencias[opcion-1]) #restar menos uno, porque Gestor.obtenerListaImprimibleDeUsuarios se le suma +1 al indice para que las opciones para el usuario no empiecen por 0
                                
                                return
                            
                        input('No existe la opcion que elejiste, vuelve a intentarlo.')
                        
                        seleccion()
                        
                    seleccion()    
                else:
                    self.callBack(coincidencias[0])
                    
            else:
                opc = input('El usuario no existe. ¿Deseas salir a la pantalla principal? y/n\n')
                
                self.manejadorDeVentana.PantallaPrincipal() if opc == 'y' else self.__manejar()

        