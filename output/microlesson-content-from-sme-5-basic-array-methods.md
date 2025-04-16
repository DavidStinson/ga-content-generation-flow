# Basic Array Methods

**Learning Objective:**  
Use basic array methods, such as `push()` and `pop()`, to manage array data.

---

## Introduction to array methods

Arrays in JavaScript act like organized lists — a way to store and manage multiple pieces of information using one variable. You've already learned how to create arrays and access or modify their elements. Now, imagine you want to keep updating your list: maybe you need to add a new item to the end, or remove the last item you added. JavaScript provides simple, built-in tools called “array methods” to help you do this quickly and easily.

Array methods are like special instructions you give to your array for common tasks. The most frequently used methods for beginners are `push()` and `pop()`. Let’s explore what these do and how you can use them.

---

## Using push(): Adding elements to the end of an array

The `push()` method adds one or more items to the **end** of an array — just like adding something new at the bottom of a shopping list. With `push()`, you can expand your array as you go, without having to create a brand new list every time.

### How `push()` works

- The syntax is:  
  `arrayName.push(newItem);`
- This will increase the array’s length by one, with the new item at the very end.

**Example: Adding to a shopping list**
```javascript
let shoppingList = ["milk", "bread"];
shoppingList.push("eggs");
console.log(shoppingList); // Outputs: ["milk", "bread", "eggs"]
```

You can also add more than one item at once:
```javascript
shoppingList.push("cheese", "apples");
console.log(shoppingList); // Outputs: ["milk", "bread", "eggs", "cheese", "apples"]
```

#### Analogy

Think of `push()` like sticking a new Post-it at the bottom of a stack — your stack of notes grows longer, but stays in order!

---

## Using pop(): Removing elements from the end of an array

The `pop()` method does the opposite of `push()`: it **removes** the last item from the array. Imagine finishing the last task on your to-do list and crossing it off. That’s exactly how `pop()` works with arrays.

### How `pop()` works

- The syntax is:
  `arrayName.pop();`
- This removes the **last** item from your array — the one at the highest index.
- `pop()` also returns the item it removed, so you can save or display it if needed.

**Example: Removing from a shopping list**
```javascript
let shoppingList = ["milk", "bread", "eggs"];
let removedItem = shoppingList.pop();
console.log(removedItem);       // Outputs: "eggs"
console.log(shoppingList);      // Outputs: ["milk", "bread"]
```

#### Analogy

Using `pop()` is like peeling off the last sticky note from your list — it disappears from the end, and your stack gets shorter.

---

## Practical scenarios for using push() and pop()

Let’s connect these methods to everyday situations:

- **Building a playlist:**  
  You can use `push()` to add new songs to the end of your queue. If you decide to remove the last song, `pop()` is your tool.

- **Task management:**  
  As new tasks come up, you `push()` them onto your to-do list. Once you finish the most recently added task, simply `pop()` it off.

- **Team sign-ups:**  
  When team members register for an event, you can `push()` their names onto an array. If the last person decides to drop out, `pop()` removes them from the list.

**Example in code: Playlist building**
```javascript
let playlist = ["Song A", "Song B"];
playlist.push("Song C"); // playlist is now ["Song A", "Song B", "Song C"]
let lastSong = playlist.pop(); // lastSong is "Song C", playlist is now back to ["Song A", "Song B"]
```

These methods help you keep your arrays up to date — no need to recreate your list from scratch each time something changes.

---

## Activity: Practice managing a dynamic list with push() and pop()

It’s time to try out these new tools for yourself! This exercise will help you practice using `push()` and `pop()` to update an array, simulating a real-life scenario.

### Step-by-step instructions

1. **Open a JavaScript editor** (such as [JSFiddle](https://jsfiddle.net/), [CodePen](https://codepen.io/), or your local editor).
2. **Create an array named `todoList`** and pre-fill it with three tasks you might do today.  
   Example:  
   `let todoList = ["Send emails", "Attend meeting", "Review notes"];`
3. **Add a new task to your to-do list** using the `push()` method.  
   Example:  
   `todoList.push("Call client");`
4. **Print the whole array** to the console to see your updated list.
   ```javascript
   console.log(todoList);
   ```
5. **Remove the last task from your list** (as if you just completed it) using `pop()`.  
   Save the result into a variable called `completedTask`.
6. **Print `completedTask`** to the console to show which task you finished.
7. **Print the updated `todoList`** to see your current to-dos.
8. **Add comments** to your code explaining each step as you use `push()` and `pop()`.

**Example code (with comments):**
```javascript
// 1. Create a to-do list with three tasks
let todoList = ["Send emails", "Attend meeting", "Review notes"];

// 2. Add a new task to the end of the list
todoList.push("Call client");

// 3. Print the updated to-do list
console.log(todoList); // ["Send emails", "Attend meeting", "Review notes", "Call client"]

// 4. Remove the latest task (completed) and store it
let completedTask = todoList.pop();

// 5. Print the completed task
console.log(completedTask); // "Call client"

// 6. Print the to-do list after removing the last task
console.log(todoList); // ["Send emails", "Attend meeting", "Review notes"]
```

### Deliverable

- Copy your full code snippet (with comments) and paste it in the class chat or your virtual whiteboard.
- Write 1-2 sentences reflecting on how using `push()` and `pop()` made updating your list easier than creating a whole new array each time.


### Discussion prompt

Array methods like `push()` and `pop()` help us keep our lists flexible and current — whether we're organizing tasks, shopping lists, or anything in between. Think about a real-world situation (in your work, studies, or daily life) where being able to quickly add or remove items from a list would be especially helpful. Share your example with the group, and read your peers’ posts. Reply to at least one peer with a comment — perhaps sharing a new scenario, or a benefit of using arrays in that context.

---

By learning to use `push()` and `pop()`, you are gaining practical tools for managing lists in your JavaScript programs. These basic methods form the foundation for even more powerful data handling in the future. Keep practicing — you’ll soon find these array updates are second nature!