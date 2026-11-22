# 4. Updating Values

Q1) How do you update a specific value inside an existing JavaScript array?

=> Simply assign to a specific index

Q2) Given `var marks = [80, 75, 90];`, what code would you write to change the second element (`75`) to `95`?

```js
marks[1] = 95
```

Q3) After executing the update from the previous question, what will `console.log(marks);` output?

=> [80, 95, 90]

Q4) True or False: You need to use a special built-in method like `update()` to change an array element's value.

=> False

Q5) Can you update a value at an index that is currently outside the bounds of the array? What happens if you assign a value to a much higher index?

=> Yes, you can update a value at an index that is currently outside the bounds of array.

If we try to assign a value to much higher index:

```js
[ 10, 20, 30, <2 empty items>, 60 ] // Array looks like this
6 // It's length will count the empty values as well
```
