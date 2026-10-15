# C] if-else if-else Statement

Q1) Write a program that takes a month number (1–12) and prints the corresponding season:
Winter (12, 1, 2), Summer (3, 4, 5), Monsoon (6, 7, 8), Autumn (9, 10, 11).

```js
let monthNumber = 5;
if (monthNumber<=0||monthNumber>12){
    console.log("Invalid month")
}else if(monthNumber<=2||monthNumber==12){
    console.log("Winter")
}else if(monthNumber<=5){
    console.log("Summer")
}else if(monthNumber<=8){
    console.log("Monsoon")
}else{
    console.log("Autumn")
}
```

Q2) Create a simple tax calculator based on income:
Income < 3,00,000 → No tax
3,00,000 – 7,00,000 → 5% tax
7,00,000 – 10,00,000 → 10% tax
Above 10,00,000 → 15% tax
Print the tax amount.

```js
let income=340000;
if(income<300000&&income>=0){
    console.log("No tax")
}else if(income<700000){
    console.log("5% tax")
    let tax = income*5/100
    console.log(tax)
}else if(income<1000000){
    console.log("10% tax")
    let tax = income*10/100
    console.log(tax)
}else{
    console.log("15% tax")
    let tax = income*15/100
    console.log(tax)
}
```

Q3) Write a program that checks a student’s score and prints:
“Outstanding” (90 and above), “Good” (70–89), “Average” (40–69), “Needs Improvement” (below 40).

```js
let marks = 64;
if (marks>=90&&marks<=100){
    console.log("Outstanding")
}else if(marks>=70){
    console.log("Good")
}else if(marks>40){
    console.log("Average")
}else if(marks>0){
    console.log("Needs Improvement")
}else{
    console.log("Invalid")
}
```

Q4) Check the speed of a vehicle and print:
“Slow” (below 40), “Normal” (40–80), “Fast” (above 80)

```js
let speed = 56;
if (speed<=40&&speed>0){
    console.log("Slow")
}else if (speed<=80){
    console.log("Normal")
}else{
    console.log("Fast")
}
```

Q5) Write a program that checks a person’s height (in cm) and prints:
“Short” (< 150), “Average” (150–170), “Tall” (> 170).

```js
let height=183;
if (height<150&&height>0){
    console.log("Short")
}else if (height<170){
    console.log("Average")
}else{
    console.log("Tall")
}
```

Q6) Check the day number (1–7) and print whether it is a Weekday or Weekend
(1 to 5 = Weekday, 6 and 7 = Weekend).

```js
let dayNumber = 6;
if (dayNumber>0&&dayNumber<=5){
    console.log("Weekday")
}else{
    console.log("Weekend")
}
```

Q7) Write a program that calculates electricity bill based on units:
0–50 units → ₹2 per unit
51–150 units → ₹4 per unit
Above 150 units → ₹6 per unit
Print the total bill.

```js
let unitsUsed = 63;
if (unitsUsed>0&&unitsUsed<=50){
    bill = unitsUsed*2
    console.log(bill)
}else if(unitsUsed<=150){
    bill = unitsUsed*4
    console.log(bill)
}else{
    bill = unitUsed*6
    console.log(bill)
}
```

Q8) Create a program that checks a student’s attendance percentage and prints:
“Excellent” (≥ 90), “Good” (75–89), “Satisfactory” (50–74), “Poor” (< 50).

```js
let attendance = 80;
if (attendance>=90 && attendance<100){
    console.log("Excellent")
}else if (attendance>=75){
    console.log("Good")
}else if (attendance>=50){
    console.log("Satisfactory")
}else{
    console.log("Poor")
}
```

Q9) Write a program that takes three subject marks and finds the highest mark among them using if...else if...else.

```js
let JSMarks = 95;
let CSSMarks = 68;
let figmaMarks = 89;
if (JSMarks>CSSMarks&&JSMarks>figmaMarks){
    console.log(JSMarks,"is highest among 3 in JS")
}else if (CSSMarks>JSMarks&&CSSMarks>figmaMarks){
    console.log(CSSMarks,"is highest among 3 in CSS")
}else{
    console.log(figmaMarks,"is highest among 3 in Figma")
}
```

Q10) Check a number and print one of the following:
“Positive Even”, “Positive Odd”, “Negative Even”, “Negative Odd”, or “Zero”.

```js
let num = 8;
if (num==0){
    console.log("Zero")
}else if(num>0&&num%2==0){
    console.log("Positive Even")
}else if(num>0&&num%2==1){
    console.log("Positive Odd")
}else if(num<0&&num%2==0){
    console.log("Negative Even")
}else{
    console.log("Negative Odd")
}
```
