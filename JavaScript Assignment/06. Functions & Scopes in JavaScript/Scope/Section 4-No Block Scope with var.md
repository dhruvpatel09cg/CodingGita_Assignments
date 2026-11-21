# Section 4: No Block Scope with `"var"`

Q16) Predict the output:

```js
if (10 > 5) {
    var result = "Success";
}
console.log(result); // Success
```

Explain why `"result"` is accessible outside the `"if"` block.

Explanation: as `var` is a function scope it ignores the blocks of `if` statement so the variable `result` can be accessed outside if block.

Q17) What will be printed?

```js
var number = 1;
if (true) {
    var number = 2;
}
console.log(number); // 2
```

Why does the output differ from what you might expect if the block had its own scope?

Explanation: As `var` is a functional scope it ignores the block of `if` statement.

Q18) Predict the output:

```js
var message = "Start";
{
    var message = "End";
}
console.log(message); // End
```

Does the standalone block create a separate scope for `"var"`?

Answer: No, standalone block can't create a separate scope for var.

Q19) Find the output and explain the variable's scope:

```js
if (false) {
    var result = 100;
}
console.log(result); // undefined
```

=> Variable is in global scope

Does the condition being `"false"` prevent the `"var"` declaration from being hoisted?

Answer: No, condition being `false` doesn't prevent `var` being hoisted.

Q20) Rewrite the following code so that the variable `"secret"` cannot be accessed outside the `"if"` block. Use a variable declaration that supports block scope.

```js
if (true) {
    var secret = "Hidden";
}
console.log(secret);
```

Corrected code:

```js
if (true){
    let secret = "Hidden";
}
console.log(secret)
```

Explain why your solution works.

Explanation: As `let` is a block scope declaration it prevent the access of variable outside the block of `if` statement
