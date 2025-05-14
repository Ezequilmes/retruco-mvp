import envido
import cv2
import os
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return "¡Hola, Railway!"

if __name__ == "__main__":
    # Usar el puerto asignado por Railway
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host="0.0.0.0", port=port)

################
## cartas.txt ##
################
arreglo = list()

# Acceder a cartas.txt 
arch = open('cartas.txt', 'r')
for linea in arch:
    arreglo.append(linea)
arch.close() 

# Permite borrar \n que hay en la lista
arreglo = map(lambda s: s.strip(), arreglo) 

##########
## Main ##
##########

texto = envido.contarEnvido(arreglo[0],arreglo[1],arreglo[2])

path = "./Resultados/"
formato = ".png"

imagen = cv2.imread(path+"photo0"+formato)
fuente = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(imagen, texto, (10,365), fuente, 1, (256, 256, 256), 1)
cv2.imwrite(path+"photo1"+formato, imagen)

cartas = map(lambda x: x.upper(), ["as", "7", "3"])  # Ejemplo de map
cartas = list(cartas)  # Convertir a lista
socketio.emit("cartas", {"cartas": cartas})

@socketio.on("join_game")
def handle_join_game(data):
    username = data["username"]
    # Generar las cartas (ejemplo)
    cartas = ["As de Espadas", "7 de Oro", "3 de Bastos"]
    # Emitir las cartas al cliente
    socketio.emit("cartas", {"cartas": cartas})

# The following JavaScript code should be moved to a separate .js file:
# socket.on("cartas", (data) => {
#   const div = document.getElementById("cartas");
#   div.innerHTML = `<strong>Tus cartas:</strong><br>` + data.cartas.join("<br>");
# });
