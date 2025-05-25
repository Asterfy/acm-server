from faker import Faker
import random as rdm

fake = Faker()

def craftCodigoAlumno(n):
    # n:cantidad de digitos
    return "".join([str(rdm.randint(0,9)) for i in range(n)])

def craftName():
    return (fake.name()).split()[0]
        
def craftNumeroTelefono():
    return "9" + "".join([str(rdm.randint(0,9)) for i in range(8)])

def craftCorreoInstitucional(codigo):
    return codigo + "@unsaac.edu.pe"

def CrearAlumnos(n):
    Alumnos = []
    for _ in range(n):
        codigo = craftCodigoAlumno(6)
        nombre = craftName()
        telefono = craftNumeroTelefono()
        correo = craftCorreoInstitucional(codigo)
        newAlumno = {
            "codigo": codigo,
            "nombres": nombre,
            "apellido_paterno": fake.last_name(),
            "apellido_materno": fake.last_name(),
            "numero_telefono": telefono,
            "correo": correo
        }
        Alumnos.append(newAlumno)
    return Alumnos