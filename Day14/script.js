// ****** continueing loops ******

// for of
const countries = ["India", "Nepal", "Russia", "Bangladesh"];
for (const count of countries) {
  console.log(count);
}

// ---------------

const greetings = "Hello World!";
for (const greet of greetings) {
  console.log(greet);
}

// ******** Maps *********
const map = new Map();
map.set("IN", "India");
map.set("US", "United States of America");
map.set("Fr", "France");
map.set("IN", "India"); // this will not get printed because map function only prints unique elements

console.log(map);

// ****** I am skiping some other basic concepts here because I already know them *********
