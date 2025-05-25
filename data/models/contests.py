import random

def getEdicion():
    arrayEditions = ["I","II","III","IV","V","VI","VII","VII","VIII","IX","X", "XI", "XII", "XIII", "XIV", "XV", "XVI", 
                     "XVII", "XVIII", "XIX", "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX"]
    return f"Edicion {random.choice(arrayEditions)}"

def getRandomDate():
    anio = random.randint(2000, 2021)
    date = f"{anio}-{random.randint(1, 12)}-{random.randint(1, 28)}" 
    return {
        "anio": anio,
        "date": date
    }

def getRandomIdSemestre(start, nroSemestres):
    return random.randint(start, nroSemestres)

def CrearContests(nroSemestres, n, startSemestre=1):
    contests = []
    for _ in range(n):
        edicion = getEdicion()
        descripcion = f"Cuscontest - {edicion}"
        objFecha = getRandomDate()
        idSemestre = getRandomIdSemestre(startSemestre, nroSemestres)
        newContest = {
            "edicion": edicion,
            "description": descripcion,
            "fecha": objFecha["date"],
            "anio": objFecha["anio"],
            "id_semestre": idSemestre
        }
        contests.append(newContest)
    return contests
