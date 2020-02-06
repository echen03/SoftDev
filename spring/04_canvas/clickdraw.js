const canvas = document.getElementById('slate');
const ctx = canvas.getContext('2d');
const check = document.getElementById('check');
var toggle = true;
// const on = True;

// var isChecked=document.getElementById("check").checked;
// console.log(isChecked);

var isChecked = function(e) {
  if (toggle){
    toggle = false;
  }
  else {
  toggle = true;
}
}
var draw = function(e) {
  // var isChecked=document.getElementById("check").checked;
  if (toggle){
    ctx.fillRect(e.clientX, e.clientY, 3, 3);
  }
  else{
    ctx.fillRect(e.clientX, e.clientY, 50, 10);
  }
}

// var draw2 = function(e) {
//   ctx.fillRect(e.clientX, e.clientY, 10, 10);
// }

var clear = function(e){
  ctx.clearRect(0,0,500,500);
}

// var check = function(e){
//
// }

var button = document.getElementById('clear');
button.addEventListener("click", clear);
canvas.addEventListener("click", draw);
check.addEventListener("click", isChecked);
