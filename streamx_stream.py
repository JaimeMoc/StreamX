# Codigo principal para el proyecto de captura de datos a X.
# Jaime Alberto Suarez Moctezuma. 

#Importamos las líbrerias necesarias. 
import os # Nos permite acceder a la variable de entorno.
import requests # Para poder realizar las peticiones.
import json # Json para manejar los datos en formatos JSON.
from dotenv import load_dotenv # Nos permiten cargar las variables de entorno del archivo .env

# Cargamos las variables del archivo .env
load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Función para las cabeceras necesarias a cada petición HTTP.
def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {BEARER_TOKEN}"
    r.headers["User_Agent"] = "StreamXDataCollector"
    return r

# Función para definir las reglas de filtrado para el Stream.
def set_stream_rules():
    rules_url = "https://api.twitter.com/2/tweets/search/stream/rules"
    # Obtiene reglas actuales para eliminarlas y evitar duplicados
    if "data" in existing_rules: 
        ids = [rule["id"] for rule in existing_rules["data"]]
        payload = {"delete": {"ids": ids}}
        del_response = requests.post(rules_url, auth=bearer_oauth, json=payload)
        print("Eliminando reglas previas", del_response.status_code, del_response.text)

    # Define nuevas reglas para filtrar tweets sobre estos temas.
    rules = {
        "add": [
            {"value": "#JusticiaSocial lang:es"},
            {"value": "#DerechosHumanos lang:es"},
            {"value": "igualdad lang:es"},
            {"value": "discriminación lang:es"},
            {"value": "pobreza lang:es"},
            {"value": "educación lang:es"},
            {"value": "salud pública lang:es"},
            {"value": "cambio climático lang:es"},
            {"value": "violencia lang:es"},
            {"value": "inclusión lang:es"},
            {"value": "movimiento social lang:es"},
            {"value": "protesta lang:es"},
            {"value": "libertad lang:es"},
            {"value": "democracia lang:es"},
            {"value": "racismo lang:es"}
        ]
    }
    # Envía las reglas a Twitter para activar el filtro.
    response = requests.post(rules_url, auth=bearer_oauth, json=rules)
    print("Reglas añadidas: ", response.status_code, response.text)

# Función para conectarse al stream de tweets en tiempo real.
def connect_stream():
    stream_url = "https://api.twitter.com/2/tweets/search/stream?tweet.fields=created_at,author_id,lang"
    response = requests.get(stream_url, auth=bearer_oauth, stream=True)

    if response.status_code != 200:
        raise Exception(f"Error al conectarse: {response.status_code} {response.text}")
    
    print("Conectado al stream...")

    for line in response.iter_lines():
        if line:
            tweet = json.loads(line)
            print(json.dumps(tweet, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    set_stream_rules() # Configuramos las reglas.
    connect_stream() # Inicia la captura en tiempo real. 