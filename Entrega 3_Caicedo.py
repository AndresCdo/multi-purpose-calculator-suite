###############################################################################
#################################### RETO: TEMA 3 #############################
############################ ANDRES FELIPE CAICEDO UTENGO #####################
###############################################################################

# Aqui se importan las librerias necesarias:
import json

# Aqui se define y se inicializa las variables globales:
productos = []
resultado = 0.

if __name__ == "__main__":

    # Mientras el dicciorario este vacio:
    while len(productos) == 0:
        # Aqui se va a intentar cambiar el valor inicial del salario, por lo
        # que pueden aparecer errores relacionadas a la entrada de datos.
        try:
            # Aquí ponemos el código que puede lanzar excepciones
            productos = json.loads(input())
            # Si es un numero valido:
            if not len(productos) == 0:
                for i in productos:
                    if i['fecha_expiracion'] == 'hoy':
                        resultado += (i['precio']*(1-i['descuento']/100))*0.8
                    else:
                        resultado += i['precio']*(1-i['descuento']/100)
            else:
                pass
        except:
            # Entrará aquí en caso que se haya producido una excepción
            # tipicamente relacionada con la converción a flotante.
            print("Se ha producido un error.\nIntente ingresar un valor real.")

    print(round(resultado,2))

# ¡EL PUEBLO ES SUPERIOR A SUS DIRIGENTES!
