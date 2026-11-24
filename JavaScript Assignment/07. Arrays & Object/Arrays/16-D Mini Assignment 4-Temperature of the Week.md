# 16-D Mini Assignment 4: Temperature of the Week

**Given Input:**

```javascript
const temperatures = [
    ["Monday", 32],
    ["Tuesday", 35],
    ["Wednesday", 30],
    ["Thursday", 28],
    ["Friday", 33],
    ["Saturday", 36],
    ["Sunday", 31]
];
```

**Tasks:**

1. Print the temperature of each day.
2. Find and print:
   - Highest temperature + day
   - Lowest temperature + day
   - Average temperature of the week
3. Print a warning if any day has temperature ≥ 35:  
   `Heat Alert on <Day>`

```js
const temperatures = [
    ["Monday", 32],
    ["Tuesday", 35],
    ["Wednesday", 30],
    ["Thursday", 28],
    ["Friday", 33],
    ["Saturday", 36],
    ["Sunday", 31]
];
let highest = -Infinity;
let lowest = Infinity;
let coldDay;
let hotDay;
let total = 0;
for (let i=0; i<temperatures.length; i++){
    console.log(`Temperature on ${temperatures[i][0]} was ${temperatures[i][1]} degree.`)
    if (temperatures[i][1]>highest){
        highest=temperatures[i][1]
        hotDay=temperatures[i][0]
    }
    if (temperatures[i][1]<lowest){
        lowest=temperatures[i][1]
        coldDay=temperatures[i][0]
    }
    total+=temperatures[i][1]
    if (temperatures[i][1]>35){
        console.log(`Heat alert on ${temperatures[i][0]}`)
    }
}
console.log("======================================================")
console.log(`Hottest Day: ${hotDay}, Temperature: ${highest}`)
console.log(`Coldest Day: ${coldDay}, Temperature: ${lowest}`)
console.log("======================================================")
let avg = total/temperatures.length
console.log(`Average temperature: ${avg} degree`)
```
