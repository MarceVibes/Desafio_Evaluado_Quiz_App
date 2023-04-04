import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

preguntas_elegidas = []

def choose_q(dificultad):

    #escoger preguntas por dificultad
    preguntas = p.pool_preguntas[dificultad]
    
    # usar opciones desde ambiente global
    global preguntas_elegidas

    # escoger una pregunta
    n_elegido = random.randint(1, 3)
    while n_elegido in preguntas_elegidas:

        n_elegido = random.randint(1, 3)
        if len(preguntas_elegidas) >= 3:

            preguntas_elegidas = []
    preguntas_elegidas.append(n_elegido)
    # eliminarla del ambiente global para no escogerla de nuevo
    
    if n_elegido == 1:

        pregunta = preguntas["pregunta_1"]

    elif n_elegido == 2:

        pregunta = preguntas["pregunta_2"]

    else:

        pregunta = preguntas["pregunta_3"]

    pregunta["alternativas"] = shuffle_alt(pregunta)
    # escoger enunciado y alternativas mezcladas
    alternativas = pregunta['alternativas']
    
    
    return pregunta['enunciado'], alternativas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')