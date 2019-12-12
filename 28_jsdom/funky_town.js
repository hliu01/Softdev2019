var fibonacci = function(n){
  if (n == 0){
    return n;
  }
  if (n == 1){
    return n;
  }
  else{
    return fibonacci(n-1) + fibonacci(n-2);
  }
}

var gcdH = function(a, b, c) {
  if (a % c == 0 && b % c == 0) return c;
  else return gcdH(a, b, c-1);
};
var gcd = function(a, b) {
  if (a == b) return a;
  else if (a < b) return gcdH(a, b, a);
  else return gcdH(a, b, b);
};

var studentList = ["Me", "You", "Ed", "Joe", "Shelley", "Martha", "Gerard", "Steve", "Sally"];

var randomStudent = function(){
  var index = Math.floor(Math.random() * studentList.length);
  return studentList[index];
}


var fib = document.getElementById("fib");
fib.addEventListener("click", function(){
  console.log(fibonacci(5))
});

var gcd = document.getElementById("gcd");
g.addEventListener("click", function(){
  console.log(gcd(12,40))
});

var randomStudent = document.getElementById("randomStudent");
rand.addEventListener("click", function(){
  console.log(randomStudent())
});


ranButton.addEventListener('click', ranClick());
