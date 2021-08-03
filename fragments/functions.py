
def individual_maze(ser, egoismo):
    lideal = ser[0]
    lsubjetivo = ser[1]
    lreal = ser[2]

    a = abs(lsubjetivo - lreal)
    b = (lideal - lreal)
    g = abs(lreal - lsubjetivo)
    if (b < 0):
        recomvir = "El modelo te sugiere re plantear tus expectativas a unas más cercanas a tú realidad"
    else:
        recomvir = "El modelo te recomienda trabajar en tu realidad para acercarla a tú ideal"       
    
    individual = (a + abs(b) + g) * egoismo  
    if (individual < 0):
        recomtotal = "El modelo te recomienda re ponderar los valores"
    else:
        recomtotal = False

    enunciado = ("dado el modelo este es el valor de cada una de las categorías, Placer {}, Virtud {}, Conocimiento {}").format(a,abs(b),g)
    if (recomtotal == False):
        return(enunciado + " " + recomvir)
    return(enunciado + " " + recomvir + " " + individual)

def world_maze(mundo, altruismo):
    lideal = mundo[0]
    lsubjetivo = mundo[1]
    lreal = mundo[2]


    a = abs(lsubjetivo - lreal)
    b = abs(lideal - lreal)
    g = abs(lreal - lsubjetivo)

    world = (a + b + g) * altruismo

def loved_maze(laberintopasion, altruismo):
    lideal = laberintopasion[0]
    lsubjetivo = laberintopasion[1]
    lreal = laberintopasion[2]


    a = abs(lsubjetivo - lreal)
    b = abs(lideal - lreal)
    g = abs(lreal - lsubjetivo)

    loved = (a + b + g) * altruismo

def lambda(individual, world, loved):
    if (loved < 5):
        lamb = indvidual + world
    else:
        lamb = individual + loved

def anguish(lamb, amor, verlaine, rimbaud):
    lis = []
    omega = lamb/amor
    for i in range(verlaine, rimbaud):
        l.append(lamb * i)

