import os
import globales 
os.system("cls")

def menu_general():
    while True:
        os.system("cls")
        print("1.Asisgnar montos aleatorios")
        print("2.ver estadisticas")
        print("3.Salir del programa") 
        opcion = globales.seleccionar_opcion(3)

        if opcion  == 1:
            print("1.Asisgnar montos aleatorios")
        elif opcion ==2:
            print("2.ver estadisticas")
        elif opcion ==3:
            print("3.Salir del programa") 
            return
        
def menu_estadisticas():
    while True:
        os.system("cls")
        print("1.Productos con Valor mas alto")
        print("2.producto con iva mas bajo")
        print("3.promedio del valor de los productos")
        print("4.media geometrica")
        print("5.Salir")
        opcion = globales.seleccionar_opcion(5)

        if opcion ==1:
            print("1.Productos con Valor mas alto")
        elif opcion ==2:
            print("2.producto con iva mas bajo")
        elif opcion ==3:
            print("3.promedio del valor de los productos")
        elif opcion ==4:
            print("4.media geometrica")
        elif opcion ==5:
            print("5.Salir")
            menu_general()


menu_general()









