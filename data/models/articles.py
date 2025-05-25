import random 

especialities = ["artificial intelligence", "cybersecurity", "data science", "machine learning", "cloud computing", "web development", "mobile development", "game development", "blockchain", "internet of things"]

def getRandomArticleTitle():
    return "An Interesting aplication of " + random.choice(especialities) + " in the real world"

def getRandomDoi():
    return f"10.1000/{random.randint(100000, 999999)}"

def getRandomPdfLink(doi, url="https://acm-cusco/articles"):
    return f"{url}/pdf/{doi}"

def getRandomPublicationDate():
    return f"{random.randint(2000, 2021)}-{random.randint(1, 12)}-{random.randint(1, 28)}"


def getRandomIdMember(nroMembers, init):
    return random.randint(init, nroMembers)

def CrearArticulos(n, nroMembers=None, init=1):
    nroMembers = n if nroMembers is None else nroMembers
    articles = []
    for _ in range(n):
        newArticle = {
            "titulo_articulo": getRandomArticleTitle(),
            "doi": getRandomDoi(),
            "pdf_link": getRandomPdfLink(getRandomDoi()),
            "fecha_publicacion": getRandomPublicationDate(),
            "id_miembro": getRandomIdMember(nroMembers, init)
        }
        articles.append(newArticle)
    return articles