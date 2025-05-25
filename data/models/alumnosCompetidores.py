import random

especialities = ["artificial intelligence", "cybersecurity", "data science", "machine learning", "cloud computing", "web development", "mobile development", "game development", "blockchain", "internet of things"]

def getDominLanguage():
    arrayLanguages = ["C++","Python","Java","Javascript","Rust","Go"]
    return random.choice(arrayLanguages)

def getEspecialization():
    return random.choice(especialities)

def getRandomAlumnoId(start,nroAlumnos):
    return random.randint(start, nroAlumnos)


def CrearAlumnosCompetidores(nroAlumnos,n,start=1):
    alumnosCompetidores = []
    for _ in range(n):
        lenguaje = getDominLanguage()
        especialidad = getEspecialization()
        idAlumno = getRandomAlumnoId(start, nroAlumnos)
        newAlumnoCompetidor = {
            "lenguaje_dominio": lenguaje,
            "area_especialidad": especialidad,
            "id_alumno":idAlumno
        }
        alumnosCompetidores.append(newAlumnoCompetidor)
    return alumnosCompetidores