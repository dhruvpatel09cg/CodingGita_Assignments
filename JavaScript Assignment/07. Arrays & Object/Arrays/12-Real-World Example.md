# 12. Real-World Example

```js
const marks = [
    [85, 90, 92], // Jenil
    [70, 75, 80], // Arjun
    [88, 82, 89]  // Krishna
];

for (let i = 0; i < marks.length; i++) {
    const studentMarks = marks[i];
    const total = studentMarks[0] + studentMarks[1] + studentMarks[2];
    const avg = total / 3;
    console.log("Student " + (i + 1) + " average: " + avg);
}
```

Q1) In the given marks example, what does `marks[i]` represent inside the loop?

=> `marks[i]` here represents element(array) at `i` index of the array `marks`

Q2) Why do we use `marks.length` in the outer loop instead of hard-coding the number 3?

=> `marks.length` is more useful when there are many elements in an array and you can't manually count the number.

Q3) What will happen if one student has only 2 subject marks instead of 3?

=> JS will give output `NaN` as the third index will become `undefined` and `number` added to `undefined` will give `NaN` and `NaN` divided by `number` will also give `NaN`
