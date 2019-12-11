var fact = function(n){
  if (n == 1){
    return 1;
  }
  else return (n * (fact(n - 1)));
}

var fibonacci = function(n){
  if (n == 0){return 0;}
  if (n == 1){return 1;}
  return fibonacci(n - 1) + fibonacci (n - 2);
}

var gcd = function(a, b){
  if (b == 0) {return a;}
  else return gcd(b, a % b);
}

var students = ["Ethan", "David", "William"]

var randomStudent = function(){
  return students[parseInt(Math.random() * students.length)]
}
