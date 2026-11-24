# 16-C Mini Assignment 3: Movie Rating Analyzer

**Given Input:**

```javascript
const movies = [
    ["Inception", [9, 8, 9, 10, 8]],
    ["Avatar", [7, 8, 7, 6, 8]],
    ["Interstellar", [10, 9, 9, 10, 9]],
    ["Joker", [8, 7, 8, 9, 8]]
];
```

**Tasks:**

1. For each movie, calculate the average rating.
2. Print in this format:

   ```md
   Movie: Inception
   Ratings: 9 8 9 10 8
   Average Rating: 8.8
   Verdict: Excellent
   ```

3. Verdict rules:
   - Average ≥ 9 → `Excellent`
   - Average ≥ 7 and < 9 → `Good`
   - Average < 7 → `Average`
4. **Bonus:** Find and print the movie with the highest average rating.

```js
const movies = [
    ["Inception", [9, 8, 9, 10, 8]],
    ["Avatar", [7, 8, 7, 6, 8]],
    ["Interstellar", [10, 9, 9, 10, 9]],
    ["Joker", [8, 7, 8, 9, 8]]
];
let highest = 0;
let movie;
for (let i=0; i<movies.length; i++){
    let ratings=0
    let bag = ""
    for (let j=0; j<movies[i][1].length; j++){
        ratings+=movies[i][1][j]
        bag+=movies[i][1][j]+" "
    }
    let avgRatings = ratings/movies[i][1].length
    console.log(`Movie: ${movies[i][0]}`)
    console.log(`Ratings: ${bag}`)
    console.log(`Average Rating: ${avgRatings}`)
    if (avgRatings>=9){
        console.log(`Verdict: Excellent`)
    }else if(avgRatings>=7){
        console.log(`Verdict: Good`)
    }else{
        console.log(`Verdict: Average`)
    }
    console.log("=====================================")
    if (avgRatings>highest){
        highest=avgRatings
        movie = movies[i][0]
    }
}
console.log(`${movie} highest average rating.`)
```
