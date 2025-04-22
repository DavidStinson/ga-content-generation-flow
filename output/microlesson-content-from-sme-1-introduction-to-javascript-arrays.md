# Introduction to JavaScript Arrays

**Learning Objective:** Define JavaScript arrays and explain how they organize data.

## What are arrays in JavaScript?

Arrays in JavaScript are a way to store multiple values in a single container. You can think of an array as a list, like a row of mailboxes, where each mailbox holds a piece of information. Instead of creating a new variable for every item you need to store, you can group related values together in one place with an array.

In JavaScript, arrays are created using square brackets `[ ]`, and each item in the array is separated by a comma. Each value in an array is called an *element*, and every element has a numbered position called an *index*. In JavaScript, arrays start with an index of 0 — this means the first item is at position 0, the second at 1, and so on.

**Example:**

```javascript
let colors = ['red', 'green', 'blue'];
```

In this example, we’ve created an array named `colors` that holds three string elements: `'red'`, `'green'`, and `'blue'`. You can access each item by its index:

```javascript
console.log(colors[0]); // Output: red
console.log(colors[2]); // Output: blue
```

## Why use arrays?

Arrays provide a simple way to organize and work with collections of data. Let’s consider a scenario: Imagine you want to store the names of the days of the week to use in a calendar app. If you tried to do this without arrays, you’d need to create a separate variable for each day:

```javascript
let monday = 'Monday';
let tuesday = 'Tuesday';
let wednesday = 'Wednesday';
// ...and so on
```

This approach quickly gets messy, especially as your list grows! Instead, you can create one array and put all the days in it:

```javascript
let daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
```

Now it’s much easier to work with the data. You can easily find out what the third day is, loop through all the days, or add new ones if needed.

## How arrays organize and store data

Arrays organize data by storing values one after another, each in its own “slot” or index. This organization makes it possible to refer to any value based on its position in the array, rather than just its name.

Think about a train with numbered carriages (0, 1, 2, ...). Each carriage can hold a passenger (a value), and you can quickly find out who's in which carriage by looking up the carriage number.

Because arrays use indexes, it’s easy to:

- Access any value with its index (for example, `colors[1]`)
- Change values by assigning a new one to a certain index (`colors[2] = 'yellow';`)
- Group related data, which helps keep your code organized and more readable

Arrays can also hold different types of data, but typically you’ll keep the data in an array consistent (like an array of numbers or an array of strings). This approach makes your code easier to work with and understand.

**Example:**

Let’s modify an array:

```javascript
let fruits = ['apple', 'banana', 'cherry'];
fruits[1] = 'orange';    // Changes 'banana' to 'orange'
console.log(fruits);     // Output: ['apple', 'orange', 'cherry']
```

This example shows how you can update the value in the second slot (index 1) from `'banana'` to `'orange'`.

## Real-world examples of array usage

Arrays are everywhere—here are a few examples you might encounter in everyday life:

- **To-do Lists:** Storing all your tasks for the day.
- **Shopping Carts:** Keeping track of the items you’ve added in an online store.
- **Playlist Apps:** Listing the songs in your current playlist.
- **Contact Lists:** Maintaining a list of friends’ phone numbers or email addresses.

**Example:**

Let’s create an array that can be used as a simple to-do list:

```javascript
let todoList = ['Finish reading chapter', 'Go for a walk', 'Cook dinner'];
console.log(todoList[0]); // Prints the first thing to do: 'Finish reading chapter'
```

Arrays let you work with all the items on your list, add and remove tasks, and keep things organized for later use.

## Activity: Create your own array

Let’s put these concepts into practice by making your first array!

### Instructions

1. **Think of a Topic:** Choose a category that interests you — for example, your favorite foods, cities you’ve visited, or movies you enjoy.
2. **Create an Array:** In your online code editor or JavaScript console, create an array to hold at least three items related to your topic.
3. **Access an Element:** Use `console.log()` to print out the second item in your array.
4. **Change an Item:** Update the third item in your array to something different, then print the entire array to the console to see the change.
5. **Share:** Post your code in the group chat or your breakout room.

### Deliverable

- Your JavaScript code showing the array you created, the step where you accessed one element, the step where you changed one element, and the resulting array.

### Discussion prompt

What kind of information or scenarios would you want to organize with a list in your everyday life? How might an array make that easier compared to using separate variables? Let’s discuss some creative uses for arrays based on what you’ve learned so far.