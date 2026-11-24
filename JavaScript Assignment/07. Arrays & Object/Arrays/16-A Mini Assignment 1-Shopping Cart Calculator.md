# 16-A Mini Assignment 1: Shopping Cart Calculator

**Given Input:**

```javascript
const cart = [
    ["Laptop", 45000, 1],
    ["Mouse", 800, 2],
    ["Keyboard", 1500, 1],
    ["Headphones", 2500, 1]
];
```

*(Format: [Product Name, Price, Quantity])*

**Tasks:**

1. Loop through the cart.
2. For each item, calculate the total price (`Price × Quantity`).
3. Print in this format:

   ```md
   Product: Laptop
   Price: 45000
   Quantity: 1
   Item Total: 45000
   ```

4. At the end, print the **Grand Total** of the entire cart.
5. **Bonus:** Apply 10% discount if Grand Total > 50000 and show the final payable amount.

```js
const cart = [
    ["Laptop", 45000, 1],
    ["Mouse", 800, 2],
    ["Keyboard", 1500, 1],
    ["Headphones", 2500, 1]
];
let total = 0;
for (let i=0; i<cart.length; i++){
    console.log(`Product: ${cart[i][0]}`)
    console.log(`Price: ${cart[i][1]}`)
    console.log(`Quantity: ${cart[i][2]}`)
    console.log(`Item Total: ${cart[i][1]*cart[i][2]}`)
    console.log("============================")
    total += cart[i][1]*cart[i][2]
}
console.log(`Grand Total: ${total}`)
console.log("============================")
if(total>50000){
    console.log("10% Discount will be applied")
    console.log("============================")
    let discountedAmount = (total*10)/100
    let payable = total-discountedAmount
    console.log(`You have to pay: ₹${payable}`)
}
```
