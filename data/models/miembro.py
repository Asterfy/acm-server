import random
from faker import Faker

# gitub username
# password
# username
# idRol
# idAlumno 
fake = Faker()
def getGitubUsernameAndPassword():
    randomName = fake.user_name()
    return randomName, randomName + "123"
def getIdRol(limitIdRol):
    return random.randint(1, limitIdRol)
def getIdAlumno(limitIdAlumno):
    return random.randint(1, limitIdAlumno)

def CrearMiembros(n, limitIdRol, limitIdAlumno):
    miembros = []
    for _ in range(n):
        gitubUsername, password = getGitubUsernameAndPassword()
        idRol = getIdRol(limitIdRol)
        idAlumno = getIdAlumno(limitIdAlumno)
        newMiembro = {
            "github_username": gitubUsername,
            "password": password,
            "username": gitubUsername,
            "id_rol": idRol,
            "id_alumno": idAlumno
        }
        miembros.append(newMiembro)
    return miembros