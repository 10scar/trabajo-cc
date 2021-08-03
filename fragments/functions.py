def individual_maze(ser, egoismo):
    egoismo = int(egoismo[0])
    lideal = int(ser[0])
    lsubjetivo = int(ser[1])
    lreal = int(ser[2])

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
        return(recomvir, individual,a,abs(b),g)
    return(recomtotal + recomvir,individual, a,abs(b),g)

def world_maze(mundo, altruismo):
    altruismo = int(altruismo[1])
    lideal = int(mundo[0])
    lsubjetivo = int(mundo[1])
    lreal = int(mundo[2])


    a = abs(lsubjetivo - lreal)
    b = abs(lideal - lreal)
    g = abs(lreal - lsubjetivo)

    world = (a + b + g) * altruismo
    return(world)

def loved_maze(laberintopasion, altruismo):
    altruismo = int(altruismo[1])
    lideal = int(laberintopasion[0])
    lsubjetivo = int(laberintopasion[1])
    lreal = int(laberintopasion[2])


    a = abs(lsubjetivo - lreal)
    b = abs(lideal - lreal)
    g = abs(lreal - lsubjetivo)

    loved = (a + b + g) * altruismo
    return(loved)

def lambd(individual, world, loved):
    if (loved < 5):
        lamb = individual + world
        return(lamb)
    else:
        lamb = individual + loved
        return(lamb)

def anguish(lamb, amor, verlaine):
    lis = []
    omega = lamb/amor
    anguish = omega * verlaine
    strang = "Tú total de angustia es {}".format(int(anguish))
    return(strang)
