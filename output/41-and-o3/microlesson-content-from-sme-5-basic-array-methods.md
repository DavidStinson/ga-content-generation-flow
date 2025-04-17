# Basic Array Methods

**Learning Objective:** Use basic array methods, such as push() and pop(), to manage array data.

## Introduction to array methods

In our earlier microlessons, we've explored what arrays are in JavaScript, how they organize data through elements and indices, how to create them, and how to access or update information inside them. Arrays aren't just about holding data—they also come with built-in tools, called "methods," that help us manage and work with the information they contain.

Think of array methods as special powers or abilities that let us quickly add, remove, and update the lists we create. Two of the most commonly used—and most helpful—methods are `push()` and `pop()`. These let us easily add or remove items at the end of an array, which is a common need in many real-world scenarios.

Let's break down what these methods are, how they work, and get some practice with code to see them in action.

## push() method: Adding elements to the end of an array

When you want to add something new to the end of your list, the `push()` method is your go-to tool. This method "pushes" a new value onto the tail (last position) of your array.

This is especially useful when you’re tracking items that arrive over time, such as new tasks on a to-do list or fresh fruit in a basket.

Here’s the basic way to use `push()`:

```javascript
let fruits = ["apple", "banana"];
fruits.push("cherry");
console.log(fruits); // Output: ["apple", "banana", "cherry"]
```

- Before calling `push()`, `fruits` contains two items.
- After calling `fruits.push("cherry")`, "cherry" appears as the new last item of the array.

You can also use `push()` to add multiple items at once:

```javascript
let numbers = [1, 2, 3];
numbers.push(4, 5);
console.log(numbers); // Output: [1, 2, 3, 4, 5]
```

With one command, you've added two values to the end of the numbers array.

### Real-world connection

Imagine you're organizing a guest list for a party. As each new RSVP comes in, you simply tack the new name to the end of your list. That’s how `push()` works with arrays—like adding another entry to the bottom of a growing sign-up sheet.

## pop() method: Removing elements from the end of an array

Just as `push()` lets you add, `pop()` is the simplest way to remove the last item in an array. Think of `pop()` as popping the lid off a stack—whatever was most recently added is the first to come off.

Here’s an example:

```javascript
let tasks = ["wash dishes", "take out trash", "feed cat"];
let lastTask = tasks.pop();
console.log(tasks);      // Output: ["wash dishes", "take out trash"]
console.log(lastTask);   // Output: "feed cat"
```

- The array `tasks` starts with three items.
- Using `pop()` removes the last item ("feed cat") and returns it, which we store in the `lastTask` variable.
- Now, `tasks` only has the first two elements left.

`pop()` is handy when you need to process things in reverse order or keep trimming your list as tasks are completed or items are removed.

### Visualizing push() and pop()

If you picture your array as a stack of trays in a cafeteria, `push()` adds a new tray on top of the pile, while `pop()` removes the top tray. The last tray placed is always the first one taken away.

## Practical examples of using these methods in code

Let's use both methods to see how they work together in a common scenario.

Suppose you’re managing a playlist:

```javascript
let playlist = ["Song A", "Song B", "Song C"];

// A friend recommends a new song
playlist.push("Song D");
console.log(playlist); // ["Song A", "Song B", "Song C", "Song D"]

// You listen to the last song and want to move on
let lastSong = playlist.pop();
console.log(playlist);  // ["Song A", "Song B", "Song C"]
console.log(lastSong);  // "Song D"
```

Notice how each time you use `push()`, your playlist grows, and each time you use `pop()`, it shrinks by one at the end. You can keep going, mixing both as your needs change.

### Practice scenario: Task management

Arrays and these methods show up everywhere:
- Adding a new item to your online shopping cart uses `push()`.
- Removing the most recently browsed webpage from your browser history might use `pop()`.

The simplicity and directness of these methods make them among the first tools every new JavaScript developer comes to rely on.

## Activity: Practice using push() and pop() on your bucket list

It’s time to put these core array methods to work yourself.

### Instructions

1. Open your JavaScript coding environment. You can use your browser's console, an online playground like JSFiddle or CodePen, or your local code editor.

2. Create a new array called `bucketList`, and add at least three places you'd love to visit in your lifetime. For example:
   ```javascript
   let bucketList = ["Machu Picchu", "Great Barrier Reef", "Santorini"];
   ```

3. Imagine you remember another dream destination. Use `push()` to add it to your array. Print the updated array.
   ```javascript
   bucketList.push("Norwegian Fjords");
   console.log(bucketList);
   ```

4. Now, let’s say you achieve your last-added dream trip! Use `pop()` to remove and store this item. Print the updated array and also print the value you removed.
   ```javascript
   let completedTrip = bucketList.pop();
   console.log(bucketList);
   console.log("Trip completed:", completedTrip);
   ```

5. Add two more destinations in one line using `push()`. Print the updated array.
   ```javascript
   bucketList.push("Petra", "Antarctica");
   console.log(bucketList);
   ```

6. Deliverable: Copy and paste your `bucketList` array definition, each `push()` and `pop()` call, and all relevant `console.log` statements into the chat or your group’s discussion forum for review.

### Discussion Prompt

After practicing with `push()` and `pop()`, think about a real-world list you manage—this could be chores for the week, shows to watch, or tasks at work. Which method (adding to the end or removing from the end) best matches how this list changes over time? Could you see a use for both at different points? Share your scenario with the group and reflect on when you’d want to add vs. remove items using these methods.