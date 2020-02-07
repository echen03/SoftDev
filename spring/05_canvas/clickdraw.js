// Elizabeth Doss (Team ToothpasteCork)
// SoftDev1 pd1
// K04 -- I See a Red Door...
// 2020-02-05

var state = "box";

var c = document.getElementById("slate");
var ctx = c.getContext("2d");
//ctx.fillStyle="#ff0000";
//ctx.fillRect(50, 50, 100, 200);

var clear = function(e){
  console.log(e);
  ctx.clearRect(0, 0, c.width, c.height);
}

var toggle = function(e){
  var mode = document.getElementById("mode");
  if (state == "box"){
    state = "dot";
    mode.innerHTML = "dot";
  }
  else {
    state = "box";
    mode.innerHTML = "box";
  }
  //console.log(state);
}

var draw = function(e){
  var x = e.pageX - c.offsetLeft;
  var y = e.pageY - c.offsetTop;
  if (state == "box"){
    ctx.fillRect(x, y, 28, 28);
  }
  else {
    ctx.beginPath();
    ctx.arc(x, y, 10, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fill();
  }
}

var cle = document.getElementById("cle");
cle.addEventListener('click', clear);

var tog = document.getElementById("tog");
tog.addEventListener('click', toggle);

c.addEventListener('click', draw);


// e.preventDefault() - This command prevents a default action from occurring and
// allows the action to continue if an error occurs. For example, in our code we could
// could preventDefault in order to prevent the user from making rectangles outside of
// the box. This is not really necessary for our purposes because the canvas is a set size.

// e.beginpath() - This command allows you to start a new path or method to draw by
// emptying out the commands or subpaths previous to it. For example, if you want to
// switch the colors in which you draw from one path to another, you would use
//  beginpath after you are done using one color and proceed accordingly.
//
//  e.offsetX() - This command returns the x-coordinate with respect to the top left corner
//  of the rendered page.
//
//  e.offsetY() - This command returns the y-coordinate with respect to the top left corner
//  of the rendered page.
