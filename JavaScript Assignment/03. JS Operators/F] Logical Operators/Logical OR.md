# Logical OR

Q1) A user can login with either a correct password (`passwordCorrect = true`) or a valid OTP (`otpValid = false`). Check if login is allowed using `||`.

```js
let passwordCorrect = true;
let otpValid = false;
let isLoginAllowed = passwordCorrect || otpValid
console.log("Is user allowed to Login?",isLoginAllowed)
```

Q2) A discount applies if the user is a member (`isMember = false`) or has a coupon (`hasCoupon = true`). Check using `||`.

```js
let isMember = false;
let hasCoupon = true;
let getDiscount = isMember || hasCoupon;
console.log("Will customer get discount?",getDiscount)
```

Q3) Entry is allowed if age is above `18` (`age = 16`) **or** height is above `150` cm (`height = 155`). Check using `||`.

```js
let age = 16;
let height = 155;
let isEntryAllowed = age > 18 || height > 150;
console.log("Is allowed to enter?",isEntryAllowed)
```

Q4) A form is valid if either email is given (`emailGiven = true`) or phone is given (`phoneGiven = false`). Check using `||`.

```js
let emailGiven = true;
let phoneGiven = false;
let valid = emailGiven || phoneGiven;
console.log("Is the form valid?",valid)
```

Q5) A game level opens if score is above `1000` (`score = 900`) **or** time bonus is collected (`timeBonus = true`). Check using `||`.

```js
let score = 900;
let timeBonus = true;
let isLevelOpen = score>1000 || timeBonus
console.log("Is the level Open?",isLevelOpen)
```

## Additional Question

Q6) Predict the output:

```js
let a = 0;
let b = false;
let c = "";
let d = null;
let e = 42;
let result = a || b || c || d || e;
console.log(result);
// Output: 42
```

Q7) Predict the output:

```js
let x = "Hello" || 0;
let y = 0 || "Hi";
console.log(x, y);
// Output: Hello Hi
```

Q8) Predict the output:

```js
let a = 10;
let b = 20;
let result = (a < 5) || (b > 15);
console.log(result);
// Output: true
```

Q9) Predict the output:

```js
let val = 5;
let condition = val || (val = 0);
console.log(condition);
console.log(val);
// Output: 5
// Output: 5 => As OR operator got the truthy value at 5 so it will directly go to next line and don't reach val = 0 expression so it left it's value 5 as it is.
```

Q10) Predict the output:

```js
let x = "" || 0 || false || null || undefined || "OK";
console.log(x);
// Output: OK
```
