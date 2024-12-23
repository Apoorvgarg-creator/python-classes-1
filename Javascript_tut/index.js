// In Javascript, first What are the ways to create variables 
// Let, var and const
// console.log("This is let keyword", a)  --> This is Error : ReferenceError
// console.log("This is var keyword", b) // --> This is not an Error : ReferenceError , Result: This is var keyword undefined
// This concept is called Hoisting , and that is one of the difference between let and var
// var allows hoisting
// Q: what is Hoisting ?
// Hoisting, using a variable before initialization
// let a = 10
// var b = 30000
// const c = 10

// const pi = 3.14
// const g = 9.8

// // c = c + 10

// a = a + 10
// b = b + 19
// // console.log(c)
// console.log("This is let keyword", a)


// function sc(){
//     if( true ) {
//         var var1 = "I"
//         let var2 = "No"
//         console.log("Print", var2) // Result: Print No
//     }
//     console.log(var1) // Result: I
//     console.log(var2) // Error, because let are block-scoped variable
// }

// sc()

// Let vs Var
/// 1. Hoisting --> Var and 2. Block scoped --> Let

// Conditional Statement

// let number = prompt("Enter a number")

// process.stdout.write('Enter the number')

// process.stdin.on('data', (data) => {
//     let d = data.toString().trim();
//     const number = parseInt(d);
//     console.log(`${number} is captured`)
//     isEven(number);
//     process.exit();
// })

// Method 1
function isEven(number) {
    if(number % 2 == 0){
        console.log(`${number} is Even`)
    }else{
        console.log(`${number} is odd`)
    }
}

// Method 1 function ran even if declared below

// sayHelloVar is getting hoisted but not its value
// console.log(sayHelloVar)

// var sayHelloVar = function () {
//     console.log("Hello, VaR Function");
// }


// console.log(sayHello)
// sayHello(); // Call a function

// // Method 2 function
// let sayHello = function () {
//     console.log("Hello, Apoorv");
// }
// // Kundana ? will it run ? --> Says Yes, Reason ? 



// isEven(number);
// Hoisting - var variable, Same way functions can also do hoisting


// IIFE Functions
// IIFE --> Immediately Invoked function expression, This function has no Name !!

(function () {
    console.log("Apoorv");
}) ();


// How to transform a function into IIFE function


function callApoorv() {
    console.log("Apoorv");
}

(function () {
    console.log("Apoorv");
}) ();


// Use an IIFE Function to create a private Scope

console.log(( function () {
    let count = 0;
    return {
        increment: function () {
            count++;
            console.log(count);
        },
        reset: function () {
            count = 0;
            console.log("Counter reset");
        }
    }
})());

const counter = ( function () {
    let count = 0;
    return {
        increment: function () {
            count++;
            console.log(count);
        },
        reset: function () {
            count = 0;
            console.log("Counter reset");
        }
    }
})();


counter.increment()
counter.increment()
counter.reset()
counter.increment()
console.log(counter.count)

const dd = {
    'app' : 'project'
}

console.log(dd.count)



let fruits = ['Orange', 'Kiwi', 'Mango']
fruits.forEach((fruit) => console.log(fruit.toUpperCase()))


// Javascript 
// Callbacks !
// What is callback ? 
// --> A function passed as an argument to another function

// function fetchData(callback) {
//     setTimeout(() => {
//         console.log("Data fetched");
//         callback("Sample data")
//     }, 2000);

//     console.log("Running before");
// }

// function processData(data) {
//     console.log("Processing", data);
// }

// function anotherFunc(data) {
//     console.log("Apoorv", data);
// }
// fetchData(processData);
// fetchData(anotherFunc);

// Promise 
// Promise Object represents the eventual completion (or failure) of an asynchronous operation and its resulting value.



// const myPromise = new Promise((resolve, reject) => {
// setTimeout(() => {
//     resolve("foo");
// },300);
// });

// myPromise.then((data) => {
//     console.log("fulfilled", data);
// }).catch(() =>  console.log("Rejected"));

// function asyncOperation(callback) {
//     setTimeout( () => {
//        callback("foo")
//     },2000);
// }

// try {
//     asyncOperation((data) => {
//         console.log("fulfilled", data);
//     })
//     console.log("Are we waiting ? ");
// }catch(_) {
//     console.log("Rejected")
// }


function asyncOperation() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            // resolve("apoooorv");
            reject("Not again !!"); 
        },1000);
    })
}


async function main() {
    try {
        const result = await asyncOperation();
        console.log(result);
        console.log("We will run after this call");
        return 2;
    } catch(error) {
        console.error(error);
    }
}

async function mainWrapper() {
    const result = await main();
    console.log("completed execution", result);
}

mainWrapper();


// Pizza place, you ordered. You created a promise, that you will get a pizza in 30 mins.
// after 30 minutes --> if pizza gets delivered --> promise resolved !
// if not  --> rejected

const orderPizza = new Promise((resolve, reject) => {
    let isPizzaAvailable = true;

    setTimeout(()=> {
        if(isPizzaAvailable){
            resolve("Pizza is ready !!");
        }else{
            reject("Sorry no pizza today");
        }
    },2000);
})

orderPizza
    .then((message) => asyncOperation())
    .then((value) => console.log("ffff", value))
    .catch((error) => console.error(error));

// it makes your code cleaner and easier to read than traditional callback functions

// chain promises
