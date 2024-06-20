import Funciones as fn
clientes:[]

print("********************************")
print("      MENÚ      ")
print("1. Registrar pedido")
print("2. Listar los todos los pedidos")
print("3. Imprimir hoja de ruta")
print("4. Salir del programa")
opc = int(input("Seleccione una opción del 1 al 4: "))

while True:
    if opc == 1:
        fn.registar_pedido

    elif opc == 2:
        fn.listar_pedidos
    elif opc == 3: 
        fn.imprimir_hoja_de_ruta
    elif opc == 4:
        print("***SALIENDO***")
        break
    else:
        print("Opcion incorrecta, ingrese una válida")
        opc = int(input("Seleccione una opción del 1 al 4: "))