# D] Nested if Statement

Q1) Check if a number is greater than 10.
If yes, then check whether it is divisible by 3 and print the appropriate message.

```js
let num = 15;
if (num>10){
    if(num%3==0){
        console.log("Number greater than 10 and divisible by 3")
    }
}
```

Q2) Write a program that first checks if a person is 18 or older.
If yes, then check if they have a voter ID. Print “Can Vote” only if both conditions are true.

```js
let age = 34;
let hasVoterID = true;
if (age>=18){
    if (hasVoterID){
        console.log("Can Vote")
    }
}
```

Q3) Check if a student has scored 40 or more marks.
If yes, then check if the score is 80 or above and print “Passed with Distinction”.

```js
let marks = 85;
if (marks>=40){
    if (marks>=80){
        console.log("Passed with Distinction")
    }
}
```

Q4) Create a simple ATM system:
First check if the PIN is correct.
If PIN is correct, then check if the account balance is sufficient for withdrawal.

```js
let isPINCorrect = true;
let sufficientBalance = false;
if (isPINCorrect){
    if (sufficientBalance) {
        console.log("Withdrawal Successful")
    }
}
```

Q5) Write a program that checks if a year is divisible by 4.
If yes, then further check if it is divisible by 100.
If it is divisible by 100, then check if it is also divisible by 400 to confirm it is a leap year.

```js
let year = 2000;
if (year%4==0){
    if (year%100==0){
        if (year%400==0){
            console.log("Leap year")
        }
    }
}
```

Q6) Check if a user has entered a valid email (contains “@”).
If yes, then check if the email ends with “.com”.
If both are true, then check if the length of the email is greater than 10 characters and print “Valid Email”.

```js
let mail = "abc@gmail.com";
if (mail)
```

Q7) Write a program for online shopping:
First check if the cart total is ₹1000 or more.
If yes, then check if the user is a premium member.
If the user is premium, give 20% discount, otherwise give 10% discount.
Finally print the final amount after discount.

```js
let cartTotal = 1300;
let isMember = true
if (cartTotal>1000){
    if (isMember){
        let discount = cartTotal*20/100
        let amount = cartTotal - discount
        console.log(amount)
    }else{
        let discount = cartTotal*10/100
        let amount = cartTotal - discount
        console.log(amount)
    }
}
```

Q8) Check if a number is positive.
If yes, then check whether it is even.
If it is even, then further check if it is divisible by 4 and print “Positive Even and Divisible by 4”.

```js
let num = 32;
if (num>0){
    if (num%2==0){
        if (num%4==0){
            console.log("Positive Even and Divisible by 4")
        }
    }
}
```

Q9) Create a job eligibility checker with multiple conditions:
First check if age is between 21 and 30.
If age is valid, then check if the candidate has a graduation degree.
If the degree is present, then check if the candidate has at least 2 years of experience.
Print “Eligible for Interview” only if all three conditions are true.

```js
let age = 26;
let graduated = true;
let experience = 3;
if (age>21&&age<30){
    if (graduated){
        if (experience>=2){
            console.log("Eligible for Interview")
        }
    }
}
```

Q10) Write a nested program for exam eligibility:
First check if the student is present.
If present, then check if internal marks are ≥ 30.
If internal marks are valid, then check if external marks are ≥ 35.
Print “Eligible for Final Exam” only when all conditions are satisfied.

```js
let isPresent = true;
let internalMarks = 34;
let externalMarks = 45;
if (isPresent){
    if (internalMarks>=30){
        if (externalMarks>=35){
            console.log("Eligible for Final Exam")
        }
    }
}
```
