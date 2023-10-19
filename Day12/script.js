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
