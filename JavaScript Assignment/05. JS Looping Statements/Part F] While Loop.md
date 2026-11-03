# Part F] While Loop

Q1) Write a while loop to print numbers from 1 to 10.

```js
let i = 1;
while (i<=10){
    console.log(i)
    i++
}
```

Q2) Write a while loop to calculate the sum of the first 10 natural numbers.

```js
let i = 1;
let sum = 0
while (i<=10){
    sum+=i
    i++
}
console.log(sum)
```

Q3) Write a while loop to print the multiplication table of a given number from 1 to 10.

```js
let i = 1;
const num = 5
while (i<=10){
    console.log(num,"x",i,"=",num*i)
    i++
}
```

Q4) Write a while loop to count the total number of digits in a given positive integer.

```js
let num = 58321
let count = 0
while (num>0){
    count+=1
    num=Math.floor(num/10)
}
console.log(count)
```

Q5) Write a while loop to reverse the digits of a given positive integer.

```js
let num = 58321
let reverse = 0
while (num>0){
    digit=num%10
    reverse=reverse*10+digit
    num=Math.floor(num/10)
}
console.log(reverse)
```

Q6) Write a while loop to calculate the sum of all digits of a given number.

```js
let num = 58321
let sum = 0
while (num>0){
    digit=num%10
    sum+=digit
    num=Math.floor(num/10)
}
console.log(sum)
```

Q7) Write a while loop to print all numbers between 1 and 100 that are divisible by both 3 and 5 but not by 7.

```js
let i = 1;
while (i<=100){
    if (i%3==0 && i%5==0 && i%7!=0){
        console.log(i)
    }
    i++
}
```

Q8) Write a while loop to calculate the factorial of a given non-negative integer.

```js
let fact = 1
let i = 1
let num = 6
while (i<=num){
    fact*=i
    i++
}
console.log("Factorial:",fact)
```

Q9) Write a while loop to check whether a given number is a palindrome without converting it into a string.

```js
let num = 12321
let original = num
let i = 1
let reverse = 0
while (i<=num){
    let digit = num%10
    reverse = reverse*10+digit
    num = Math.floor(num/10)
}
if (reverse===original){
    console.log("A Palindrome number")
}else{
    console.log("Not a Palindrome")
}
```

Q10) Write a while loop to convert a positive decimal integer into its binary representation without using built-in methods such as toString(2).

```js
let num = 154
let binary = ""
let i = 1
while (i<=num){
    digit = num%2
    binary=digit+binary
    num = Math.floor(num/2)
}
console.log(binary)
```
