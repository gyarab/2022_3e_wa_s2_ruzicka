setInterval(pepa, 10);

let body = document.getElementsByTagName("body");
let img = document.getElementsByTagName("img");

let ry = 1;
let rx = 1;

let x = 0;
let y = 0;

function getWidth() {
    return Math.max(
      document.body.scrollWidth,
      document.documentElement.scrollWidth,
      document.body.offsetWidth,
      document.documentElement.offsetWidth,
      document.documentElement.clientWidth
    );
  }
  
  function getHeight() {
    return Math.max(
      document.body.scrollHeight,
      document.documentElement.scrollHeight,
      document.body.offsetHeight,
      document.documentElement.offsetHeight,
      document.documentElement.clientHeight
    );
  }

function pepa() {
    body[0].style.backgroundColor = "rgb(" + Math.random() * 255 + "," + Math.random() * 255 + "," + Math.random() * 255 + ")";
    if (x >= getWidth()-200 || x < 0) {
        rx = -rx
    }
    if (y >= getHeight()-200 || y < 0) {
        ry = -ry
    }
    x += rx
    y += ry
    img[0].style.top = y + "px";
    img[0].style.left = x + "px";
}