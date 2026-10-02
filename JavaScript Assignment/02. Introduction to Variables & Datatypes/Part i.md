**5. Valid vs Invalid Variable Names**  
Identify which of the following variable names are **valid** and which are **invalid**. For invalid ones, explain why.

```javascript
let userName;
let 2ndPlace; // This is invalid as variable name should not start with a number.
let _privateData;
let $price;
let my-age; // This is also invalid as variable should not contain any other symbol except _ and $
let function; // This is not valid as function is a keyword of js
let totalCount;
let const; // This is not valid as const is a keyword of js
```

**6. Apply Best Practices**  
Rewrite the following poorly written code using best practices (`const`/`let`, meaningful names, camelCase, UPPERCASE for constants):

```javascript
const length = 10;
const width = 5;
const areaRectangle = x * y;
const MAX_VALUE = 100;
```

**7. Declaration & Assignment**  
Write code that demonstrates:
- Declaring a variable without assigning a value, then assigning a value later  
- Declaring and assigning a value in one step  
- Creating a constant that cannot be changed  

Print all variables.

```js
let age;
age = 19
let isHere = false
const NAME = "Fenil"

console.log(age)
console.log(isHere)
console.log(NAME)
```