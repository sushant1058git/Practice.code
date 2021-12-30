// 'use strict';
// let hasdriverslicsence=false;

// const driver=true
// if (driver) hasdriverslicsence=true

// if (hasdriverslicsence) alert("great ! you got drivers liscence");

//Function declaration
// function myfunc(apples, oranges){
//     console.log(apples, oranges)
//     const juice = `Juice with ${apples} apples and ${oranges} oranges`;
//     return juice
// }

// var res=myfunc(2,3)
// console.log(res)

// const res1=myfunc(3,6)
// console.log(res1)




// function birthCal(birthYear){
//     return 2037-birthYear
// }

// res=birthCal(1994)
// console.log(res)

//Arrow Function is helpful fro one liner function

function calcAverage(n1,n2,n3){
    return (n1+n2+n3)/3
}

a1=calcAverage(44,23,71)
a2=calcAverage(65,54,49)

function checkWinner(a1,a2){
    if (a1>=2*a2) console.log("Dolphin wins ")
    else if (a2>=2*a1) console.log("koala wins")
    else console.log("match tied")
}

checkWinner(a1, a2)