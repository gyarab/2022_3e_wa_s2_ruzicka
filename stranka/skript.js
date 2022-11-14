setInterval(pepa, 30);

let body = document.getElementsByTagName("body");

function pepa() {
    body[0].style.backgroundColor = "rgb(" + Math.random() * 255 + "," + Math.random() * 255 + "," + Math.random() * 255 + ")";
}