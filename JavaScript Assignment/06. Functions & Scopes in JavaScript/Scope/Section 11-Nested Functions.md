# Section 11: Nested Functions

Q51) Predict the output:

```js
function outer() {
    var teacher = "Kartik Sir";
    function inner() {
        var student = "Jenil";
        console.log(student); // Jenil
        console.log(teacher); // Kartik Sir
    }
    inner();
}
outer();
```

Can you access `teacher` or `student` outside `outer()`? Explain.

=> No, any variable declared inside function can't be accessible outside function.

Q52) What will this code print? Explain the accessibility of each variable.

```js
function parent() {
    var a = "Parent";
    function child() {
        var b = "Child";
        function grandchild() {
            var c = "Grandchild";
            console.log(a); // Parent
            console.log(b); // Child
            console.log(c); // Grandchild
        }
        grandchild();
    }
    child();
}
parent();
```

a => Any variable declared outside a function, will work as a global scope variable for the function.
b => This variable is also declared outside the function `grandchild()` so it will be accessible inside function.
c => It is a local variable for for function.

Q53) Find the error(s):

```js
function outer() {
    var secret = "Hidden";
    function inner() {
        console.log(secret);
    }
}
inner(); // ReferenceError: inner is not defined
outer();
```

Why does the order and placement of the function call matter?

=> As we haven't called the function `inner()` just after its declaration (inside the function outer). Also inner is declared inside a function `outer()` so it will not be accessible outside it.

Q54) Predict the output:

```js
function createMessage() {
    var greeting = "Hello";
    function show() {
        console.log(greeting + " students"); // Hello students
    }
    return show;
}
var messageFunc = createMessage();
messageFunc();
```

Explain how the inner function still has access to `greeting`.

Explanation: Any variable declared outside a function, will work as a global scope variable for the function so it will be accessible inside the function.

Q55) Write a function named `studentInfo()` that:

- Declares a local variable `name`
- Declares a local variable `course`
- Contains an inner function `display()` that prints both variables
- Calls the inner function from the outer function

```js
function studentInfo(){
    var name = "Dhruv"
    var course = "CSE"
    function display(){
        console.log(name)
        console.log(course)
    }
    display()
}
studentInfo()
```
