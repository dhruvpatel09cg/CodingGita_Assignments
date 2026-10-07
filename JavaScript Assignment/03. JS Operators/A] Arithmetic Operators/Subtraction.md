# Subtraction

Q1) A bus has 80 seats, and 53 seats are occupied. Find the number of empty seats.

```js
let totalSeats = 80
let occupiedSeats = 53
let emptySeats = totalSeats - occupiedSeats
console.log(emptySeats)
```

Q2) A student has 500 marks and loses 35 marks due to incorrect answers. Find the final marks.

```js
let initialMarks = 500
let marksLost = 35
let finalMarks = initialMarks - marksLost
console.log(finalMarks)
```

Q3) A warehouse has 2,500 boxes and sends 875 boxes to a store. Find the remaining boxes.

```js
let totalBoxes = 2500
let boxesSentToStore = 875
let remainingBoxes = totalBoxes - boxesSentToStore
console.log(remainingBoxes)
```

Q4) Predict the output:

```js
let a = "10";
let b = 3;
let result = a - b;
console.log(result);
// Output: 7
```

Q5) Predict the output:

```js
let x = "20";
let y = "5";
let result = x - y;
console.log(result);
// Output: 15
```

Q6) What is the output of `100 - 37`?

Output: 63

Q7) A tank has 500 litres of water. After using 175 litres, how much water is left?

```js
let totalWater = 500
let waterUsed = 175
let waterLeft = totalWater - waterUsed
console.log(waterLeft)
```

Q8) What is the result of `"50" - 20` and `"50" - "20"`? Explain any difference.

    `"50" - 20 = 30` also `"50" - "20" = 30`:
    There is no difference between both. But the notable point is that unlike addition operator 
    JS converts string datatype to number for operating a subtraction.

Q9) A shopkeeper had 240 apples. He sold 95 in the morning and 67 in the evening. Write expressions to find how many apples are left.

```js
let totalApple = 240
let soldAtMorning = 95
let soldAtEvening = 67
let totalSell = soldAtMorning + soldAtEvening
console.log("Total apples sold:",totalSell)
let appleLeft = totalApple - totalSell
console.log("Apples left:",appelLeft)
```

Q10) Predict and explain the outputs:  

```js
console.log("100" - 50);
console.log("abc" - 10);
console.log(10 - "5" - "2");
console.log("10" - "5" - "2");
```