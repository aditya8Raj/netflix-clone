// **************** comparison operators ****************
/*
> : greater than
< : less than
>= : greater than or equal to
<= : less than or equal to
== : equal to
!= : not equal to
=== : strict equal to
!== : strict not equal to
*/

// **************** logical operators ****************
/*
&& : and
|| : or
! : not
*/

// **************** ternary operator ****************
// condition ? true : false
// example code for ternary operator:
const age = 19;
age >= 18 ? console.log("You can vote") : console.log("You cannot vote");

// **************** if else ****************
if (2 === "2") {
  console.log("true");
} else {
  console.log("false");
}

// -------------------------------------

// Pracrice problems
// 1. Write a program that compares two numbers and returns true if the first number is greater than the second number.
const num1 = 19;
const num2 = 19;
if (num1 > num2) {
  console.log(`${num1} is greater than ${num2}.`);
} else if (num1 < num2) {
  console.log(`${num1} is smaller than ${num2}.`);
} else {
  console.log("Both the numbers are equal.");
}

// 2. Write a program that compares two strings and returns true if they are equal.
const str1 = "Hello";
const str2 = "False";

if (str1 == str2) {
  console.log(true);
} else {
  console.log(false);
}

// 3. Write a program that compares two boolean values and returns true if they are not equal.

const isLoggedIn = false;
const canCode = true;

if (isLoggedIn !== canCode) {
  console.log(true);
} else {
  console.log(false);
}

// **************** switch ****************

// example code for switch statement
const day = 4;

switch (day) {
  case 1:
    console.log("Monday");
    break;
  case 2:
    console.log("Tuesday");
    break;
  case 3:
    console.log("Wednesday");
    break;
  case 4:
    console.log("Thursday");
    break;
  case 5:
    console.log("Friday");
    break;
  case 6:
    console.log("Saturday");
    break;
  case 7:
    console.log("Sunday");
    break;

  default:
    console.log("Invalid day count");
    break;
}

// ------------------------------s

const month = 11;

switch (month) {
  case 1:
    console.log("January");
    break;
  case 2:
    console.log("February");
    break;
  case 3:
    console.log("March");
    break;
  case 4:
    console.log("April");
    break;
  case 5:
    console.log("May");
    break;
  case 6:
    console.log("June");
    break;
  case 7:
    console.log("July");
    break;
  case 8:
    console.log("August");
    break;
  case 9:
    console.log("September");
    break;
  case 10:
    console.log("October");
    break;
  case 11:
    console.log("November");
    break;
  case 12:
    console.log("December");
    break;

  default:
    console.log("there is no such month count");
    break;
}

//  **************** loops / iterations ****************
// ----------- for loop -----------
const myarr = ["apple", "mango", "grapes", "banana"];
for (let index = 0; index < myarr.length; index++) {
  const element = myarr[index];
  console.log(element);
}

// ---------------

for (let index = 0; index < 10; index++) {
  const element = index;
  console.log(element);
}

for (let i = 1; i <= 10; i++) {
  for (let num2 = 1; num2 <= 10; num2++) {
    console.log(i + " * " + num2 + " = " + i * num2);
  }
}

// --------------
// -------- while loop ---------
let index = 0;
while (index <= 10) {
  console.log(`Value of index is ${index}`);
  index = index + 2;
}

// ---------------
let fruits = ["apple", "mango", "grapes", "banana", "pineapple"];
let arr = 0;
while (arr < fruits.length) {
  console.log(`Fruit is: ${fruits[arr]}`);
  arr = arr + 1;
}

// ---------
// -------- do while ----------
let score = 1;
do {
  console.log(`Score is ${score}`);
  score++;
} while (score <= 10);
