# Greater Than

Q1) A student’s marks are 78. The passing marks are 40. Check whether the student has scored more than the passing marks.

```js
let marks = 78
let passingMarks = 40;
console.log("Is student has scored more than passing marks:", marks > passingMarks)
```

Q2) Temperature today is 35°C and yesterday it was 28°C. Check if today is hotter.

```js
let todayTemp = 35
let yesterdayTemp = 28;
console.log("Is today is hotter:", todayTemp > yesterdayTemp)
```

Q3) Predict the output:

```js
console.log(15 > 10); // Output: true
console.log(10 > 15); // Output: false
console.log(10 > 10); // Output: false
```

Q4) Predict the output:

```js
console.log("20" > 15); // Output: true
console.log("5" > "10"); // Output: true => Compares only 1st position
console.log("abc" > 10); // Output: false => abc is NaN and give false
```

Q5) What is the result of `null > 0` and `undefined > 0`? Explain.

Output: null > 0 = false => As JS converts null in number which is 0 so 0>0 is false
Output: undefined > 0 = false => As JS converts undefined in number which is NaN and comparing anything with NaN gives false.

Q6) A shop has 120 items in stock. A customer wants to buy 85 items. Write a condition using `>` to check if stock is sufficient.

```js
let stock = 120;
let demand = 85;
console.log("Is stock sufficient:", stock > demand)
```

Q7) Predict and explain:

```js
console.log(true > false); // Output: true => JS will convert both to number so true = 1and false = 0
console.log("10" > "2"); // Output: false => JS will compare only 1st characters of both strings so 1>2
console.log(NaN > 5); // Output: false => Comparing NaN with anything will give false
```
