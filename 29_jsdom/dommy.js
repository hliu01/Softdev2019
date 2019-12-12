var changeHeading = function(e){
  var h = document.getElementById("h");
  h.innerHTML = e;
};

var removeItem = function(e){
};
var lis = document.getElementsByTagName("li");
for (var i=0; i<lis.length; i++)
{
  lis[i].addEventListener('click',removeItem(lis[i]));
  lis[i].addEventListener('mouseover',changeHeading(lis[i]));
  lis[i].addEventListener('mouseout',changeHeading("helloWorld"));
}



var addItem = function(e){
  var list = document.getElementById("thelist");
  var item = document.createElement("li");
  item.innerHTML = "WORD";
  list.append(item);
};
var button = document.getElementById("b");
button.addEventListener('click',addItem);
