```markdown
# Basic Array Methods

**Learning Objective:**  
Use basic array methods, such as `push()` and `pop()`, to manage array data.

---

## Introduction to Array Methods

Arrays in JavaScript are incredibly versatile: not only do they help us store and organize lists of information, but they also come with built-in methods—special commands that let us change, add, and remove data from our lists easily. In previous lessons, you've learned how to create arrays, access elements by index, and update them. Now, let's take it a step further and explore *array methods*—the core tools you'll use to interact with your arrays every day.

An "array method" is a function that's attached to every array in JavaScript. Think of methods as buttons you can press to make your array do something specific: like extending your checklist with new items or removing things you've already completed.

---

## `push()`: Adding Elements to the End

The most common way to add new data to an array is with the `push()` method. This method puts a new element (or several) right at the end of your array—like adding another box to the line or a new song at the end of your playlist.

**Syntax:**
```javascript
array.push(element1, element2, ...);
```

- `array` is your array variable.
- `push()` takes one or more items and adds them to the very end of the array.

**Example:**
```javascript
let groceries = ["milk", "bread"];
groceries.push("eggs");
console.log(groceries); // Output: ["milk", "bread", "eggs"]
```

**Plain Language:**  
Imagine your array is a row of lockers. `push()` lets you attach a new locker at the far end and put something new inside it.

> **Tip:** `push()` returns the new length of the array, but you can usually ignore this unless you need to know how long your array is afterward.

---

## `pop()`: Removing Elements from the End

What if you want to take the last item off your list—maybe you've finished a task or bought the last item on your shopping list? That's where the `pop()` method comes in. `pop()` removes the final element from the array and gives it back to you.

**Syntax:**
```javascript
let removedItem = array.pop();
```

- `pop()` doesn't need any arguments.
- It removes the last element and returns *what it removed*.

**Example:**
```javascript
let fruits = ["apple", "banana", "orange"];
let lastFruit = fruits.pop();
console.log(fruits);     // Output: ["apple", "banana"]
console.log(lastFruit);  // Output: "orange"
```

**Plain Language:**  
Imagine finishing the last task on your to-do list and then crossing it off. `pop()` is like erasing the last thing you added to your array!

> **Tip:** If your array is empty, `pop()` will just return `undefined` (meaning there's nothing left to remove).

---

## Brief Overview of Other Common Methods: `unshift()` and `shift()`

While `push()` and `pop()` help you manage the end of your list, there are also methods to work with the *beginning* of the array:

- **`unshift()`**: Adds one or more elements to the *start* of the array (the beginning of the line).
    - Example:
      ```javascript
      let queue = ["first", "second"];
      queue.unshift("zero");
      console.log(queue); // Output: ["zero", "first", "second"]
      ```
- **`shift()`**: Removes the very first element from the array.
    - Example:
      ```javascript
      let cars = ["Toyota", "Ford", "BMW"];
      let firstCar = cars.shift();
      console.log(cars);       // Output: ["Ford", "BMW"]
      console.log(firstCar);   // Output: "Toyota"
      ```

We're introducing these briefly so you know they're available, but for now, you'll focus on mastering `push()` and `pop()`.

---

## Practice: Manipulating Arrays with `push()` and `pop()`

It’s time to get hands-on! You’ll practice using `push()` and `pop()` to update a personal to-do list, right in your coding console or JavaScript editor.

### Activity: Build and Manage Your To-Do List

**Imagine** you have a digital to-do list for the week. You want to add new tasks as they come up and cross them off as you complete them. Let’s put `push()` and `pop()` to the test!

#### Step-by-Step Instructions

1. **Set Up Your To-Do List**
    - Create a new array called `todoList` that starts out with three tasks:
      ```javascript
      let todoList = ["Read emails", "Write project update", "Review code"];
      console.log(todoList);
      ```
      
2. **Add a New Task**
    - A new priority comes in: "Team meeting." Use `push()` to add it to the end of your list. Print the updated list.
      ```javascript
      todoList.push("Team meeting");
      console.log(todoList);
      ```
      
3. **Add Two More Tasks at Once**
    - Add "Prepare presentation" and "Update calendar" using a single `push()` statement.
      ```javascript
      todoList.push("Prepare presentation", "Update calendar");
      console.log(todoList);
      ```
      
4. **Tick Off (Remove) the Last Task**
    - You finished your most recent task! Use `pop()` to remove it and store the removed value in a variable called `completedTask`. Log both the updated array and the value you popped.
      ```javascript
      let completedTask = todoList.pop();
      console.log(todoList);
      console.log("Completed:", completedTask);
      ```
      
5. **Keep Going**
    - Use `pop()` again to finish and remove the next latest task. Print your results.
      ```javascript
      completedTask = todoList.pop();
      console.log(todoList);
      console.log("Completed:", completedTask);
      ```
      
6. **(Optional Challenge): Empty Your List**
    - Use `pop()` in a loop or as many times as you need until your array is empty. Observe what happens when you `pop()` from an empty array.

#### Deliverable

- **Share your Code and Console Output:**  
  Copy and paste your complete code and the results from each `console.log()` statement into the virtual classroom chat, a shared document, or as instructed by your facilitator.
- **Bonus:**  
  Note what value you get when using `pop()` on an empty array.

---

### Discussion Prompt

**Reflect:**  
How did using `push()` and `pop()` compare to adding and removing items from a physical list or notes app? Did you notice how easy it is to update your to-do list with just one line of code? Can you think of situations—either in your job, personal life, or even in other software—where being able to quickly add or remove data from the end of a list would save you time or prevent mistakes?

- Share a real-world scenario (from your life or work) where this type of list management could help you stay organized or be more efficient.
- If you tried the challenge, did you find anything interesting when popping from an empty array?

Discuss your experience and ideas with your group. Don’t worry if you found any steps tricky—that's how learning happens!

---

Congratulations!  
You’ve just learned two of the most practical tools for working with arrays in JavaScript: `push()` and `pop()`. Master these, and you’ll be able to start building dynamic lists, inventories, or task trackers in your own web projects, scripts, or future assignments.
```