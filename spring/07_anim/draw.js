// Ethan Chen
// SoftDev PD1
// K #07: They lock us in the tower whenever we get caught
// 2020-02-12

const canvas = document.getElementById('playground');
const context = canvas.getContext('2d');
const stopButton = document.getElementById('stop');
const animateButton = document.getElementById('animate');

var i = 0;
var isDrawing = false;
var id;

const drawCircle = (radius) => {
    context.fillStyle = "blue";
    context.beginPath();
    context.arc(300, 300, radius, 0, 2 * Math.PI);
    context.fill();
    context.closePath();
};

const draw = () => {
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

const stop = () => {
    window.cancelAnimationFrame(id);
    isDrawing = false;
};

const start = () => {
    if(!isDrawing){
        id = window.requestAnimationFrame(draw);
        isDrawing = true;
    }
};

stopButton.addEventListener('click', stop);
animateButton.addEventListener('click', start);
