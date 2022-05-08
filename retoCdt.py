def CDT(usuario:str, capital:int, tiempo:int):
    if tiempo <= 2:
        return penalidad(usuario, capital, tiempo)
    else:
        return ganancias(usuario, capital, tiempo)
    
def ganancias(usuario, capital, tiempo):
    interes = (capital * 0.03 * tiempo)/12
    totalrecibido = capital + interes
    return  f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {totalrecibido}' # El los mismo corchetes tambien 
                                                                                                                                                                # se pueden hacer operaciones
                                                                                                                                                                # ya que con la concatenacion mas comun de suma o comas
                                                                                                                                                                # Python no acepta string con enteros, tendria que colocar el tipo str a cada parametro.
                                                                                                                                                                # por ejemplo "hola " + str(nombre)+"tengo" + str(edad) + "años"
def penalidad(usuario, capital, tiempo):
    perdida = capital - (capital * 0.02)
    return f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {perdida}'

print(CDT("AB1012",1000000,3))
print(CDT("ER3366",650000,2))

# Este codigo tambien lo podemos hacer de una manera mas reducida con condicionales.

def CDT(usuario: str, capital: int, tiempo: int):
    if tiempo > 2:
        valor_intereses = (capital * 0.03 * tiempo)/12
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_intereses}"
    else:
        valor_perder = capital * 0.02
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_perder}"
    
print(CDT("AB1012",8000000,1))
print(CDT("ER3366",765000,2))
    
    