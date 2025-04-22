# Basic Array Methods

**Learning Objective:** Use basic array methods, such as push() and pop(), to manage array data.

## Introduction to array methods

In our previous lessons, we've learned how arrays store data, how to create them, and how to access or modify their contents using indices. Now, let's explore a set of special functions called **array methods** that let us manage the data inside our arrays more efficiently. These methods can help us add, remove, or update items with simple, easy-to-remember commands.

You can think of array methods as tools in your programming toolbox. They allow us to organize, update, or clean up our lists as our program runs—without having to rewrite the whole array from scratch. 

Let’s look at the most common methods you’ll use when working with JavaScript arrays, especially when you want to add or remove elements.

## Using push() to add elements to the end of an array

The `.push()` method is one of the most frequently used array tools. Its job is simple: it **adds a new element to the end of an array**. This is perfect for situations where your list keeps growing—like adding new tasks to your to-do list or new names to a guest list.

Here's what it looks like in action:

```javascript
let shoppingList = ["apples", "bread", "milk"];
shoppingList.push("eggs");
console.log(shoppingList); // Output: ["apples", "bread", "milk", "eggs"]
```

Let’s break it down:
- The array `shoppingList` starts with three items.
- We call `shoppingList.push("eggs")` to add "eggs" at the end.
- After calling `.push()`, the array now has four items—the new one is always at the end.

You can also add more than one item at a time:

```javascript
shoppingList.push("cheese", "yogurt");
console.log(shoppingList); // Output: ["apples", "bread", "milk", "eggs", "cheese", "yogurt"]
```

**When is push() useful?**
- Keeping a running list of items, such as user responses or game scores.
- Dynamically updating content as your program runs, for example, as users add new entries.

## Using pop() to remove elements from the end of an array

Just as `.push()` lets us add at the end, the `.pop()` method allows us to **remove the last element from an array**. Think of it like taking the top book off a stack—you always remove from the end.

Here’s how it works:

```javascript
let colors = ["red", "green", "blue"];
let lastColor = colors.pop();
console.log(colors);      // Output: ["red", "green"]
console.log(lastColor);   // Output: "blue"
```

What happened here?
- We started with three colors.
- `colors.pop()` takes off the last color ("blue") and stores it in the variable `lastColor`.
- Now, the `colors` array only has two items.

`.pop()` is especially useful when you need to process or display the most recent item, or when cleaning up after a task is complete.

## Other useful array methods: unshift() and shift()

While `.push()` and `.pop()` work with the **end** of an array, `.unshift()` and `.shift()` help us work with the **beginning** of an array.

### unshift(): Adding elements to the start

The `.unshift()` method **adds one or more elements to the beginning of an array**. The items you add with `.unshift()` become the new first elements.

Example:

```javascript
let queue = ["Ann", "Bob"];
queue.unshift("Zara");
console.log(queue); // Output: ["Zara", "Ann", "Bob"]
```

Here, "Zara" is inserted at the very start of the array.

### shift(): Removing elements from the start

The `.shift()` method **removes the first element from an array**, similar to how `.pop()` removes from the end.

Example:

```javascript
let queue = ["Zara", "Ann", "Bob"];
let firstPerson = queue.shift();
console.log(queue);       // Output: ["Ann", "Bob"]
console.log(firstPerson); // Output: "Zara"
```

This is often used when you’re processing items in the order they arrived, like a line at a ticket counter.

### Comparing push/pop vs. unshift/shift

- **push()**: Add to the **end** (`["a", "b"]` → `["a", "b", "c"]`)
- **pop()**: Remove from the **end** (`["a", "b", "c"]` → `["a", "b"]`)
- **unshift()**: Add to the **start** (`["a", "b"]` → `["z", "a", "b"]`)
- **shift()**: Remove from the **start** (`["z", "a", "b"]` → `["a", "b"]`)

These methods let you treat your array like a stack (last-in, first-out) or a queue (first-in, first-out), depending on how you use them.

## Practical exercises using array methods

Let’s bring these concepts together with some practical JavaScript snippets you might encounter in everyday scenarios:

**Example 1: Building a guest list**

Suppose you’re planning an event. Your guest list keeps growing as new people RSVP.

```javascript
let guestList = [];
guestList.push("Sophia");
guestList.push("Liam");
console.log(guestList); // Output: ["Sophia", "Liam"]
guestList.unshift("Olivia");
console.log(guestList); // Output: ["Olivia", "Sophia", "Liam"]
let firstToArrive = guestList.shift();
console.log(guestList); // Output: ["Sophia", "Liam"]
console.log(firstToArrive); // Output: "Olivia"
```

Notice how we built the list, added to both ends, and processed the first to arrive.

**Example 2: Canceling the latest task**

Let’s imagine a to-do list where you occasionally remove the last task you added.

```javascript
let todo = ["Wash dishes", "Take out trash"];
todo.push("Read book");
console.log(todo); // Output: ["Wash dishes", "Take out trash", "Read book"]
let canceledTask = todo.pop();
console.log(todo); // Output: ["Wash dishes", "Take out trash"]
console.log(canceledTask); // Output: "Read book"
```

These examples show how much flexibility array methods give you to manage changing data efficiently.

## Activity: Practice managing a playlist with array methods

Now it's your turn to apply these array methods! We'll work together to build and manage a music playlist.

### Step-by-step instructions

1. **Open your coding environment.**
   - Use your favorite code editor or an online JavaScript tool like repl.it or JSFiddle.

2. **Create your starting playlist.**
   - Make an array called `playlist` that includes three song titles as strings.
     ```javascript
     let playlist = ["Song A", "Song B", "Song C"];
     ```

3. **Add new songs with push() and unshift().**
   - Use `.push()` to add a song you recently discovered to the end of your playlist.
   - Use `.unshift()` to add your all-time favorite song to the start of the playlist.
     ```javascript
     playlist.push("Song D");
     playlist.unshift("Song X");
     console.log(playlist);
     ```
   - Print the playlist after each step to see how it changes.

4. **Remove songs with pop() and shift().**
   - Use `.pop()` to remove the last song (perhaps you decided it’s out of mood).
   - Store the removed song in a variable called `removedSong`.
   - Use `.shift()` to remove the first song (your favorite was overplayed).
     ```javascript
     let removedSong = playlist.pop();
     playlist.shift();
     console.log(playlist);
     console.log("Removed song:", removedSong);
     ```

5. **Print your final playlist to the console.**

6. **Deliverable:**
   - Share your code snippet with your learning group, instructor, or post it to the class discussion channel.
   - Your code should show the array being modified at each step, and printouts of the playlist after each change.

### Discussion prompt

Reflect on your experience managing your playlist: How did using `.push()`, `.pop()`, `.unshift()`, and `.shift()` make updating your list easier compared to manually assigning values or re-writing the array? Can you think of another situation—at work or in your daily life—where these methods could help you organize changing information? Share your insights with your group and discuss which method you found most helpful and why.