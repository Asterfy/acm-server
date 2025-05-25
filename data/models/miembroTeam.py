import random
from faker import Faker

fake = Faker()
def getRandomDate():
    anio = random.randint(2000, 2023)
    date = f"{anio}-{random.randint(1, 12)}-{random.randint(1, 28)}" 
    return date

def getEsLider():
    return random.choice([True, False])
def getEstadoMiembro():
    return random.choice([True, False])
def getIdTeam(limitIdTeam):
    return random.randint(1, limitIdTeam)
def getIdMiembro(limitIdMiembro):
    return random.randint(1, limitIdMiembro)

def CrearMiembroTeam(n, limitIdTeam, limitIdMiembro):
    miembros = []
    for _ in range(n):
        fechaInclusion = getRandomDate()
        esLider = getEsLider()
        estadoMiembro = getEstadoMiembro()
        idTeam = getIdTeam(limitIdTeam)
        idMiembro = getIdMiembro(limitIdMiembro)
        newMiembro = {
            "fecha_inclusion": fechaInclusion,
            "es_lider": esLider,
            "estado_miembro": estadoMiembro,
            "id_team": idTeam,
            "id_miembro": idMiembro
        }
        miembros.append(newMiembro)
    return miembros
