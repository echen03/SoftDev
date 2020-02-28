// Ethan Chen
// SoftDev PD1
// K #07: They lock us in the tower whenever we get caught
// 2020-02-12

const canvas = document.getElementById('playground');
const context = canvas.getContext('2d');
const stopButton = document.getElementById('stop');
const animateButton = document.getElementById('animate');
const movieButton = document.getElementById('movie');

var isDrawing = false;
var circleSpeed = 0;
var movieSpeed = 0;
var id;
var dvd = new Image();
dvd.src = "dvd_logo.png";
var x = Math.random(600);
var y = Math.random(600);
var xspeed = 1;
var yspeed = 1;

var drawCircle = function(radius) {
    context.fillStyle = "blue";
    context.beginPath();
    context.arc(300, 300, radius, 0, 2 * Math.PI);
    context.fill();
    context.closePath();
};

var animateCircle = function() {
    i++;
    var radius = i % 600;
    context.clearRect(0, 0, 600, 600);
    if (radius <= 300) {
        drawCircle(radius);
    } else {
        drawCircle(600 - radius);
    }
    id = window.requestAnimationFrame(draw);
};

var animateMovie = function() {
    x = x + xspeed;
    y = y + yspeed;
    context.clearRect(0, 0, 600, 600);
    context.beginPath();
    if (x + dvd.width >= 600) {
      xspeed = -xspeed;
      x = width - dvd.width;
    } else if (x <= 0) {
      xspeed = -xspeed;
      x = 0;
    }
    if (y + dvd.height >= 600) {
      yspeed = -yspeed;
      y = height - dvd.height;
    } else if (y <= 0) {
      yspeed = -yspeed;
      y = 0;
    }
    context.drawImage(dvd, x, y);
    context.closePath();
    id = window.requestAnimationFrame(animateMovie);
}

var stop = function() {
    window.cancelAnimationFrame(id);
    isDrawing = false;
};

var circle = function() {
    if(!isDrawing){
        id = window.requestAnimationFrame(animateCircle);
        isDrawing = true;
    }
};

var movie = function(){
    if(!isDrawing){
        id = window.requestAnimationFrame(animateMovie);
        isDrawing = true;
      }
}

stopButton.addEventListener('click', stop);
animateButton.addEventListener('click', circle);
movieButton.addEventListener('click', movie);
