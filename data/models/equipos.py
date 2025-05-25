import random
from faker import Faker

array_names = ["Tiger Sharks", "Thunderbolts", "Golden Eagles", "Fire Dragons", "Ice Wolves", "Storm Riders", "Silver Hawks", "Midnight Panthers", "Sunset Serpents", "Emerald Falcons"]

def getNombreEquipo():
    return random.choice(array_names)

def getCategoria():
    return random.choice(["Basico","Intermedio","Avanzado"])

def getPuesto(maxPuesto=15):
    return random.randint(1,maxPuesto)

def getRandomContestId(start,nroContests):
    return random.randint(start, nroContests)

def CrearEquipos(nroMaxPuesto, nroContests, n, startContest=1):
    equipos = []
    for _ in range(n):
        nombre = getNombreEquipo()
        categoria = getCategoria()
        puesto = getPuesto(maxPuesto=nroMaxPuesto)
        idContest = getRandomContestId(startContest, nroContests)
        newEquipo = {
            "nombre_equipo": nombre,
            "categoria": categoria,
            "puesto": puesto,
            "id_contest": idContest
        }
        equipos.append(newEquipo)
    return equipos
    