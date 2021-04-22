from CEmail import Email

class Manejador:
    __email = ''
    def __init__(self, email=''):
        self.__email = email

    def CrearObjeto (self): 
        if (self.__email.find("@")!= -1) & (self.__email.find(".")!= -1):
            #se señala de donde hasta donde se va a guardar en cada uno
           idCuentas= self.__email[:self.__email.find("@")]
           dominio= self.__email[self.__email.find("@") + 1 :self.__email.find(".")]
           tipoDominio= self.__email[self.__email.find(".")+1:]
           contrasenia= input("Ingrese la contraseña: ")
           nuevoEmail= Email(idCuentas,dominio,tipoDominio,contrasenia)
           print('Id: ',idCuentas)
           print('Dominio: ', dominio)
           print('Tipo de dominio: ',tipoDominio)
           print('Contraseña: ',contrasenia)
           return(nuevoEmail)
        else:
            print('ERROR')