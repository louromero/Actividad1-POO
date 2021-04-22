class Email: 
    __idCuenta = ''
    __dominio = ''
    __tipoDominio= ''
    __contrasenia=''

    def __init__(self, idc='' , dom='' , tipo='' , password=''):
        self.__idCuenta= idc
        self.__dominio= dom
        self.__tipoDominio= tipo
        self.__contrasenia= password

    def retornaEmail(self):
        return (self.__idCuenta + '@' + self.__dominio + '.' + self.__tipoDominio)

    def getDominio(self):
        return (self.__dominio)

    def ModificarContrasenia(self, contraseniavieja):
        if(contraseniavieja == self.__contrasenia):
            self.__contrasenia = input('Ingrese nueva contraseña: ')
            print('La contraseña se cambió correctamente ')
            return(self.__contrasenia)
