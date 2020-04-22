// var countries = ["Senegal", "France", "USA"]

// for (var i = 0; i < countries.length; i++) {
// 	console.log(countries[0])
// };

// var mixed = [true, 20, "string"];
// console.log(mixed.length);

// var myarr = ['one', 'two', 'three']

// var lastItem = myarr.pop()

// console.log(lastItem)
// myarr.push("new_item")
// console.log(myarr)

// var matrix = [[1,2,3], [4,5,6], [7,8,9]]
// console.log(matrix)

// for (coun of countries){
// 	console.log(coun)
// }

// function addAweSome(name){
// 	console.log(name +" is AweSome" )
// }

// var topics = ["python", "django", "science"]

// topics.forEach(addAweSome)

var rooster = []

function add(){
	var new_name = prompt("What name would you like add?")
	rooster.push(new_name)
}

function remove(){
	var remName = prompt("What name would you like remove?")
	var index = rooster.indexOf(remName)
	rooster.splice(index, 1)
}

function display(){
	console.log(rooster)
}

var start = prompt("Would you like to start the rooster web app? y/n")
var request = "empty"

if (start==='y') {
	while(request!=='quit'){
		request = prompt("Please select an action: add, remove, display or quit")
		if (request==="add") {
			add();
		}else if (request==="remove") {
			remove();
		}else if (request==="display") {
			display();
		}else {
			alert('Non Reconnu')
		};
	}

};