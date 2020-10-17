// MIT License

// Copyright (c) 2017 Nicolas DUBIEN

// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
function play_pointer(data) {
  var frame = 1;
  var x = (document.body.offsetWidth * +data.x) / 100;
  var y = (document.body.offsetHeight * +data.y) / 100;
  var half_dimension = 5;

  var elt = document.createElement("div");
  elt.style.diplay = "block";
  elt.style.position = "absolute";
  elt.style.backgroundColor = "#ffffff";
  elt.style.borderRadius = "50%";
  elt.style.zIndex = 999;
  document.body.appendChild(elt);

  function update(elt, frame) {
    var frame_dimension = (1 + (frame - 1) / 5) * half_dimension;
    elt.style.opacity = 1 / Math.sqrt(frame);
    elt.style.left = x - frame_dimension + "px";
    elt.style.top = y - frame_dimension + "px";
    elt.style.height = 2 * frame_dimension + "px";
    elt.style.width = 2 * frame_dimension + "px";
  }
  update(elt, frame);

  function iter() {
    if (++frame >= 20) {
      document.body.removeChild(elt);
      return;
    }
    update(elt, frame);
    setTimeout(iter, 50);
  }

  setTimeout(iter, 50);
}

function play_goto(target) {
  switch (target) {
    case "prev":
      Reveal.prev();
      break;
    case "next":
      Reveal.next();
      break;
  }
}

var socket = io.connect("http://localhost:8080/");
socket.emit("register", "presenter");
socket.on("command", function (raw) {
  console.log("Received command " + raw);
  var command = JSON.parse(raw);
  switch (command.type) {
    case "pointer":
      play_pointer(command.data);
      break;
    case "goto":
      play_goto(command.data.target);
      break;
  }
});