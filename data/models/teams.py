import random 
from faker import Faker

fake = Faker()

array_names = ["Tiger Sharks", "Thunderbolts", "Golden Eagles", "Fire Dragons", "Ice Wolves", "Storm Riders", "Silver Hawks", "Midnight Panthers", "Sunset Serpents", "Emerald Falcons"]
especialities = ["artificial intelligence", "cybersecurity", "data science", "machine learning", "cloud computing", "web development", "mobile development", "game development", "blockchain", "internet of things"]

def CrearTeams(n):
    teams = []
    for _ in range(n):
        especiality = random.choice(especialities)
        descripcion = f"Circulo de estudios especializados en {especiality}"
        newTeam = {
            "nombre_team": random.choice(array_names),
            "description": descripcion,
        }
        teams.append(newTeam)
    return teams
    