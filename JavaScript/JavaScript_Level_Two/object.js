// var myheader = document.querySelector("h1");
// myheader.style.color = "red";
console.log("test");

var headOne = document.querySelector('#pickme');

headOne.addEventListener('mouseover', function(){
	headOne.textContent = "Mouse Currently Over"
	headOne.style.color = "red";
})