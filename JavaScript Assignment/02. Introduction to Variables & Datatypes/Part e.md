**1. Classify the Types**  
Declare one variable of each of the following types and print both the value and its type using `typeof`:
- A whole number  
- A decimal number  
- A piece of text  
- A true/false value 
```js
let num = 10
console.log(num)
console.log(typeof(num))

let decimal = 48.53
console.log(decimal)
console.log(typeof(decimal))

let txt = "ckwk"
console.log(txt)
console.log(typeof(txt))

let me = true
console.log(me)
console.log(typeof(me))
```

**2. Undefined vs Null**  
Declare two variables:
- `a` using `let` without assigning any value  
- `b` and intentionally assign `null` to it  

Print both variables and their `typeof` results. Explain the difference between `undefined` and `null`.

```js
let a;
console.log(a)
console.log(typeof(a)) // type is undefined because we unintentionally left it empty

let b = null
console.log(b)
console.log(typeof(b)) // type is object as we intentionally made it null
```

**3. Number Special Values**  
Create variables for the following and print each value along with its type:
- Positive Infinity  
- Negative Infinity  
- Not-a-Number (`NaN`)  
- A large number written with scientific notation (e.g., `2.5e3`)  
- A number written with underscores for readability (e.g., `1_000_000`)

```js
let positiveInfinity = Infinity;
let negativeInfinity = -Infinity;
let notANumber = NaN;
let scientificNumber = 2.5e3;
let readableNumber = 1_000_000;

console.log(positiveInfinity);
console.log(negativeInfinity);
console.log(notANumber);
console.log(scientificNumber);
console.log(readableNumber);

console.log(typeof positiveInfinity);
console.log(typeof negativeInfinity);
console.log(typeof notANumber);
console.log(typeof scientificNumber);
console.log(typeof readableNumber);
```

**4. String Styles**  
Create three string variables using:
- Single quotes  
- Double quotes  
- Template literals (backticks) that include another variable  

Print all three strings.

```js
let str1 = "Hello"
let str2 = 'Code Master'
let str3 = `${str1} world!`

console.log(str1)
console.log(str2)
console.log(str3)
```