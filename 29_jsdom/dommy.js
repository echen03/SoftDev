var changeHeading = function(e) {
    var h = document.getElementById("h");
    h.innerHTML = e.target.innerHTML;
};

var defaultHeading = function() {
    var h = document.getElementById("h");
    h.innerHTML = "Hello World!"
};

var removeItem = function(e) {
    e.target.remove();
};

var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++) {
    lis[i].addEventListener('mouseover', changeHeading);
    lis[i].addEventListener('mouseout', defaultHeading);
    lis[i].addEventListener('click', removeItem);
}

var addItem = function(e) {
    var list = document.getElementById("thelist");
    var item = document.createElement("li");
    item.innerHTML = "WORD";
    item.addEventListener('mouseover', changeHeading);
    item.addEventListener('mouseout', changeHeading);
    item.addEventListener('click', removeItem);
    list.appendChild(item);
};

var button = document.getElementById("b");
button.addEventListener('click', addItem);

var fib = function(n) {
    if (n < 2) return 1;
    else return fib(n - 1) + fib(n -2);
};

var addFib = function(e) {
    //console.log(e);
    var list = document.getElementById("fiblist")
    var item = document.createElement("li");
    item.innerHTML = fib(list.getElementsByTagName("li").length);
    list.append(item);
};

fiblist = [];

var addFib2 = function(e) {
  //console.log(e);
  var list = document.getElementById("fiblist")
  var item = document.createElement("li");
  var len = fiblist.length;
  var ans;
  if (len < 2){
      ans = fib(len);
  }
  else{
    ans = fiblist[len - 1] + fiblist[len - 2];
  }
  fiblist.push(ans);
  item.innerHTML = ans;
  list.append(item);
};

var fb = document.getElementById("fb");
fb.addEventListener('click', addFib2);
