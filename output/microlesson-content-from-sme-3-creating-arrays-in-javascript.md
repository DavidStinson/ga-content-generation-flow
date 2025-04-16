# Creating Arrays in JavaScript

**Learning Objective:**  
Create arrays using JavaScript literal notation.

---

## Array literal notation syntax

Arrays are an essential part of working with JavaScript because they allow you to group multiple values under a single name. The most common—and most beginner-friendly—way to make an array is by using **array literal notation**.

**What is array literal notation?**  
Literal notation is a straightforward, visual way to create arrays in your code. It uses square brackets `[` and `]` to "wrap up" a list of items. Each item, called an **element**, is separated by a comma.

**Basic syntax:**

```javascript
let myArray = [item1, item2, item3];
```

- **`let`** (or `const`/`var`) is how you define a variable in JavaScript.
- **`myArray`** is the name you're giving to your array.
- The brackets **`[ ]`** create the array.
- The items inside the brackets are your elements, and they're separated by commas.

**Example with strings:**  
Suppose you want to list your favorite fruits:

```javascript
let fruits = ['Apple', 'Banana', 'Orange'];
```

Each fruit is a string (text inside quotes), and they're bundled together as one array called `fruits`.

**Why is it called "literal"?**  
Because what you write is exactly what you'll get—it's a direct, readable way to spell out your list.

---

## Creating empty arrays

Sometimes, you need to start with an array that has nothing in it and fill it up later (perhaps as your code runs and you collect new information). You can do this by simply writing a pair of empty square brackets.

**Example:**

```javascript
let emptyList = [];
```

- This creates an array called `emptyList` with zero elements.
- You can now add elements to it as needed later in your program.

**Everyday Analogy:**  
Think of an empty folder on your computer—it’s ready for you to add files at any time. An empty array acts the same way for your data.

---

## Creating arrays with initial values

If you already know what you want in your array, you can list the values right away. Arrays can store many different types of data, but in most beginner projects, you'll likely work with text (strings) or numbers.

**Example with strings (shopping list):**

```javascript
let shoppingList = ['Milk', 'Eggs', 'Bread'];
```

Now, `shoppingList` contains three elements: `'Milk'`, `'Eggs'`, and `'Bread'`.

**Example with numbers (scores):**

```javascript
let scores = [97, 86, 75];
```

The array `scores` holds three numbers.

**Mixing it all together:**  
Although possible, it's not recommended for beginners—but JavaScript does allow different types in one array:

```javascript
let mixedArray = ['Book', 42, true];
```
For now, keep your arrays simple with similar items for easier management.

**Visual Description:**  
Imagine a row of numbered boxes (these are your array indexes). You can place any item in each box when you create the array, or you can leave some boxes empty for now.

---

## Hands-on practice: Creating arrays in VS Code

Putting theory into action is the best way to learn programming. In this activity, you'll create different types of arrays using array literal notation.

### Step-by-step solo exercise

1. **Open Visual Studio Code (VS Code)** (or your preferred code editor) and create a new JavaScript file called `arrays-practice.js`.
2. **Create an empty array** called `tasks` and print it to the console:
    ```javascript
    let tasks = [];
    console.log(tasks); // Prints: []
    ```
3. **Create an array with initial values**: Pick a theme you like (for example, favorite movies, cities you'd like to visit, or types of cuisine). Create an array containing at least 4 items (as strings).
    ```javascript
    let favoriteMovies = ['Inception', 'Spirited Away', 'The Matrix', 'Hidden Figures'];
    console.log(favoriteMovies);
    ```
4. **Create another array** with at least 4 numbers (for example, ages, scores, or years) and print it to the console.
    ```javascript
    let years = [1998, 2005, 2012, 2023];
    console.log(years);
    ```
5. **Share your work**:
    - Post your file or code snippets (the array creations and printed outputs) to the class chat, discussion board, or designated sharing space.
    - Briefly introduce what type of list (array) you chose and why.
6. **Explore:** Try creating an empty array, and then adding some values to it later in your code (using comments to document each step).

---

### Discussion prompt

Arrays are everywhere in programming—from shopping lists to tracking the top scores in a game. Take a moment to reflect and discuss:

- **How did it feel to create your own arrays?**
- If you had to add more items later, what would be the advantage of starting with an empty array versus a pre-filled one?
- Can you think of a real-life scenario where you might start with an empty list and fill it gradually (for example, signing up for an event, collecting survey responses, or tracking completed tasks)?

Share your thoughts with your peers or your instructor. Listening to others' examples can help you imagine many ways arrays can help you organize information in your own projects.

---

## Key takeaways

- Arrays in JavaScript are created using square brackets—this is called literal notation.
- You can start with an empty array, or fill it with initial values right away.
- Elements in an array can be accessed, updated, and added to later, giving you flexibility and control over your data.
- Creating arrays is a foundational skill that will support your progress in handling more complex data tasks as you continue learning JavaScript.

---

*Ready to keep building? Practicing creating arrays now sets you up for confidently storing, updating, and managing all kinds of information in your programming journey!*