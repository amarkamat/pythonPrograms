//7. Create a human readable time format using the Date time object
//a. YYYY-MM-DD HH:mm
//b. DD-MM-YYYY HH:mm
//c. DD/MM/YYYY HH:mm

//6. Write a program which tells the number of days in a month.
month="june"
if (month=="january")
    console.log("31 days")
if (month=="march")
    console.log("31 days")
if (month=="june")
    console.log("30 days")

//5. Write a code which can give grades to students according
// to theirs scores:
score=90
if (score>=80 && score<=100){
    console.log("A greade")
}
else if (score>=70 && score<=89){
    console.log("B greade")
}
else if (score>=60 && score<=69){
    console.log("C greade")
}
else if (score>=50 && score<=59){
    console.log("D greade")
}
else if (score>=0 && score<=49){
    console.log("F greade")
}
else{
    console.log("Invalid score")
}

//4. Even numbers are divisible by 2 and the remainder
// is zero. How do you check, if a number is even or
// not using JavaScript?
n=10
if (n%2==0){
    console.log("Even number")
}
n=11
if (n%2!=0){
    console.log("Odd number")
}
//3. Figure out the result of the following expressions
// first without using console.log(). After you decide 
//the result confirm it by using console.log()
//a.
console.log(4 > 3 && 10 < 12)
//b.
console.log(4 > 3 && 10 > 12)
//c.
console.log(4 > 3 || 10 < 12)
//d.
console.log(4 > 3 || 10 > 12)
//e.
console.log(!(4 > 3))
//f.
console.log(!(4 < 3))
//g.
console.log(!(false))
//h.
console.log(!(4 > 3 && 10 < 12))
//i. 
console.log(!(4 > 3 && 10 > 12))
//j. 
console.log(!(4 === '4'))


//2. Boolean value is either true or false.
//a. Write three JavaScript statements which provide truthy value.
//b. Write three JavaScript statements which provide falsy value.
if (true){
    console.log(true);
}
if (10>8){
    console.log("10 greater")
}
if ("rohit"){
    console.log("rohit")
}
if (false){
    console.log(false)
}
if (0){
    console.log(0)
}
if (null){
    console.log(null)
}

//1. Declare firstName, lastName, country, city, age, isMarried,
// year variable and assign value to it and use the typeof
// operator to check different data types.
let firstName="Rohit";
let lastName="Sharma";
var country="India";
var city="Mumbai";
let age=32;
var isMarried=true;
let year=2022;
console.log(firstName, typeof(firstName));
console.log(age,typeof(age));
console.log(isMarried,typeof(isMarried));


