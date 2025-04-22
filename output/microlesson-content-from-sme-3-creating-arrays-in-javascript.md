# Creating Arrays in JavaScript

**Learning Objective:** Create arrays using JavaScript literal notation.

## Array literal notation syntax

In JavaScript, the most common way to create an array is using **array literal notation**. This simply means writing your array directly into the code, enclosed by square brackets (`[` and `]`). Each value in the array is separated by a comma.

You can think of array literals like making a shopping list and writing each item, separated by commas, on a single sheet of paper. This approach makes your code clear and concise.

**Example:**

```javascript
let shoppingList = ['milk', 'eggs', 'bread'];
```

In this example, `shoppingList` is an array holding three string elements: `'milk'`, `'eggs'`, and `'bread'`. Creating arrays with literal notation is not just the most straightforward way—it's also the most widely used in real-world JavaScript projects.

**Key features of array literal notation:**

- Use square brackets to define the array.
- Separate each element with a comma.
- Elements can be any data type (more on this shortly).

## Creating empty arrays

Sometimes, you want to start with an array that’s empty and add values later. You can do this by using an empty pair of square brackets:

**Example:**

```javascript
let emptyList = [];
```

Now, `emptyList` exists in your program, but it doesn’t hold any elements—yet. You might use this if you're collecting information from a user or generating a list as your code runs.

**Why create an empty array?**

Imagine you're building a guest list for a party. At first, you might not know who will attend, so you start with nothing:

```javascript
let guestList = [];
```

As people RSVP, you'll add their names to the array.

## Initializing arrays with values

It’s very common to start with an array that already has some values you know you’ll need from the beginning—this is called **initializing an array with values**.

**Example:**

```javascript
let seasons = ['Spring', 'Summer', 'Autumn', 'Winter'];
```

This array is ready to use, with all four seasons already included. You can access each season by its index—just as you learned in earlier microlessons:

```javascript
console.log(seasons[0]); // Output: 'Spring'
```

You can also create arrays with numbers or other data types:

```javascript
let ages = [25, 30, 44, 18];
```

It's helpful to initialize arrays when you already know what values you need, like days of the week, months in a year, or a set of predefined settings for a program.

## Arrays with mixed data types

While it's most common to keep arrays consistent (all numbers, all strings, etc.), JavaScript allows arrays to store **mixed data types**. This means you can have numbers, strings, booleans, and even other arrays all together.

**Example:**

```javascript
let mixedArray = ['hello', 42, true, null, [1, 2, 3]];
```

In the `mixedArray` above, each element has a different type:

- `'hello'` is a string
- `42` is a number
- `true` is a boolean
- `null` represents the intentional absence of any value
- `[1, 2, 3]` is itself another array (sometimes called a nested array)

**Why does this matter?**

Flexibility can be useful, but it's also important to stay organized. When you mix types in an array, it can become harder to keep track of what each slot is used for, especially as your projects grow. For most beginner projects, try to stick with one type per array until you get comfortable.

## Activity: Build, Explore, and Share Your Array

Let's get hands-on with creating JavaScript arrays using literal notation.

### Instructions

1. **Pick a category:** Choose a theme that interests you—this could be your favorite snacks, cities you’d like to visit, TV shows you enjoy, or types of pets.
2. **Create three arrays:**
   - An empty array. 
   - An array initialized with at least four values of the same data type (for example, four cities).
   - An array that mixes at least three different types (for example, a string, a number, and a boolean).
3. **Print your arrays:** Use `console.log()` to display each array in your editor or console.
4. **Add a value to your empty array:** Using the bracket notation learned earlier, put a new value in your empty array. For example:
   ```javascript
   let emptyArray = [];
   emptyArray[0] = 'First item';
   ```
   Print the updated array.
5. **Share your arrays:** Post your code snippets in the group chat or your virtual classroom space. Review what others have created—do you notice any creative or unusual combinations?

### Deliverable

- Code snippets for each of your three arrays.
- Your console output that shows the arrays and any updates you made.
- A brief note about your chosen theme.

### Discussion prompt

Why might you choose to keep arrays consistent with just one data type, and when could it be useful to mix types together? Do you see any risks or benefits to having mixed-type arrays as your programs get more complex? Let’s discuss real-world scenarios where each approach might be more effective.