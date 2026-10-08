# Addition

Q1) A school collected ₹15,000 from one class and ₹12,500 from another class. Find the total collection.

```js
let class1Collection = 15000
let class2Collection = 12500
let totalCollection = class1Collection + class2Collection
console.log(totalCollection)
```

Q2) A person reads 18 pages in the morning and 25 pages in the evening. Find the total pages read.

```js
let pagesReadMorning = 18
let pagesReadEvening = 25
let totalPagesRead = pagesReadMorning + pagesReadEvening
console.log(totalPagesRead)
```

Q3) A shop sold 125 items on Monday and 178 items on Tuesday. Find the total items sold.

```js
let mondaySell = 125
let tuesdaySell = 178
let totalSell = mondaySell + tuesdaySell
console.log(totalSell)
```

Q4) Predict the output:

```js
let a = "10";
let b = 5;
let result = a + b;
console.log(result);
// Output: 105
```

Q5) Predict the output:

```js
let x = 5;
let y = "3";
let result = x + y;
console.log(result);
// Output: 53
```

Q6) What is the output of `15 + 27`?

`42`

Q7) Calculate the total price if a book costs ₹350 and a pen costs ₹45.

```js
let penPrice = 45
let bookPrice = 350
let totalPrice = penPrice + bookPrice
console.log(totalPrice)
```

Q8) What is the result of `"25" + 10` and why?

Output will be `2510` as JS will convert datatype of number into string if we try to add them.

Q9) A person has ₹2000 in their wallet. They buy items worth ₹750 and ₹320. Write an expression using + to find the total spent, then calculate the remaining balance.

```js
let priceItem1 = 750
let priceItem2 = 320
let totalSpent = priceItem1 + priceItem2
console.log(totalSpent)
let moneyInWallet = 2000
let remainingBalance = moneyInWallet - totalSpent
console.log(remainingBalance)
```

Q10) Predict the outputs and explain:

```js
console.log(5 + "5" + 5); // Output: 555 => Output is 555 as JS converts number datatype to string while
adding them together.
console.log(5 + 5 + "5"); // Output: 105 => Output is 105 as JS first adds 5 with 5 and makes it 10 and
then converts it to string datatype to add it in another string.
console.log("5" + 5 + 5); // Output: 555 => Output is 555 as JS converts number datatype to string while
adding them together.
```
