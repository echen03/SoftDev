// Kenneth Chin
// SoftDev1 pd1
// K07 They lock us in the tower whenever we get caught
// 2020-02-13

var c = document.getElementById("playground");
var dotButton = document.getElementById( "circle" );
var stopButton = document.getElementById( "stop" );
var button2 = document.getElementById('movie');
const width = 125;
const height = 100;
var dvdId, x , y;
deltax = 1;
deltay = 1;
var logo = new Image();
logo.src = "logo_dvd.jpg";

//prepare to interact with canvas in 2D
var ctx = c.getContext("2d");

//set fill color to celine
ctx.fillStyle = "#00ffff";


var requestID;

var clear = function(e) {
  e.preventDefault();
  ctx.clearRect(0, 0, 500, 500);
};

var drawLogo = function() {
  ctx.clearRect(0,0,c.width,c.height);
  x = Math.round(Math.random() * (c.width - 250) + 125);
  y = Math.round(Math.random() * (c.height - 250) + 125);
  ctx.drawImage(logo,x,y,50,50);

}

var move= function(){
	window.cancelAnimationFrame(requestID);
	window.cancelAnimationFrame(dvdId);
	ctx.clearRect(0,0,c.width,c.height);
	x += deltax;
	y += deltay;
	//console.log(dvdX);
	if (x + 50 == c.width || x + 2 == 0){
		deltax = -1 * deltax;
		//console.log(dvdX);
	}
	if (y + 43 == c.height || y + 7 == 0){
		deltay = -1 * deltay;
		//console.log(dvdY);
	}
	ctx.drawImage(logo,x,y,50,50);
  console.log("d  ")
	dvdId = window.requestAnimationFrame(move);
}

var radius = 0;
var growing = true;


var drawDot = function() {
  window.cancelAnimationFrame( requestID );

  ctx.clearRect( 0, 0, c.width, c.height );

  if ( growing ) {
	  radius += 1;
  }
  else {
	  radius -= 1;
  }

  if ( radius == (c.width / 2) )
	  growing = false;
  else if ( radius == 0 ) {
	  growing = true;
  }

  //draw the dot
  ctx.beginPath();
  ctx.arc( c.width / 2, c.height / 2, radius, 0, 2 * Math.PI );
  ctx.stroke();
  ctx.fill();

  //console.log(requestID);
  requestID = window.requestAnimationFrame( drawDot );
};


var stopIt = function() {
  console.log( requestID );
  window.cancelAnimationFrame( requestID );
  window.cancelAnimationFrame(dvdId);
};

dotButton.addEventListener( "click", drawDot );
stopButton.addEventListener( "click",  stopIt );
button2.addEventListener("click", function(e){move(); drawLogo()});
//c.addEventListener( "click", drawDot );
//drawDot();
//dvdLogo();
