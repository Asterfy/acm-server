import random

def getRandomNombreSemestre():
    return str(random.randint(2010, 2024)) + "-" + str(random.choice(["I", "II"]))

def CrearSemestres(n):
    semestres = set()
    while len(semestres) < n:
        semestres.add(getRandomNombreSemestre())
    return [{
        "nombre_semestre": semestre
    } for semestre in semestres]

