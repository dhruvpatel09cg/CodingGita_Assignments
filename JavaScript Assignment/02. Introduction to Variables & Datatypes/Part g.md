**8. Predict the Output**  
Without running the code, predict what each `console.log` will print (value + type). Explain your reasoning.

```javascript
let a;
let b = null;
let c = 42;
let d = "Hello";
let e = true;
let f = Symbol("key");
let g = 123n;

console.log(typeof a, a); //undefined, undefined=> unintentionally empty
console.log(typeof b, b); //object, null=> Intentionally empty(give object due to js quirk)
console.log(typeof c, c); //number, 42=> Normal number
console.log(typeof d, d); //string, Hello=> String
console.log(typeof e, e); //boolean, true=> boolean type only for true and false
console.log(typeof f, f); //symbol, Symbol(key)=> symbol used to create unique ids
console.log(typeof g, g); //bigint, 123n=> bigint used to maintain precision while operating large numbers
```

**9. Fix the Code**  
The following program has mistakes related to primitive types. Fix it so that it runs correctly and prints meaningful values.

```javascript
let num = 10;
let text = "Hello";//"" were not used for string
let flag = true;//for boolean value all letters should be in lowercase
let empty;
let nothing = null;//all characters should be in lowercase to keep a variable intentionally empty
let unique = Symbol("id");// S should be capital in Symbol to generate unique id using it
let big = 9007199254740991n;//for bigint the number should end with n

console.log(num, text, flag, empty, nothing, unique, big);
```

**10. Primitive vs Non-Primitive**  
Answer the following questions in your own words and give one example for each:

a) What is the main difference between Primitive and Non-Primitive data types?  
b) Why are Numbers, Strings, Booleans, Undefined, Null, Symbol, and BigInt called Primitive?  
c) Give one example of a Non-Primitive data type and explain why it is considered Non-Primitive.

    a)
    Primitive data type can only hold a single value.
    Non-Primitive data type can hold multiple values.

    b)
    As they all are basic data types and can hold only a single value that's why they are
    called Primitive.

    c)
    object is one of the Non-Primitive data types.
    It is considered as Non-Primitive as it can hold multiple values as variable and it is a
    complex datatype.
    
