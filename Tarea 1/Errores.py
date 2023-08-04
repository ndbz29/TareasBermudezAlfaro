#Codigos de error unico para separa:letras:
# -100 El parametro recibido no es un String
# -200 El string no contine solo letras del abecedario
# -300 El string esta vacio

# Codigos de exito unico:
# 0 El string cumple con los verificaciones realizadas

def separa_letras(cadena):
    # Se verifica si lo recibido es un string
    # Si no es un string se retorna lo siguiente
    if not isinstance(cadena, str):
        return -100, None, None

    # Se verificar si el string esta vacio primero antes que si solo letras

    # Asi se evita el codigo de error unico erroneo,
    # ya que esto tambien cumple el no ser solo letras del abecedario
    # El strip quita espacios y si la cadena es vacia, retorna el error
    if not cadena.strip():
        return -300, None, None

    # Se verifica si el string contiene unicamente letras del abecedario

    # Utilizando isalpha se verifica si cadena es solo letras
    if not cadena.isalpha():
        return -200, None, None

    # Proceso de separar el string en los strings de may�sculas y min�sculas

    # Separar el string en letras mayusculas
    # Se utiliza la funcion .join que concatena iterables de la lista
    # Esta utiliza una lista que se arma con for que verifica si es mayuscula
    lista_mayusculas = [letra1 for letra1 in cadena if letra1.isupper()]
    mayusculas = "".join(lista_mayusculas)

    # Separar el string en letras min�sculas
    # Se utiliza la funcion join que concatena iterables de la lista
    # Esta utiliza una lista que se arma con for que verifica si es minuscula
    lista_minusculas = [letra2 for letra2 in cadena if letra2.islower()]
    minusculas = "".join(lista_minusculas)

    return 0, mayusculas, minusculas

# Codigos de error unico para potencia_manual:
# -400 Caso que entrada sea string
# Codigos de exito unico:
# 0 Potencia correcta sin multiplicaciones


def potencia_manual(base,exponente):
    # definicion de la funcion con dos parámetros
    # revisa que ningún parámetro sea de tipo str
    if isinstance(base, str) | isinstance(exponente, str):
        estado = -400
        result = None
        return estado, result
        # si es el caso devuelve código de error y none como resultado si no es así continúa al cálculo
    else:
        # si el exponente es cero, el resultado es uno. Caso especial
        if exponente == 0:
            estado = 0
            result = 1
            return estado, result  # el código de éxito es cero
        else:
            # para exponente distinto de cero
            # recursion y anterior son variables usadas en el loop for
            recursion = base
            anterior = base
            estado = 0
            # 0 es código de éxito
            # debe realizar la operación a*a "exponente menos uno" veces
            # por ejemplo 3xx3 corresponde a (3*3)*3,
            # Esto es 2 multiplicaciones
            for i in range(exponente-1):
                # En vez de multiplicar se suma a la base ella misma
                # "base menos uno" veces
                # Ejemplo 3xx3 corresponde a 3+3+3, como el primer 3 ya existe,
                # se le suma sí mismo dos veces.
                for j in range(base-1):
                    recursion += anterior
                    if j == base-2:
                        # como 3x3x3 es 9x3, se actualiza el valor recursivo
                        # es decir, ahora es 9 se suma a sí mismo las 2 veces
                        anterior = recursion
            result = recursion
            return estado, result
            # se devuelve el resultado

# Errores:
# Errores.py:1:1: E265 block comment should start with '# '
# Errores.py:51:25: E231 missing whitespace after ','
# Errores.py:58:80: E501 line too long (103 > 79 characters)
