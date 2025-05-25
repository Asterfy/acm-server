import json

from models.alumnos import CrearAlumnos
from models.alumnosCompetidores import CrearAlumnosCompetidores
from models.articles import CrearArticulos
from models.contests import CrearContests
from models.equipos import CrearEquipos
from models.miembro import CrearMiembros
from models.miembroTeam import CrearMiembroTeam
from models.participantesContest import CrearParticipantesContest
from models.preguntas import CrearPreguntas
from models.roles import CrearRoles
from models.semestres import CrearSemestres
from models.teams import CrearTeams

def createAndSaveJsonFile(arrayData, fileName):
    with open(f'{fileName}', 'w') as file:
        json.dump(arrayData, file, ensure_ascii=False, indent=4)
# Definir cantidad de datos
nroAlumnos = 60
nroAlumnosCompetidores = 45
nroArticulos = 30
nroContests = 10
nroEquipos = 12
nroMiembros = 25
nroMiembroTeam = 25
nroParticipantesContest = 45
nroPreguntasXcontest = 10
nroRoles = 5
nroSemestres = 10
nroTeams = 5

# Crear datos
arrayAlumnos = CrearAlumnos(nroAlumnos)
arraySemestres = CrearSemestres(nroSemestres)
arrayContests = CrearContests(nroSemestres, nroContests)
arrayPreguntas = []
for index, contest in enumerate(arrayContests):
    arrayPreguntas += CrearPreguntas(contest["edicion"], index+1)
arrayEquipos = CrearEquipos(10, nroContests, nroEquipos)
arrayAlumnosCompetidores = CrearAlumnosCompetidores(nroAlumnos, nroAlumnosCompetidores)
arrayParticipantesContest = CrearParticipantesContest(nroParticipantesContest, nroEquipos, nroContests)
arrayMiembros = CrearMiembros(nroMiembros, nroRoles, nroAlumnos)
arrayTeams = CrearTeams(nroTeams)
arrayMiembrosTeam = CrearMiembroTeam(nroMiembroTeam, nroTeams, nroMiembros)
arrayRoles = CrearRoles(nroRoles)
arrayArticulos = CrearArticulos(nroArticulos, nroMiembros)

# Guardar datos
basePath = "./datajson/"
createAndSaveJsonFile(arrayAlumnos, basePath + "alumnos.json")
createAndSaveJsonFile(arraySemestres, basePath + "semestre.json")
createAndSaveJsonFile(arrayContests, basePath + "contests.json")
createAndSaveJsonFile(arrayPreguntas, basePath + "preguntas.json")
createAndSaveJsonFile(arrayEquipos, basePath + "equipos.json")
createAndSaveJsonFile(arrayAlumnosCompetidores, basePath + "alumnos_competidores.json")
createAndSaveJsonFile(arrayParticipantesContest, basePath + "participantes_contest.json")
createAndSaveJsonFile(arrayMiembros, basePath + "miembros.json")
createAndSaveJsonFile(arrayTeams, basePath + "teams.json")
createAndSaveJsonFile(arrayMiembrosTeam, basePath + "miembros_team.json")
createAndSaveJsonFile(arrayRoles, basePath + "roles.json")
createAndSaveJsonFile(arrayArticulos, basePath + "scientific_articles.json")
