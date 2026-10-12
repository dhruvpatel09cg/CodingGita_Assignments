# Part b

Q6) Start with `x = 5`.

- Create `y = x++`  
- Print both `x` and `y`.

Explain why the values are different.

```js
let x = 5
let y = x++
console.log(x, y)
```

Explanation: As we used PostFix Increment Operator here so JS will first assign the old value of x to y and then updates it, so both values are different.

Q7) Start with `a = 5`.  

- Create `b = ++a`  
- Print both `a` and `b`.  

Explain the difference from the previous question

```js
let a = 5
let b = ++a;
console.log(a, b);
```

Explanation: Here we used PreFix Increment Operator so JS will first update the value of x and then assigns the new value to y variable.

Q8) Start with `lives = 3`.

- Use post-decrement (`lives--`) and store the result in `previousLives`.  
- Print both variables.

```js
let lives = 3;
let previousLives = lives--;
console.log(lives, previousLives)
```

Q9) Start with `attempts = 0`.

- Use pre-increment (`++attempts`) and store the result in `currentAttempts`.  
- Print both variables.

```js
let attempts = 0;
let currentAttempts = ++attempts
console.log(attempts, currentAttempts)
```

Q10) Start with `points = 100`.

- Increase it using `++`  
- Then decrease it using `--`  
- Print the final value.

```js
let points = 100;
points++;
points--;
console.log(points);
```
