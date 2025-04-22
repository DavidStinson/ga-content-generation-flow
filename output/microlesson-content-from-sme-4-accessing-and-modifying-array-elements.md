# Accessing and Modifying Array Elements

**Learning Objective:** Access and modify elements within an array using square brackets.

## Using square bracket notation to access elements

So far, you’ve learned that arrays in JavaScript are like organized lists where each value (element) has a specific position (index). But how do we actually look up or change items inside these arrays? The answer is square bracket notation.

To access an element in an array, you type the array’s name followed by the index of the element inside square brackets. Remember, JavaScript arrays use zero-based indexing—meaning the first element lives at index `0`, the second at index `1`, and so on.

**Example:**

```javascript
let fruits = ['apple', 'banana', 'cherry'];
console.log(fruits[0]); // Output: apple
console.log(fruits[2]); // Output: cherry
```

If you’re thinking of each array like a row of lockers, then accessing `fruits[1]` is like checking locker number 1 (the second locker, because we start from zero).

**Quick analogy:**  
Imagine a bookshelf with numbered spots. The number tells you where to find your book (the element).

## Modifying existing array elements

Arrays are designed to let us update or overwrite elements whenever our information changes. You use the same square bracket notation, but instead of just looking up an element, you assign a new value to it using the equals sign (`=`).

**Example:**

```javascript
let colors = ['red', 'green', 'blue'];
colors[1] = 'yellow'; // This changes the value at index 1 from 'green' to 'yellow'
console.log(colors); // Output: ['red', 'yellow', 'blue']
```

It’s similar to taking something out of a locker and putting something new inside.

**Why is this useful?**  
Any time you want to update data in a list, whether it's a to-do list, a game scoreboard, or a set of recorded temperatures, modifying array elements is the way to go.

## Adding new elements to specific positions

In JavaScript, arrays can change size as your program runs. That means you can add new elements—even if those positions didn’t exist before!

You add a new element by assigning a value to an index that’s equal to or greater than the current length of the array. If you add an element at the next available index, it increases the array’s length by one.

**Example:**

```javascript
let animals = ['cat', 'dog'];
animals[2] = 'hamster'; // Adds 'hamster' at index 2
console.log(animals); // Output: ['cat', 'dog', 'hamster']
```

You can also “skip” indexes, though this sometimes creates gaps filled with `undefined`. We usually add to the very end by using the current array length as the index:

```javascript
let books = ['1984', 'Brave New World'];
books[books.length] = 'Fahrenheit 451'; // Adds to the end
console.log(books); // ['1984', 'Brave New World', 'Fahrenheit 451']
```

**Tip:**  
There are built-in methods like `.push()` for adding to the end of an array, but here we’re focusing on bracket notation for clarity and practice.

## Common pitfalls when accessing or modifying arrays

Working with indexes in arrays opens the door to a few common mistakes. Let’s look at what to watch out for:

- **Index out of bounds:** If you try to access an element at an index that doesn’t exist, you get `undefined`.

  ```javascript
  let pets = ['parrot', 'iguana'];
  console.log(pets[5]); // Output: undefined
  ```

- **Accidentally skipping indexes:** If you assign to an index far beyond the current array length, JavaScript fills the skipped spots with `undefined`.

  ```javascript
  let groceries = ['bread'];
  groceries[3] = 'milk';
  console.log(groceries); // ['bread', undefined, undefined, 'milk']
  ```

- **Typo in the index:** Trying to use a string index (like `fruits['one']`) will not access the first element—always use numbers.

- **Trying to access negative indexes:** JavaScript arrays do not support negative indexes (like `fruits[-1]`), which will return `undefined`.

Understanding these behaviors helps you write code that behaves as you expect and avoids mysterious bugs.

## Practice exercises: accessing and modifying arrays

Let’s try using what we’ve learned so far. Here are a few small exercises:

**Example 1: Updating an element**
```javascript
let movies = ['Titanic', 'Inception', 'Avatar'];
movies[2] = 'The Matrix';
console.log(movies); // ['Titanic', 'Inception', 'The Matrix']
```

**Example 2: Adding a new element at the last index**
```javascript
let pets = ['dog', 'cat'];
pets[pets.length] = 'hamster';
console.log(pets); // ['dog', 'cat', 'hamster']
```

**Example 3: Exploring skipped indexes**
```javascript
let shopping = ['soap'];
shopping[4] = 'toothpaste';
console.log(shopping); // ['soap', undefined, undefined, undefined, 'toothpaste']
```

Think about what happens in each example and see if you can predict the result before running the code.

## Activity: Array element makeover – access, modify, and grow

Let’s put all these skills to work with a hands-on activity that walks you through accessing and modifying array elements.

### Instructions

1. **Choose a theme:** Pick a topic you enjoy, like your favorite sports teams, types of pizza, or places you want to visit.
2. **Create an array:** In your JavaScript editor or online playground, create an array with at least three string elements based on your theme.
3. **Access and print:** Print the first and last elements from your array using square bracket notation.
4. **Modify an element:** Change the second element in your array to a new value. Print the whole array to show the update.
5. **Add a new element:** Use bracket notation to add a new item at the end of your array (use the array’s current length as the index). Print your array again.
6. **Explore edge cases:** Try to access an index that doesn’t exist (for example, a number larger than your array’s length) and note what JavaScript returns.
7. **Share your code:** Post your code and output in the group chat, breakout room, or wherever your classroom shares solutions.

### Deliverable

Your submission should include:
- The code for your array, including the original setup, element access, modification, and new addition steps.
- The results of each printout, and a note describing any surprises or questions you encountered (for example, if you tried accessing an index that wasn’t present).

### Discussion prompt

As you experimented with modifying your array, did anything surprise you? How do you think JavaScript’s approach to array indexes and `undefined` values helps or complicates managing lists of data? Can you think of a real-life scenario where changing or adding items in a list (using indexes) would be especially powerful? Let’s discuss your discoveries and consider when these array techniques might be useful in your day-to-day life or in professional applications.