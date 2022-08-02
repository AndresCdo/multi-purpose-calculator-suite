###############################################################################
#################################### RETO: TEMA 1 #############################
############################ ANDRES FELIPE CAICEDO UTENGO #####################
###############################################################################

# Aqui se define y se inicializa las variables globales:
salario = 0.
compra_de_alimentos = 0.
compra_de_pasajes = 0.
compra_de_boletos_de_cine = 0.
compra_de_libros = 0.
alquiler = 0.

if __name__ == "__main__":

    # Mientras el valor del salario no sea un valor real positivo:
    while salario <= 0.:
        # Aqui se va a intentar cambiar el valor inicial del salario, por lo
        # que pueden aparecer errores relacionadas a la entrada de datos.
        try:
            # Aquí ponemos el código que puede lanzar excepciones    
            salario = float(input("Ingrese el valor en pesos de su salario: "))
            # Si es un numero valido:
            if salario == 0:
                # No debe ser cero.
                print("Ingrese un valor distinto de cero.")
            elif salario < 0:
                print("Ingrese un valor positivo.")
            else:
                # Se hace una distribucion del salario entre los gastos:
                compra_de_alimentos = 0.1*salario
                compra_de_pasajes = 0.15*salario
                compra_de_boletos_de_cine = 0.05*salario
                compra_de_libros = 0.1*salario
                alquiler = salario-(compra_de_alimentos+compra_de_pasajes
                    +compra_de_boletos_de_cine+compra_de_libros)
                print(f"Su salario es de {salario} pesos colombianos.")
                print(f"Se destina {compra_de_alimentos} pesos para compra") 
                print(f"de alimentos, {compra_de_pasajes} pesos para compra")
                print(f" de pasajes, {compra_de_boletos_de_cine} pesos para")
                print(f" compra de boletos de cine, {compra_de_libros}")
                print(" pesos para compra de libros y el resto,")
                print(f" {alquiler} pesos, para el alquiler.")

        except:
            # Entrará aquí en caso que se haya producido una excepción
            # tipicamente relacionada con la converción a flotante.
            print("Se ha producido un error.\nIntente ingresar un valor real.")

# ¡EL PUEBLO ES SUPERIOR A SUS DIRIGENTES!
