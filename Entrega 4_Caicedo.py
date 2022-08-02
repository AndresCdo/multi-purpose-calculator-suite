###############################################################################
#################################### RETO: TEMA 4 #############################
############################ ANDRES FELIPE CAICEDO UTENGO #####################
###############################################################################

# Aqui se importan las librerias necesarias:
import json

# Aqui se define y se inicializa las variables globales:
data_huevos = []
clasificacion = [{'tipo_huevos': 'A', 'numero_huevos': 0, 'numero_bandejas': 0}, 
                {'tipo_huevos': 'AA', 'numero_huevos': 0, 'numero_bandejas': 0}, 
                {'tipo_huevos': 'AAA', 'numero_huevos': 0, 'numero_bandejas': 0},
                {'tipo_huevos': 'BC', 'numero_huevos': 0, 'numero_bandejas': 0}]

# Aqui se deinen las funciones:
def calcular_bandejas(clasificacion):
    # Esta funcion calcula el numero de bandejas que se usaran según el tipo:
    for i in clasificacion:
        if(i['tipo_huevos'] == 'A'):
            i['numero_bandejas'] = int(i['numero_huevos']/30)
            pass
        elif(i['tipo_huevos'] == 'AA'):
            i['numero_bandejas'] = int(i['numero_huevos']/24)
            pass
        elif(i['tipo_huevos'] == 'AAA'):
            i['numero_bandejas'] = int(i['numero_huevos']/12)
            pass
        else:
            i['numero_bandejas'] = int(i['numero_huevos']/30)
            pass

def clasificacion_huevos(data_huevos):
    # Esta funcion clasifica la lista de datos de pesos de los huevos:
    for i in data_huevos:
        if(55 <= i < 60):
            clasificacion[0]['numero_huevos'] += 1
            pass
        elif(60 <= i < 69):
            clasificacion[1]['numero_huevos'] += 1
            pass
        elif(69 <= i):
            clasificacion[2]['numero_huevos'] += 1
            pass
        elif(43 <= i < 53):
            clasificacion[3]['numero_huevos'] += 1
            pass
        else:
            clasificacion[3]['numero_huevos'] += 1
            pass

if __name__ == "__main__":
    # Aqui se va a intentar cambiar los datos, por lo
    # que pueden aparecer errores relacionadas a la entrada de datos.
    # Aquí ponemos el código que puede lanzar excepciones
    data_huevos = json.loads(input())
    clasificacion_huevos(data_huevos)
    calcular_bandejas(clasificacion)

    print(clasificacion)

# ¡EL PUEBLO ES SUPERIOR A SUS DIRIGENTES!
