const socket = io();

function unirse() {
  const username = document.getElementById("username").value;
  if (!username) return alert("Ingresá tu nombre");
  socket.emit("join_game", { username });
  document.getElementById("registro").classList.add("oculto");
  document.getElementById("mesa").classList.remove("oculto");
}

function enviarMensaje() {
  const input = document.getElementById("inputMsg");
  if (input.value.trim()) {
    socket.emit("mensaje", { msg: input.value });
    input.value = "";
  }
}

socket.on("cartas", (data) => {
  const div = document.getElementById("cartas");
  div.innerHTML = `<strong>Tus cartas:</strong><br>` + data.cartas.join("<br>");
});

socket.on("mensaje", (data) => {
  const mensajes = document.getElementById("mensajes");
  mensajes.innerHTML += `<div>${data.msg}</div>`;
});


