# Creating Arrays with Literal Notation

**Learning Objective:** Create arrays using JavaScript literal notation.

## Introduction to array literal notation syntax

Arrays are a fundamental way to hold lists of items in JavaScript. When we say "literal notation," we're talking about a simple, direct way to create an array using square brackets: `[ ]`. It's a bit like listing your favorite items inside a container. Each item, or "element," is separated by a comma.

Here’s the basic syntax for creating an array with literal notation:

```javascript
let colors = ["red", "green", "blue"];
```

In this example, `colors` is an array with three strings: "red", "green", and "blue." The square brackets tell JavaScript, "We're making an array now," and the commas separate each entry in the array.

Let’s look at how this breaks down:
- The opening bracket `[` marks the start of the array.
- Each item (`"red"`, `"green"`, `"blue"`) is an element in the array.
- The closing bracket `]` ends the array.

We’ll use this structure as the foundation throughout the lesson.

## Creating arrays with different data types

Arrays in JavaScript can store more than one type of data at a time. This is different from some other languages, where all elements in an array must be the same type. You can mix numbers, strings, booleans (true/false), or even other arrays—all in the same container.

Here are a few examples:

```javascript
let mixedArray = [28, "apple", true, null];
```

In this case, `mixedArray` has:
- A number: `28`
- A string: `"apple"`
- A boolean: `true`
- A special value representing "no value": `null`

Arrays are also able to store other arrays, like a list of lists. For example:

```javascript
let nestedArray = [[1, 2], ["a", "b"]];
```

To sum up, JavaScript arrays are flexible containers that can hold different data types together using literal notation.

## Empty arrays and their uses

Sometimes you won’t know yet what values will go into your array, or you want to start with an empty list and add items later. This is when you create an empty array.

Here’s how you make an empty array with literal notation:

```javascript
let emptyList = [];
```

This simple structure is useful when, for example, you're gathering input from a user or planning to add information step by step.

Why use empty arrays?
- Collect data dynamically, like user responses or scores as a game is played.
- Store results from a series of calculations as you process information.
- Help your code stay organized if you want to build up a list later.

You can later add elements to your empty array using JavaScript methods like `.push()`. For instance:

```javascript
emptyList.push("first item");
```

Now, `emptyList` contains one element: `["first item"]`.

## Demonstration: Creating various arrays in Visual Studio Code

Let’s imagine you have Visual Studio Code (VS Code) open and ready for JavaScript coding. Here are some hands-on examples you can type and run in your editor or a browser console.

**Example 1: An array of your top three favorite foods**

```javascript
let favoriteFoods = ["pizza", "sushi", "tacos"];
console.log(favoriteFoods);
```

**Example 2: An array with numbers**

```javascript
let luckyNumbers = [7, 13, 22];
console.log(luckyNumbers);
```

**Example 3: An array with mixed types**

```javascript
let everydayItems = ["keys", 5, true];
console.log(everydayItems);
```

**Example 4: An empty array to fill with user input**

```javascript
let toDoList = [];
console.log(toDoList); // []
```

For each example, look at the pattern: square brackets, commas, and the values inside.

You can use `console.log()` to print out the array and check what’s inside. If you follow along in VS Code, take a minute to type these out and change the values to your own favorites or interests.

## Guided practice: Creating arrays based on real-world scenarios

Now that you’ve seen how arrays work, let’s practice building some ourselves. Imagine a few different situations where you might use an array.

Here are some real-life scenarios:
- You want to keep track of books you’d like to read.
- You need a list of friends participating in a group chat.
- You’re storing temperatures measured during four weeks of an experiment.
- You’re outlining ingredients for a recipe.
- You are organizing your top five favorite destinations.

For each case, think about what values belong in your array and what type of data those values would be—are they all strings, numbers, or a mix? Try writing the literal notation array for at least two scenarios.

For example, to store cities you want to visit:

```javascript
let dreamDestinations = ["Tokyo", "Cairo", "Rome", "Sydney"];
```

Or a list of recipe ingredients:

```javascript
let ingredients = ["flour", "sugar", "eggs", "milk"];
```

Arrays are adaptable for almost any list-based need you encounter in everyday coding!

## Activity: Solo array creation challenge

Let’s reinforce what we’ve learned with some hands-on practice.

**Step-by-step instructions:**
1. Open Visual Studio Code or your favorite JavaScript workspace.
2. Think of three lists that relate to your own life or interests. Each list should have at least three items.
   - For example: favorite movies, grocery items, daily tasks, places you want to visit, or skills you want to learn.
3. For each list:
   - Use JavaScript literal notation (`[ ]`) to create an array and store your items as elements inside.
   - Assign the array to a `let` or `const` variable with a meaningful name.
   - Include at least one array with elements of different data types (such as a mix of numbers, strings, or booleans).
4. Use `console.log()` to print each array to the console.
5. Double-check your syntax: 
   - Make sure to use square brackets `[ ]`.
   - Separate each element with a comma.
   - Surround any string elements with quotes.

**Deliverable:**  
Post your three array code snippets to the shared class chat, or, if working solo, save them in your project folder for quick reference.

**Discussion Prompt:**  
Why might it be helpful to start with an empty array in some situations, rather than filling it immediately? Can you think of a real-world scenario where you’d want to let your array grow over time as events happen or users provide input?

Feel free to share your thoughts on how arrays could help you stay organized or solve problems in future projects!