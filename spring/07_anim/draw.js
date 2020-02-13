// Ethan Chen
// SoftDev PD1
// K #07: They lock us in the tower whenever we get caught
// 2020-02-12

const canvas = document.getElementById('playground');
const context = canvas.getContext('2d');
const stopButton = document.getElementById('stop');
const animateButton = document.getElementById('animate');
const movieButton = document.getElementById('movie');

var i = 0;
var isDrawing = false;
var id;

var drawCircle = function(radius) {
    context.fillStyle = "blue";
    context.beginPath();
    context.arc(300, 300, radius, 0, 2 * Math.PI);
    context.fill();
    context.closePath();
};

var draw = function() {
    i++;
    let radius = i % 600;
    context.clearRect(0, 0, 600, 600);
    if (radius <= 300) {
        drawCircle(radius);
    } else {
        drawCircle(600 - radius);
    }
    id = window.requestAnimationFrame(draw);
};

var stop = function() {
    window.cancelAnimationFrame(id);
    isDrawing = false;
};

var start = function() {
    if(!isDrawing){
        id = window.requestAnimationFrame(draw);
        isDrawing = true;
    }
};

stopButton.addEventListener('click', stop);
animateButton.addEventListener('click', start);
