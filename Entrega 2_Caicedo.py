###############################################################################
#################################### RETO: TEMA 2 #############################
############################ ANDRES FELIPE CAICEDO UTENGO #####################
###############################################################################

# Aqui se define y se inicializa las variables globales:
examen = -1.
lecciones = -1.
tareas = -1.
practicas = -1.
calificacion_final = 0.

if __name__ == "__main__":

    # Mientras el valor del examen no sea un valor real positivo:
    while examen < 0.:
        # Aqui se va a intentar cambiar el valor inicial del salario, por lo
        # que pueden aparecer errores relacionadas a la entrada de datos.
        try:
            # Aquí ponemos el código que puede lanzar excepciones    
            examen = float(input())
            # Si es un numero valido:
            if examen < 0:
                print("Ingrese un valor positivo.")
        except:
            # Entrará aquí en caso que se haya producido una excepción
            # tipicamente relacionada con la converción a flotante.
            print("Se ha producido un error.\nIntente ingresar un valor real.")

    # Mientras el valor de las lecciones no sea un valor real positivo:    
    while lecciones < 0.:
        # Aqui se va a intentar cambiar el valor inicial del salario, por lo
        # que pueden aparecer errores relacionadas a la entrada de datos.
        try:
            # Aquí ponemos el código que puede lanzar excepciones    
            lecciones = float(input())
            # Si es un numero valido:
            if lecciones < 0:
                print("Ingrese un valor positivo.")
        except:
            # Entrará aquí en caso que se haya producido una excepción
            # tipicamente relacionada con la converción a flotante.
            print("Se ha producido un error.\nIntente ingresar un valor real.")
    
    # Mientras el valor de las tareas no sea un valor real positivo:    
    while tareas < 0.:
        # Aqui se va a intentar cambiar el valor inicial del salario, por lo
        # que pueden aparecer errores relacionadas a la entrada de datos.
        try:
            # Aquí ponemos el código que puede lanzar excepciones    
            tareas = float(input())
            # Si es un numero valido:
            if tareas < 0:
                print("Ingrese un valor positivo.")
        except:
            # Entrará aquí en caso que se haya producido una excepción
            # tipicamente relacionada con la converción a flotante.
            print("Se ha producido un error.\nIntente ingresar un valor real.")

    # Mientras el valor de las practicas no sea un valor real positivo:
    while practicas < 0.:
        # Aqui se va a intentar cambiar el valor inicial del salario, por lo
        # que pueden aparecer errores relacionadas a la entrada de datos.
        try:
            # Aquí ponemos el código que puede lanzar excepciones    
            practicas = float(input())
            # Si es un numero valido:
            if practicas < 0:
                print("Ingrese un valor positivo.")
        except:
            # Entrará aquí en caso que se haya producido una excepción
            # tipicamente relacionada con la converción a flotante.
            print("Se ha producido un error.\nIntente ingresar un valor real.")
    
    # Se hace hace una conversion del sistema de calificacion:
    calificacion_final = 0.45*examen+0.25*lecciones+0.15*tareas+0.15*practicas
    if calificacion_final <= 2:
        print("E")
        pass
    elif calificacion_final <= 3:
        print("D")
        pass
    elif calificacion_final <= 3.5:
        print("C")
        pass
    elif calificacion_final <= 4:
        print("B")
        pass
    elif calificacion_final <= 4.5:
        print("B+")
        pass
    elif calificacion_final > 4.5:
        print("A")
        pass

# ¡EL PUEBLO ES SUPERIOR A SUS DIRIGENTES!
