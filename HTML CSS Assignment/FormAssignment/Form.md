## Answers:
---
```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Assignment</title>
</head>
<body>
    <h1 align="center">Form Assignment</h1>
    <h3>Q1</h3>
    <form action="../submit.php" method="post" autocomplete="on">
        <label for="name">Name:</label>
        <input type="text" name="Name" id="name" placeholder="Full name">
        <button type="submit">Submit</button>
    </form>

    <h3>Q2</h3>
    <form action="../submit.php" method="get">
        <input type="search" name="search" placeholder="Search">
        <button type="submit">Submit</button>
    </form>

    <h3>Q3</h3>
    <form action="../submit.php" method="post" novalidate>
        <label for="email">Email:</label>
        <input type="email" name="Email" id="email">
        <button type="submit">Submit</button>
    </form>

    <h3>Q4</h3>
    <form action="../submit.php" enctype="application/x-www-form-urlencoded">
        <!--application/x-www-form-urlencoded is the default form encoding, so you normally don't need to specify enctype. It encodes the form data as key-value pairs-->
        <label for="name">Name:</label>
        <input type="text" name="Name" id="name" placeholder="Your Name">
        <label for="email">Email:</label>
        <input type="email" name="Email" id="email" placeholder="Email ID">
        <button type="submit">Submit</button>
    </form>

    <h3>Q5</h3>
    <form enctype="multipart/form-data" action="../submit.php" method="post">
        <label for="photo">Your Photo:</label>
        <input type="file" name="Photo" id="photo">
        <button type="submit">Submit</button>
    </form>

    <h3>Q6</h3>
    <form action="../submit.php" method="post" enctype="text/plain">
        <label for="first">First Name:</label>
        <input type="text" name="First Name" id="first" placeholder="Enter Your First Name">
        <label for="sur">Surname:</label>
        <input type="text" name="Surname" id="sur" placeholder="Enter Your Surname">
        <button type="submit">Submit</button>
    </form>

    <h3>Q7</h3>
    <form action="../submit.php" name="userForm" target="_blank">
        <input type="color" name="Colour" id="color">
        <button type="submit">Submit</button>
    </form>

    <h3>Q8</h3>
    <form action="../submit.php">
        <label for="email">Email:</label>
        <input type="email" id="email" placeholder="Email ID">
        <button type="submit">Submit</button>
    </form>

    <h3>Q9</h3>
    <form action="../submit.php">
        <label for="gender">Gender:</label>
        <input type="radio" name="gender" id="male" value="Male">Male
        <input type="radio" name="gender" id="female"
        value="Female">Female
        <input type="radio" name="gender" id="other" value="Other">Other
        <button type="submit">Submit</button>
    </form>

    <h3>Q10</h3>
    <form action="../submit.php">
        <label for="hobbies">Hobbies:</label>
        <input type="checkbox" name="hobbies" id="reading" value="Reading">
        <label for="reading">Reading</label>
        <input type="checkbox" name="hobbies" id="cricket" value="Cricket" checked>
        <label for="cricket">Cricket</label>
        <input type="checkbox" name="hobbies" id="horse" value="Horse Riding">
        <label for="horse">Horse Riding</label>
        <button type="submit">Submit</button>
    </form>

    <h3>Q11</h3>
    <form action="../submit.php">
        <select name="cars" id="brand">
            <option value="Rolls-Royce">Rolls-Royce</option>
            <option value="Pagani">Pagani</option>
            <option value="Bently">Bently</option>
        </select>
    </form>

    <h3>Q12</h3>
    <form action="../submit.php">
        <select multiple name="sports" size="3">
            <option value="">Cricket</option>
            <option value="">Horse Riding</option>
            <option value="">Archery</option>
            <option value="">Shooting</option>
            <option value="">Basketball</option>
        </select>
    </form>

    <h3>Q13</h3>
    <form action="../submit.php">
        <select name="fruits" id="">
            <optgroup label="Berries"></optgroup>
            <option value="">Blueberries</option>
            <option value="">Strawberries</option>
            <optgroup label="Tropical Fruits"></optgroup>
            <option value="">Mango</option>
            <option value="">Banana</option>
        </select>
    </form>

    <h3>Q14</h3>
    <textarea name="comment" id="" cols="50" rows="4" placeholder="Leave comment"></textarea>

    <h3>Q15</h3>
    <form action="../submit.php">
        <button type="button">Button</button>
        <button type="reset">Reset</button>
        <button type="submit">Submit</button>
    </form>

    <h3>Q16</h3>
    <form action="../submit.php">
        <fieldset>
            <legend>Personal Information</legend>
            <label for="name">Name:</label>
            <input type="text" name="name" id="name" placeholder="Your Name">
            <br>
            <label for="age">Age:</label>
            <input type="number" name="age" id="age" placeholder="Your Age">
        </fieldset>
    </form>

    <h3>Q17</h3>
    <form>
        <fieldset disabled>
            <legend>User Information</legend>
            <label for="name">Username:</label>
            <input type="text" name="name" id="name" placeholder="Username">
            <br>
            <label for="pass">Password:</label>
            <input type="password" name="pass" id="pass" placeholder="Password">
        </fieldset>
    </form>

    <h3>Q18</h3>
    <form action="../submit.php">
        <input list="browsers">
        <datalist id="browsers">
            <option value="Chrome"></option>
            <option value="Duck Duck Go"></option>
            <option value="Firefox"></option>
        </datalist>
    </form>

    <h3>Q19</h3>
    <form action="../submit.php">
        <label for="pass">Password:</label>
        <input type="password" name="Password" id="pass" minlength="8" required>
        <button type="submit">Submit</button>
    </form>

    <h3>Q20</h3>
    <form action="../submit.php">
        <label for="email">Email:</label>
        <input type="email" multiple name="Email ID" id="email" placeholder="Seperate by comma --> ,">
    </form>

    <h3>Q21</h3>
    <form>
        <input type="date" name="Date" id="date" min="2023-01-01" max="2023-12-31">
    </form>

    <h3>Q22</h3>
    <form action="../submit.php">
        <label for="quantity">Quantity:</label>
        <input type="number" name="quantity" id="quantity" min="1" max="10" step="1">
    </form>

    <h3>Q23</h3>
    <form action="../submit.php">
        <label for="vol">Volume</label>
        <input type="range" name="Volume" id="vol" min="0" max="100" value="15">
    </form>

    <h3>Q24</h3>
    <form action="../submit.php" enctype="multipart/form-data">
        <input type="file" name="" id="" accept=".pdf,.docx" required>
    </form>

    <h3>Q25</h3>
    <form action="../submit.php">
        <input type="hidden" name="Token" value="2ED32QS">
        <label for="name">Name:</label>
        <input type="text" name="user" id="">
    </form>

    <h3>Q26</h3>
    <form action="../submit.php">
        <label for="color">Favorite Color</label>
        <input type="color" value="#ff0000">
    </form>

    <h3>Q27</h3>
    <form action="../submit.php">
        <label for="phone">Phone no.:</label>
        <input type="tel" pattern="[0-9]{5}-[0-9]{5}" placeholder="XXXXX-XXXXX">
        <button type="submit">Submit</button>
    </form>

    <h3>Q28</h3>
    <form action="../submit.php">
        <label for="link">Link:</label>
        <input type="url" name="link" id="link" required placeholder="https://">
    </form>

    <h3>Q29</h3>
    <form action="../submit.php">
        <input type="search" value="" autofocus placeholder="Search here">
    </form>

    <h3>Q30</h3>
    <form action="../submit.php" id="form">
        <input type="date" name="">
    </form>
    <label for="email">Email:</label>
    <input type="email" name="" id="email" form="form" placeholder="Email">

    <h3>Q31</h3>
    <form action="../submit.php">
        <button type="submit">Submit</button>
        <button type="submit" formaction="../2nd.php">Submit 2</button>
    </form>

    <h3>Q32</h3>
    <form action="../submit.php" method="post">
        <button type="submit">Submit</button>
        <button type="submit" formmethod="get">Submit 2</button>
    </form>

    <h3>Q33</h3>
    <form action="../submit.php">
        <label for="email">Email:</label>
        <input type="email" name="" id="email" required placeholder="Email ID">
        <label for="dob">D.O.B</label>
        <input type="date" name="" id="dob" required>
        <button type="submit">Submit</button>
        <button type="submit" formnovalidate>Save as Draft</button>
    </form>

    <h3>Q34</h3>
    <form action="/preview">
        <label for="">Title:</label>
        <input type="text" name="" id="" placeholder="Add Title">
        <textarea name="" id="" placeholder="Content" rows="4" cols="30"></textarea>
        <button type="submit">Save</button>
        <button type="submit" formtarget="_blank">Preview</button>
    </form>

    <h3>Q35</h3>
    <form action="../submit.php" method="post">
        <label for="user">Username:</label>
        <input type="text" name="Username" id="user" required>
        <label for="pass">Password:</label>
        <input type="password" name="Password" id="pass" required minlength="8">
        <button type="submit">Submit</button>
    </form>

    <h3>Q36</h3>
    <form action="">
        <fieldset>
            <legend>Personal Information</legend>
            <label for="name">Name:</label>
            <input type="text" name="Name" id="name" required>
            <label for="email">Email:</label>
            <input type="email" name="Email" id="email" required>
        </fieldset>
        <fieldset>
            <legend>Preferences</legend>
            <input type="checkbox" name="newsletter" id="newsletter">
            <label for="newsletter">Subscribe to Newsletter</label>
        </fieldset>
    </form>
</body>
</html>
```
