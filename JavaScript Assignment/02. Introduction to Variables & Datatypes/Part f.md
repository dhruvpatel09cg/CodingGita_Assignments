**5. Symbol Uniqueness**  
Create two Symbols with the same description (`'id'`).  
Compare them using `===` and print the result.  
Then use both Symbols as keys in an object and retrieve the values.  
Explain why the comparison returns `false`.

```js
let id1 = Symbol("id")
let id2 = Symbol("id")

console.log(id1 === id2) // false as Symbol provides a unique id to its description value.

let ids = {
    [id1]: "DPATEL"
    [id2]: 54321
}

console.log(ids[id1])
console.log(ids[id2])
```

**6. BigInt Precision**  
Create a regular `number` with the value `9007199254740991` (Number.MAX_SAFE_INTEGER).  
Add `1`, `2`, and `3` to it and print the results.  
Now create the same value as a `BigInt` and perform the same additions.  
Print the results and explain the difference.

```js
let num = 9007199254740991

console.log(typeof(num))

console.log(num+ 1)
console.log(num+ 2) // Output only adds 1 (As it is out of max safe number limit)
console.log(num+ 3)

let big = 9007199254740991n

console.log(typeof(big))

console.log(big + 1n)
console.log(big + 2n) // This adds the numbers precisely
console.log(big + 3n)
```

**7. Choose the Correct Type**  
For each description below, write the most appropriate primitive data type and give an example declaration:  

```js
// A unique identifier that is never equal to another value with the same description ==> Symbol
let id = Symbol('id')
let ids = {
    [id]: 123
}

console.log(ids[id])

// A very large integer that must keep exact precision
let big = 12345678904737357989n
console.log(big)

// A variable that has been declared but not yet given a value 
var x;
console.log(x)

// An intentional empty value
let empt = null
console.log(empt)
```