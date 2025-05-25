import json
import psycopg2
from dotenv import load_dotenv
import os
arrayFileNames = ['alumnos', 'semestre', 'contests', 'preguntas', 'equipos', 'alumnos_competidores', 'roles',
                  'participantes_contest', 'miembros', 'teams', 'miembros_team', 'scientific_articles']
basicPath = "./datajson/"

def createSqlQuery(arrayDataDicc, tablename):
    query = f"INSERT INTO {tablename} ("
    for key in arrayDataDicc[0]:
        query += f"{key}, "
    query = query[:-2]
    query += ") VALUES "
    for dataDicc in arrayDataDicc:
        query += "("
        for key in dataDicc:
            query += f"'{dataDicc[key]}', "
        query = query[:-2]
        query += "), "
    query = query[:-2]
    query += ";"
    return query

# Conectar con la base de datos
load_dotenv("../.env")
DATABASE_URL = os.getenv("DATABASE_URL")
conn = psycopg2.connect(DATABASE_URL)

try:
    cur = conn.cursor()
    print('Connected to the database')
except:
    print('Error connecting to the database')

for fileName in arrayFileNames:
    filePath = f"{basicPath}{fileName}.json"
    with open(filePath, 'r') as file:
        data = json.load(file)
        queryToInsertData = createSqlQuery(data, fileName)
        cur.execute(queryToInsertData)
        conn.commit()
        print(f'Data inserted in {fileName} table')