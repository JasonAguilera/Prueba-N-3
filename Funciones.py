PAQUETES = [pequeño,mediano,grande]
SECTOR = [norte,centro,sur]
def registar_pedido(clientes):
    print("1. Registrar pedido")
    cliente = input("Ingrese su nombre y apellido")
    direccion = input("Ingrese su dirección: ")
    sector = input("Ingrese sector donde se ubica: ").lower()
    detalles=({
        "CLIENTE"; cliente,
        "DIRECCION" ; direccion,
        "SECTOR" ; sector
    })
    


def listar_pedidos(clientes):
    for CLIENTES in clientes:
        print(CLIENTES)




def imprimir_hoja_de_ruta(clientes):
    with open("")