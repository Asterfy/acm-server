import random
    
def getRandomLetter():
    return random.choice('ABCDEFGHIJKLMN')

def getRandomUrlJsonFile(letra, edicionContest, url="htttps://acm-cusco/banco-preguntas"):
    edicionFormated = "_".join(edicionContest.lower().split())
    return f"{url}/{edicionFormated}/{letra.lower()}.json"

def CrearPreguntas(edicionContest, idContest):
    Preguntas = []
    for letter in "ABCDEFGHIJKLMN":
        url = getRandomUrlJsonFile(letter, edicionContest)
        newPregunta = {
            "letra_pregunta": letter,
            "info_pregunta": url,
            "id_contest": idContest
                   
        }
        Preguntas.append(newPregunta)
    return Preguntas