# 16-B Mini Assignment 2: Classroom Attendance Tracker

**Given Input:**

```javascript
const attendance = [
    ["Jenil", ["P", "P", "A", "P", "P"]],
    ["Mahir", ["P", "A", "P", "P", "A"]],
    ["Yashvi", ["P", "P", "P", "P", "P"]],
    ["Arjun", ["A", "A", "P", "P", "A"]]
];
```

`(P = Present, A = Absent)`

**Tasks:**

1. Loop through each student.
2. Count total Presents and Absents.
3. Calculate attendance percentage.
4. Print in this format:

   ```md
   Name: Jenil
   Present: 4
   Absent: 1
   Attendance: 80%
   Status: Good
   ```

5. Status rule:
   - ≥ 75% → `Good`
   - < 75% → `Low Attendance`
6. **Bonus:** Print the name of the student with highest attendance.

```js
const attendance = [
    ["Jenil", ["P", "P", "A", "P", "P"]],
    ["Mahir", ["P", "A", "P", "P", "A"]],
    ["Yashvi", ["P", "P", "P", "P", "P"]],
    ["Arjun", ["A", "A", "P", "P", "A"]]
];
let highest=0
let student;
for (let i=0; i<attendance.length; i++){
    let total=0;
    for (let j=0; j<attendance[i][1].length; j++){
        if (attendance[i][1][j]=="P"){
            total++
        }
    }
    console.log(`Name: ${attendance[i][0]}`)
    console.log(`Present: ${total}`)
    console.log(`Absent: ${5-total}`)
    console.log(`Attendance: ${(total*100)/5}%`)
    if ((total*100)/5>highest){
        highest = (total*100)/5
        student = attendance[i][0]
    }
    if ((total*100)/5>=75){
        console.log(`Status: Good`)
    }else{
        console.log(`Status: Low Attendance`)
    }
    console.log("=====================================")
}
console.log(`${student} has highest attendance`)
```
