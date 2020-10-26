const socket = io();
socket.on("next", () => {
  Reveal.next();
});
socket.on("prev", () => {
  Reveal.prev();
});
