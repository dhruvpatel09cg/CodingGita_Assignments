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
