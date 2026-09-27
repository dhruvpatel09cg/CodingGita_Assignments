## Answers:
---
```html


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Assignment</title>
</head>
<body>
    <h2 align="center">Image Assignment</h2>
    <h3>Date: 14 August, 2026</h3>

    <img src="flower.jpg" alt="Flower Image" width="150" height="210">

    <img src="D:\IMAGE\logo.png" alt="GitHub logo" width="200">
    
    <img src="D:\IMAGE\Banner.jpg" alt="Banner" width="200">
    
    <img src="../Photo.jpg" width="200" title="Click to view full size">
    
    <img src="D:\IMAGE\Nature.jpg" alt="Beautiful nature view" width="300" height="200">
    
    <img src="D:\IMAGE\GZ.webp" title="Lazy loaded" loading="lazy" width="200">
    
    <img src="D:\IMAGE\Hero.jpeg" loading="eager" width="200">
    
    <img src="D:\IMAGE\shopping.webp" loading="auto" width="200">

    <p>
        Loading attribute set on "auto" lets the browser determine the best way to load images depending
        on network conditions and other factors. It allows the browser to decide whether to load image eagerly
        or lazily.
    </p>

    <img src="../medium.png"
        srcset="../small.png 480w, ../medium.png 800w, ../large.png 1200w"
        alt="Responsive image" width="300">

    <img src="D:\IMAGE\danger2.jpeg" alt="Emoji" width="200" height="200" loading="lazy" title="Emoji"
        srcset="../small.png 480w, ../medium.png 800w">

    <br><br>

    <img src="D:\IMAGE\logo.png" loading="eager" width="200">
    <img src="D:\IMAGE\Goggles.webp" loading="lazy" width="200">
</body>
</html>
```
