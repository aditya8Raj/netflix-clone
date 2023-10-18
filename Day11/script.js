"use strict"; // treats all JS code as newer version

// loging into the console
console.log("Welcome ADITYA RAJ");

// const  - you cannot change/re-assign the value of the variable
const myFirstName = "Aditya";
myFirstName = "Ujjwal"; // executing this line will give error
console.log(firstName);

// let  - you can change/reassign the value of the variable
let newName = "Aditya";
newName = "Ujjwal";
console.log(newName);

newName = "John";
console.log(newName);

// -------------------
console.log("-------------");
//--------------------

const myname = "Aditya";
const accID = 71000;
const email = "adityaraj@gmail.com";
const phNumber = 9876543210;
const city = "Bangalore";

console.table([myname, accID, email, phNumber, city]);

// -----------------

// alert("hello") // we are using nodejs, not browser

// *************** Data types - objects not included ***************

const myName = "aditya"; // string
const age = 18; // number
const isLoggedIn = true; // boolean - true or false
const isCool = null; // null - standalone value
const friends = undefined; // undefined - it means it has no assigned value
const mySymbol = Symbol(); // symbol -  used to create unique identifiers

// ---------------------

let score = "33";
console.log(typeof score);

let valueInNumber = Number(score);
console.log(valueInNumber);

// *************** Concatanation ****************

const firstName = "Aditya";
const lastName = " Raj";
console.log(firstName + lastName);
