Q20. Predict the output of the following code and explain why:

    let value = 25;
    console.log(typeof value);
    value = "JavaScript";
    console.log(typeof value);
    value = false;
    console.log(typeof value);

  Ans: 
  
Output:
    
      number
      string
      Boolean

  Reason:

    As JS is a Dynamically typed language it changes type of variable according to the value assigned in it.
      
Q21. Write a simple HTML + JavaScript program that displays an alert box with the message "Welcome to JavaScript!" when a button is clicked.

```html
<button id="msg">Click Me!</button>

<script>
    let msg = document.getElementById("msg")

    msg.addEventListener("click", function() {
        alert("Welcome to JavaScript!")
    })
</script>
```

Q22. Write JavaScript code to demonstrate event-driven programming.
When a user clicks a button with id "myBtn", the text of a paragraph with id "demo" should change to "Button was clicked!".

```html
<p id="demo">Click The Button</p>

<button id="myBtn">Click Me</button>

<script>

document.getElementById("muBtn").addEventListener("click", function() {
    document.getElementById("demo").textContent = "Button was Clicked!"
})
</script>
```
