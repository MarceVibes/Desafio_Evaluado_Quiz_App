def choose_level(n_pregunta, p_level):
    
    # Construir lógica para escoger el nivel
    ##################################################
    i = int(p_level) * 3
    x = i / 3
    if n_pregunta <= x:

        level = "basicas"
    elif n_pregunta <= x * 2 and n_pregunta > x:

        level = "intermedias"
    else:
        
        level = "avanzadas"
    
    
    ##################################################
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias