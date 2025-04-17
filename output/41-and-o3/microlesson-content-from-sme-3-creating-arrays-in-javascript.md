# Creating Arrays in JavaScript

**Learning Objective:** Create arrays using JavaScript literal notation.

## Array literal notation syntax

To work effectively with data in JavaScript, you’ll often need to create arrays—ordered collections that let you store multiple values in one place. One of the most common and straightforward ways to make an array in JavaScript is using what’s called “array literal notation.”

Array literal notation uses square brackets `[ ]` to wrap a list of values, separated by commas. This approach is direct and easy to read, which is why it’s preferred in modern JavaScript.

Let’s break down what this looks like:

```javascript
let fruits = ["apple", "banana", "cherry"];
```

In this example:

- `let fruits` declares a variable named `fruits`.
- The `[` and `]` brackets show that you’re creating an array.
- `"apple"`, `"banana"`, and `"cherry"` are the elements, separated by commas.

This method lets you quickly create and fill arrays with as many elements as you need.

### Why use literal notation?

Literal notation is quick, readable, and widely used in codebases large and small. It’s the method you’ll see most frequently in tutorials and real-world JavaScript projects.

## Creating empty arrays

There will be times when you want to set up an array, but don’t know yet what values it will store. You can start with an empty array, then add items later programmatically or based on user input.

Here’s how to create an empty array:

```javascript
let emptyList = [];
```

Now, `emptyList` is ready to have elements added as your code runs.

For example, you might use `.push()` to add items one at a time:

```javascript
emptyList.push("first item");
console.log(emptyList); // ["first item"]
```

Why might you want an empty array? Imagine building a to-do list app. When a person first opens the app, their list is empty—but you still need a place to store new tasks as they’re added.

## Initializing arrays with elements

Often, you’ll want to create an array and fill it with some starting values immediately. This can make your code neater and more efficient, since everything is set up from the beginning.

Let’s take a closer look using a real-world scenario: storing favorite music genres.

```javascript
let musicGenres = ["rock", "jazz", "classical"];
```

Here, you’re telling JavaScript right away that you want to keep track of three genres. Each value inside the array is called an "element," and each one stays in its specific order unless you change it.

This way of setting up arrays is great for lists you already know, like the months of the year, ingredients in a recipe, or color options in a menu.

You can also initialize arrays with numbers, booleans, or even other arrays:

```javascript
let scores = [98, 85, 91, 100];
let booleanValues = [true, false, true];
let nestedArray = [["Mon", "Tues"], ["Wed", "Thu"]];
```

## Arrays with mixed data types

JavaScript arrays aren't limited to just one type of value. You can mix numbers, strings, booleans, and even objects or other arrays together if your program calls for it.

For example:

```javascript
let mixedArray = ["Hello", 42, true, null, { name: "Alex" }];
```

- The first element is a string: `"Hello"`
- The second is a number: `42`
- The third is a boolean: `true`
- The fourth is a special value: `null`
- The fifth is an object: `{ name: "Alex" }`

While JavaScript’s flexibility lets you mix types, it’s a good practice to keep arrays organized with similar items when possible. This makes your code easier to read and maintain. But when you need to represent something more complex—a list of settings, information from a form, or game state—this feature can be very helpful.

## Activity: Build and explore your own arrays

It’s time to put these concepts into practice by creating different types of arrays using literal notation.

**Instructions:**

1. Open your JavaScript play area, browser console, or an online editor like JSFiddle or CodePen.

2. Create the following arrays using array literal notation:

   - An empty array for a shopping list and print it to the console.
     ```javascript
     let shoppingList = [];
     console.log(shoppingList);
     ```
     
   - An array of three favorite movie titles as strings.
     ```javascript
     let favoriteMovies = ["Spirited Away", "The Matrix", "Coco"];
     console.log(favoriteMovies);
     ```
     
   - An array with at least one string, one number, and one boolean value.
     ```javascript
     let myInfo = ["Jordan", 29, false];
     console.log(myInfo);
     ```
   
   - An array with at least two different data types (get creative!). Print each array to the console right after you create it.

3. Add a new item to one of your arrays by using the `.push()` method, then print the updated array. For example:
   ```javascript
   favoriteMovies.push("Finding Nemo");
   console.log(favoriteMovies);
   ```

**Deliverable:**  
Copy and paste your array definitions and all corresponding `console.log` statements into the chat for group review.

**Discussion Prompt:**  
Think about the lists and data you organize in your daily life—groceries, playlists, contacts, or even steps in a routine. In what situations do you think an array with mixed data types might be useful? Do you see any advantages or challenges in organizing your data this way compared to sticking with a single data type per array? Share your thoughts and be prepared to discuss your decisions with the group.