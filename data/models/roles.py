import random

def getRandomRoleName():
    return random.choice(["Student", "Member", "Admin"])

def getRandomPermission():
    return random.choice(["Read", "Write", "Delete"])

def CrearRoles(n):
    roles = []
    for _ in range(n):
        newRol = {
            "nombre_rol": getRandomRoleName(),
            "permiso": getRandomPermission()
        }
        roles.append(newRol)
    return roles