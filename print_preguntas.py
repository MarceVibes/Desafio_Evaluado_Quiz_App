import preguntas as p

def print_pregunta(enunciado, alternativas):
    
    # Imprimir enunciado y alternativas
    ###############################################################
    print(f"{enunciado[0]}\n")

    x = 0
    z = ""
    for i in alternativas:

        x += 1

        if x == 1:

            z = "A"
        elif x == 2:

            z = "B"
        elif x == 3:

            z = "C"
        else:

            z = "D"
        print(f"{z}. {i[0]}")
        
    
    
    
    
    ###############################################################
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4