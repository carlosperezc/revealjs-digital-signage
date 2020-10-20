var socket = io.connect("http://localhost:8080/");
socket.emit("register");
socket.on("command", function (raw) {
  var command = JSON.parse(raw);
  if (command.type == "goto") {
    if (command.data.target == "prev") {
      Reveal.prev();
    } else if (command.data.target == "next") {
      Reveal.next();
    }
  }
});