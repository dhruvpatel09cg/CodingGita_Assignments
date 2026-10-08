# Modulus

Q1) A teacher has 53 students and forms groups of 5. Find the number of students left over.

```js
let totalStudents = 53
let strengthOfGroup = 5
let studentsLeft = totalStudents % strengthOfGroup
console.log("Students left:",studentsLeft)
```

Q2) A shop has 128 candies and packs 10 candies in each box. Find the number of candies left unpacked.

```js
let totalCandies = 128
let candiesPerBox = 10
let candiesLeft = totalCandies % candiesPerBox
console.log("Candies left:",candiesLeft)
```

Q3) A factory produces 237 toys and packs them in boxes of 6. Find how many toys are left after packing full boxes.

```js
let totalToys = 237
let toysPerBox = 6
let toysLeft = totalToys % toysPerBox
console.log("Toys left unpacked:",toysLeft)
```

Q4) A bus can carry 40 passengers. If 185 people are waiting, find how many people will be left after filling as many full buses as possible.

```js
let busCapacity = 40
let totalPeople = 185
let peopleLeft = totalPeople % busCapacity
console.log("People left behind:",peopleLeft)
```

Q5) Predict the output:

```js
let a = 10;
let b = 0;
let result = a % b;
console.log(result);
// Output: NaN
```

Q6) What is the output of `29 % 5`?

Output: 4

Q7) There are 23 chocolates to be packed in boxes of 4. How many chocolates will be left over?

```js
let totalChocolates = 23
let chocolatePerBox = 4
let chocolateLeft = totalChocolates % chocolatePerBox
console.log(chocolateLeft)
```

Q8) What is the result of `0 % 7` and `15 % 0`? Explain.

Output: 0 % 7 = 0 : JS uses simple math here as 0 divided by any integer gives 0.
Output: 15 % 0 = NaN : As in maths it is Not Defined so JS give Not a Number.

Q9) A number of pages (47) needs to be printed on sheets that hold 6 pages each. How many full sheets are needed and how many pages will be left over? Write expressions using `%` and `/`.

```js
let totalPages = 47
let pagesPerSheet = 6
let fullSheetsNeeded = Math.floor(47/6)
let pagesLeft = 47 % 6
console.log(fullSheetsNeeded)
console.log(pagesLeft)
```

Q10) Predict and explain the outputs (especially the signs):

```js
console.log(17 % 5); // Output: 2 => Gives remainder when 17 divided by 5
console.log(-17 % 5); // Output: -2 => Gives remainder when -17 divided by 5 as numerator is negative output is also negative
console.log(17 % -5); // Output: 2 => Gives remainder when 17 divided by -5 output will be positive as numerator is positive
console.log(-17 % -5); // Output: -2 => Gives remainder when -17 divided by -5 as numerator is negative output will also be negative
console.log(10 % 0); // Output: NaN => As in math 0 in divisor gives Not Defined
```

Notable thing is that in JS Output of modulus depends only on sign of dividend(numerator).
