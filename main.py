import os
import cv2
from flask import Flask
from flask_socketio import SocketIO
import envido

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return "¡Hola, Railway!"

################
## cartas.txt ##
################
arreglo = list()

# Acceder a cartas.txt 
arch = open('cartas.txt', 'r')
for linea in arch:
    arreglo.append(int(linea.strip()))  # Elimina espacios en blanco o caracteres de nueva línea
arch.close() 

# Permite borrar \n que hay en la lista
arreglo = list(map(lambda s: s.strip(), arreglo))  # Convertir map a lista

##########
## Main ##
##########

texto = envido.contarEnvido(arreglo[0], arreglo[1], arreglo[2])

path = "./Resultados/"
formato = ".png"

imagen = cv2.imread(path + "photo0" + formato)
fuente = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(imagen, texto, (10, 365), fuente, 1, (256, 256, 256), 1)
cv2.imwrite(path + "photo1" + formato, imagen)

cartas = ["As de Espadas", "7 de Oro", "3 de Bastos"]

@socketio.on("join_game")
def handle_join_game(data):
    username = data["username"]
    # Emitir las cartas al cliente
    socketio.emit("cartas", {"cartas": cartas})

if __name__ == "__main__":
    # Usar el puerto asignado por Railway
    port = int(os.environ.get("PORT", 5000))  # Obtiene el puerto de la variable de entorno PORT
    socketio.run(app, host="0.0.0.0", port=port)  # Escucha en el puerto asignado
