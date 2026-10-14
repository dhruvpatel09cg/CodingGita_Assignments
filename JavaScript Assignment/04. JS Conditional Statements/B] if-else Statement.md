# B] if-else Statement

Q1) Write a program to check whether a number is even or odd.

```js
let num = 54;
if (num%2==1){
    console.log("Odd number")
}else{
    console.log("Even number")
}
```

Q2) Check if a person is eligible to vote (age ≥ 18). Print “Eligible” or “Not Eligible”.

```js
let age = 33;
if (age>=18){
    console.log("Eligible")
}else{
    console.log("Not Eligible")
}
```

Q3) Write a program that checks whether a number is positive or negative.

```js
let num = 4;
if (num>=0){
    console.log("Positive")
}else{
    console.log("Negative")
}
```

Q4) Check if a student has passed or failed based on marks (pass mark = 35).

```js
let marks = 24;
if (marks>=35){
    console.log("Pass")
}else{
    console.log("Fail")
}
```

Q5) Write a program to check whether a given character is an uppercase letter or not.
(Hint: Use character comparison)

```js
let chr = "j";
if (chr>="A" && chr<="Z"){
    console.log("Uppercase")
}else{
    console.log("Lowercase")
}
```

Q6) Check if a number is divisible by 3 or not. Print appropriate messages.

```js
let num = 5;
if (num%3==0){
    console.log("Divisible by 3")
}else{
    console.log("Not divisible by 3")
}
```

Q7) Write a program that takes a password as input. If the password is “admin123”, print “Login Successful”, otherwise print “Incorrect Password”.

```js
let password = "Admin1234"
if (password=="admin123"){
    console.log("Login Successful")
}else{
    console.log("Incorrect Password")
}
```

Q8) Check whether a given year is a leap year or not using the basic rule (divisible by 4).

```js
let year = 2034;
if (year%4==0){
    console.log("Leap year")
}else{
    console.log("Not a Leap year")
}
```

Q9) Write a program to find the greater of two numbers using if...else.

```js
let a = 53;
let b = 23;
if (a>b){
    console.log("a is greater")
}else{
    console.log("b is greater")
}
```

Q10) Check if a number is positive, negative, or zero using only if...else (you may use nested or multiple conditions carefully).

```js
let num = 0;
if(num>=0){
    if(num==0){
        console.log("Zero")
    }else{
        console.log("Positive")
    }
}else{
    console.log("Negative")
}
```
