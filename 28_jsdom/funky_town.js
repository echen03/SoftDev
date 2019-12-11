
var fact = function(n){
  if (n == 1){
    return 1;
  }
  else return (n * (fact(n - 1)));
}

document.getElementById("1").addEventListener("click", () => console.log(fact(7)))

var fibonacci = function(n){
  if (n == 0){return 0;}
  if (n == 1){return 1;}
  return fibonacci(n - 1) + fibonacci (n - 2);
}

document.getElementById("2").addEventListener("click", () => console.log(fibonacci(7)))

var gcd = function(a, b){
  if (b == 0) {return a;}
  else return gcd(b, a % b);
}

document.getElementById("3").addEventListener("click", () => console.log(gcd(124,324)))

var students = ["Ethan", "David", "William", "Jionghao", "Tim", "Kevin"]

var randomStudent = function(){
  return students[parseInt(Math.random() * students.length)]
}

document.getElementById("4").addEventListener("click", () => console.log(randomStudent()))
