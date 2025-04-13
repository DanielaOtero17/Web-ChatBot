import json
from firestore import db

def get_bot_reply(user_msg):
    
    user_msg = user_msg.lower()

    respuestas = db.collection("respuestas").stream()
    preguntas = db.collection("Keywords").stream()

    respuestas_JSON = []
    preguntas_JSON = []

    for respuesta in respuestas:
        objectA = {
          "Categoria":  f'{respuesta.id}',
           "Mensaje": f'{respuesta.get("mensaje")}'
        }
        respuestas_JSON.append(objectA)

    with open("respuestas.json", 'w') as file:
        json.dump(respuestas_JSON, file, indent=4)


    for pregunta in preguntas:
        theKeywords = []
        for keyword in pregunta.get("keywords"):
            theKeywords.append(keyword)

        objectA = {
            "Categoria":f'{pregunta.id}',
            "Keywords" : theKeywords
        }
        preguntas_JSON.append(objectA)

    with open("preguntasKeywords.json", 'w') as file:
        json.dump(preguntas_JSON, file, indent=4)


    for dupla in preguntas_JSON:
        if any(palabra in user_msg for palabra in dupla.get("Keywords")):
            return find_reply(dupla.get("Categoria"), respuestas_JSON)
    
    return noResponse(respuestas_JSON)
        

def find_reply(categoria, respuestas_JSON):

    for dupla in respuestas_JSON:
        
        if dupla.get("Categoria") == categoria:
            return(dupla.get("Mensaje"))

def noResponse(respuestas_JSON):

    message = ""
    for dupla in respuestas_JSON:
        if dupla.get("Categoria") == "noEntiendo":
            message = dupla.get("Mensaje")

    print(message)
    
    return message

        


