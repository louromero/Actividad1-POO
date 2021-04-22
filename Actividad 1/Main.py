import csv
from CEmail import Email
from CManejadorEmail import Manejador

def imprimir():
    print("---------- MENU --------")
    print("Opciones disponibles:")
    print("1. Ingresar datos para crear un Email")
    print("2. Cambiar contraseña ")
    print("3. Crear objeto a partir de un email")
    print("4. Contar cuantos email coinciden con el dominio")
    print("0. Salir")
    print()

def menu():
    while True:
        imprimir()
        try:
            entrada_usuario = int(input("Seleccione una opcion:  "))
            if entrada_usuario in range(5):

                #Punto 1 - Crear Cuenta
                if entrada_usuario == 1:
                    print(' ')
                    print('Ingrese los siguientes datos: ')
                    nombre = input('Nombre: ')
                    idCuenta = input('Id de la cuenta: ')
                    dominio = input('Dominio de la cuenta: ')
                    tipoDominio = input('Tipo de dominio de la cuenta: ')
                    contrasenia = input('Contraseña: ')
                    mail = Email(idCuenta, dominio, tipoDominio, contrasenia)
                    print('\n Estimado {} te enviaremos tus mensajes a la dirección {} \n '.format(nombre, mail.retornaEmail()))

                #Punto 2 - Cambiar contraseña
                if entrada_usuario == 2:
                    print(' ')
                    print('Se procederá a cambiar la contraseña que se ingresó anteriormente.\n')
                    print(' ')
                    contrasenia = input('Ingrese contraseña actual: ')
                    #mail.ModificarContrasenia(contrasenia)
                    print('La contraseña nueva e3s: {} '.format(mail.ModificarContrasenia(contrasenia)))

                #Punto 3 - Crear Objeto de Clase Email
                if entrada_usuario == 3:
                    print(' ')
                    print('Se creará un objeto de tipo Email ')
                    mail= input('Ingrese un mail: ')
                    #mail = Manejador(input('Ingrese un mail: '))
                    correo= Manejador(mail)
                    objetonuevo = correo.CrearObjeto()
                    if isinstance(objetonuevo, Email):
                    #if type(objetonuevo) == Email:
                        print('El correo creado es: ',mail )
                        print('El identificador del objeto creado es  ', objetonuevo)
                        print(' ')

                #Punto 4 - Leer archivo
                if entrada_usuario == 4:
                    print(' ')
                    archivo = open('email.csv')
                    #Manejador.CrearObjeto("email.csv")
                    dominio = input('Ingrese un dominio: ')
                    cont = 0
                    #archivo = open('email.csv')
                    reader = csv.reader(archivo, delimiter=',')
                    for fila in reader:
                        if fila[1] == dominio:
                            cont+=1
                            
                    else: 
                        print('La cantidad de mails con el dominio ingresado es:{}'.format(cont))
                        print(' ')
                        archivo.close()


                if entrada_usuario == 0:
                    print("Programa Finalizado")
                    break


            else:
                print('\nError, solo de aceptan numeros del 0 al 4\n')

        except ValueError:
            print("\nError, ingrese solamente numeros\n")


if __name__ == '__main__':
    menu()