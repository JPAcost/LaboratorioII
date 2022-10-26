def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Pagado por horas', accion1),
        '2': ('Bienvenido a la UIA ', accion2),
        '3': ('Potencias', accion3),
        '4': ('Primos ', accion4),
        '5': ('Contar Palabras', accion5),
        '6': ('Salir del programa ', salir)

    }

    generar_menu(opciones, '6')


def accion1():
     print('Por favor ahora ingrese la cantidad de horas')
     Horas=(int(input()))
     print('Porfavor ingrese el coste por horas')
     Pagar= (int(input()))
     Resultado= PagaXhoras(Horas, Pagar)
     
     
def accion2():
    print('Por favor ingrese su nombre')
    Hola=(input())
    print('Bienvenido a la UIA ', Hola.lower())
    print('Bienvenido a la UIA ', Hola.upper())


def accion3():
   print('Por favor digite un numero para poder elevarlo a la potencia ')
   entero=int(input())
   
   if (entero>=1 and entero<=11 ):
    potencia=pow(entero, 2)
    print("La potencia de su numero se elevo entre 2 el resultado es ",potencia)
   elif (entero>=11 and entero<=20 ):
    potencia=pow(entero, 4)
    print("La potencia de su numero se elevo entre 4 el resultado es ",potencia)
   elif (entero>=21 and entero<=30 ):
    potencia=pow(entero, 6)
    print("La potencia de su numero se elevo entre 6 el resultado es ")
    print(potencia)
   elif (entero>=31 and entero<=40 ):
    potencia=pow(entero, 8)
    print("La potencia de su numero se elevo entre 8 el resultado es ",potencia)
   elif (entero>=41 and entero<=50 ):
    potencia=pow(entero, 10)
    print("La potencia de su numero se elevo entre 10 el resultado es ",potencia)
   else:
     print("0")

def accion4():
    print('Por favor ingrese un numero')
    numero=((int (input())))
    Result= es_primo(numero)
    
def accion5():
    Palabra=(input())
   
    ocurrencias = Palabra.count("a")
    print("El numero de veces que aparece la letra a", ocurrencias)
    
def salir():
    print('Saliendo')


def PagaXhoras(hora_trabajadas,costo_x_hora):
    Pagar = hora_trabajadas * costo_x_hora
    result=Pagar
    print (result)

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo")
            return False
    print("Es primo")
    return True

if __name__ == '__main__':
    menu_principal()