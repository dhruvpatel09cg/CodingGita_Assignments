# A] if Statement

Q1) Write a program to check if a number is divisible by 5. If yes, print “Divisible by 5”.

```js
let num = 45;
let isDivisibleBy5 = num % 5 == 0;
if (isDivisibleBy5) {
    console.log("Divisible by 5")
}
```

Q2) Check if a person’s age is greater than or equal to 60. If true, print “Senior Citizen”.

```js
let age = 63;
if (age>=60) {
    console.log("Senior Citizen")
}
```

Q3) Write a program that checks if a given number is greater than 100. If yes, print “Big Number”.

```js
let num = 321;
if (num>100) {
    console.log("Big number")
}
```

Q4) Check if the temperature is less than 10. If true, print “Very Cold”.

```js
let temp = 2;
if (temp<10) {
    console.log("Very cold")
}
```

Q5) Write a program to check if a student scored full marks (100). If yes, print “Perfect Score”.

```js
let marks = 100;
let fullMarks = 100;
if (marks==fullMarks){
    console.log("Perfect Score")
}
```

Q6) Check if a number is negative. If it is, print “Negative Number”.

```js
let num = -43;
if (num<0){
    console.log("Negative Number")
}
```

Q7) Write a program that checks if a user has entered an empty string. If the string is empty, print “No input provided”.

```js
let input = ""
if (input==""){
    console.log("No input provided")
}
```

Q8) Check if a given year is divisible by 100. If yes, print “Century Year”.

```js
let year = 2000;
if (year%100==0){
    console.log("Century year")
}
```

Q9) Write a program to check if a number is both positive and even using a single if condition. If true, print “Positive Even Number”.

```js
let num = 34;
if (num>0&&num%2==0){
    console.log("Positive even number")
}
```

Q10) Check if the value of a variable marks is greater than or equal to 35 and less than or equal to 100. If true, print “Valid Marks”.

```js
let marks = 35;
let validMarks = marks>=35 && marks<=100
if (validMarks){
    console.log("Valid marks")
}
```
