# Division

Q1) A teacher distributes 144 pencils equally among 12 students. Find the number of pencils each student receives.

```js
let totalPencils = 144
let totalStudents = 12
let pencilsPerStudents = totalPencils / totalStudents
console.log("Pencils each student got:",pencilsPerStudents)
```

Q2) A train travels 360 kilometres in 6 hours. Find its average distance travelled per hour.

```js
let totalDist = 360
let timeTaken = 6
let distPerHour = totalDist / timeTaken
console.log("Distance covered per hour:",distPerHour)
```

Q3) A company distributes ₹72,000 equally among 9 departments. Find the amount received by each department.

```js
let totalMoney = 72000
let totalDepartments = 9
let moneyPerDepartment = totalMoney / totalDepartments
console.log("Money each department will get:",moneyPerDepartment)
```

Q4) Predict the output:

```js
let a = "20";
let b = 4;
let result = a / b;
console.log(result);
// Output: 5
```

Q5) Predict the output:

```js
let x = "100";
let y = "5";
let result = x / y;
console.log(result);
// Output: 20
```

Q6) What is the output of `144 / 12`?

Output: 12

Q7) 360 students are to be divided equally into 9 classrooms. How many students per classroom?

```js
let totalStudents = 360
let totalClassrooms = 9
let studentsPerClass = totalStudents / totalClassrooms
console.log("Students per Classroom:",studentsPerClass)
```

Q8) What is the result of `"100" / 4` and `"100" / "4"`?

Result: 25 => Same result for both

Q9) A total bill of ₹2400 is to be shared equally among 6 friends. Write the expression and find each person’s share.

```js
let totalBillAmount = 2400
let numberOfFriends = 6
let share = totalBillAmount / numberOfFriends
console.log("Each friend's share:",share)
```

Q10) Predict and explain the outputs:

```js
console.log(10 / 0); // Output: Infinity => JS follows simple maths rules while executing division
operator
console.log(-10 / 0); // Output: -Infinity => JS follows simple maths rules while executing division
operator
console.log(0 / 0); // Output: NaN => As 0/0 is not defined in maths so JS gives NaN
console.log("20" / "4" / 2); // Output: 2.5 => JS converts string datatype into number while executing
division operator
console.log("abc" / 5); // Output: NaN => As abc can't be converted to number datatype so JS will give
output with type number and value Not a Number
```
