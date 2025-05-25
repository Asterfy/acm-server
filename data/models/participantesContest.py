import random

def getUniversidad():
    return random.choice(["UNSAAC", "UAC","UTEA","Universidad Continental"])

def getSemestreParticipante():
    return random.choice(["Primer", "Segundo","Tercer","Cuarto","Quinto","Sexto","Septimo","Octavo","Noveno","Decimo"])

def getCreditaje(maxCreditos=220):
    return random.randint(0, maxCreditos)

def getRandomIdEquipo(start, nroEquipos):
    return random.randint(start, nroEquipos)

def getRandomIdCompetidor(start, nroCompetidores):
    return random.randint(start, nroCompetidores)
    
def CrearParticipantesContest(n, nroEquipos, nroCompetidores, startEquipo=1, startCompetidor=1):
    participantes = []
    for _ in range(n):
        universidad = getUniversidad()
        semestre = getSemestreParticipante()
        creditaje = getCreditaje(maxCreditos=200)
        idEquipo = getRandomIdEquipo(startEquipo, nroEquipos)
        idCompetidor = getRandomIdCompetidor(startCompetidor, nroCompetidores)
        newParticipante = {
            "universidad": universidad,
            "semestre": semestre,
            "creditos": creditaje,
            "id_equipo": idEquipo,
            "id_alumno_competidor": idCompetidor
        }
        participantes.append(newParticipante)
    return participantes
        
