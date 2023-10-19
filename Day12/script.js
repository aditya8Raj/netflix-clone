/*
************* Return type of variables in JavaScript ***************

1) Primitive Datatypes
       Number => number
       String  => string
       Boolean  => boolean
       null  => object
       undefined  =>  undefined
       Symbol  =>  symbol
       BigInt  =>  bigint

2) Non-primitive Datatypes
       Arrays  =>  object
       Function  =>  function
       Object  =>  object
*/

// correct way to declare variables
const myName = "Aditya";
const work = "Software Developer";
const age = 21;

console.log(
  `My name is ${myName} and I am ${age} years old. I work as a ${work}.`
);

// -------------------

// ********* Dates **********
let myDate = new Date();
console.log(myDate); // 2023-10-19T06:12:49.940Z
console.log(myDate.toString()); // Thu Oct 19 2023 11:40:39 GMT+0530 (India Standard Time)
console.log(myDate.toDateString()); // Thu Oct 19 2023
console.log(myDate.toLocaleString()); // 19/10/2023, 11:40:39 am
console.log(typeof myDate);

// ******** arrays *********
const myArr = ["hello", 17, true];
console.log(myArr[0]);

// ******* objects *********
// object literals
const myObj = {
  name: "Aditya",
  age: 18,
  email: "test@email.com",
  location: "India",
  isLoggedIn: false,
};

console.log(myObj);
console.log(typeof myObj);
console.log(myObj.email);

// ********** Functions ***********

function sayMyName() {
  console.log("A");
  console.log("D");
  console.log("I");
  console.log("T");
  console.log("Y");
  console.log("A");
}

sayMyName();

// ****** functions with parameters & arguments ********

function addTwoNumbers(num1, num2) {
  const result = num1 + num2;
  return result;
}

console.log(addTwoNumbers(5, 3));

// ---------------

if (true) {
  let a = 10;
  const b = 20;
}

// console.log(a);
// console.log(b);
// console.log(c);

//********* this keyword **********/

const user = {
  username: "aditya",
  price: 999,

  welcomeMessage: function () {
    console.log(`${this.username}, welcome to website`);
  },
};

user.welcomeMessage();
user.username = "ujjwal";
user.welcomeMessage();

// ********** arrow functions ***********
const addTwo = (num1, num2) => {
  return num1 + num2;
};

console.log(addTwo(3, 5));

// ******* Immediately Invoked Function Expressions (IIFI) *******
(function sayHello() {
  console.log("Hello");
})(); // Hello

function sayHello() {
  console.log("Hello");
}

sayHello(); // Hello
