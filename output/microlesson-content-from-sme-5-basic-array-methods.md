# Basic Array Methods

**Learning Objective:** Use basic array methods, such as push() and pop(), to manage array data.

## Introduction to array methods push() and pop()

Arrays in JavaScript are lists that help us organize and manage groups of data. Sometimes, we need to add more items to our list or remove some. To make these tasks easy, JavaScript gives us special tools called "methods."

Two of the most common array methods are `push()` and `pop()`. They're like simple controls for lists: one adds items to the end of your list, and the other removes them from the end. By learning how to use these, you'll be able to grow and shrink your arrays whenever you need.

Let's look at what these methods do and how you might use them to manage lists in your code.

## Adding elements to the end of an array with push()

Imagine you're making a list of groceries. You might start out with a few items, but as you remember more, you need a way to add them to your list. The `push()` method lets you add one or more items to the end of an array.

### Example: Using push() to add to your list

```javascript
let groceries = ["apples", "bananas"];
groceries.push("oranges"); 
console.log(groceries); // ["apples", "bananas", "oranges"]
```

Here, `push("oranges")` adds "oranges" to the end of the groceries array.

You can also add more than one item at the same time:

```javascript
groceries.push("milk", "bread");
console.log(groceries); // ["apples", "bananas", "oranges", "milk", "bread"]
```

Think of `push()` as the action of sticking a new sheet at the end of a stack.

## Removing elements from the end of an array with pop()

Now, what if you want to remove the last thing on your list? That’s where `pop()` comes in. The `pop()` method removes the last item in the array.

### Example: Using pop() to remove from your list

```javascript
let groceries = ["apples", "bananas", "oranges"];
groceries.pop();
console.log(groceries); // ["apples", "bananas"]
```

In this example, calling `pop()` takes "oranges" off the list.

`pop()` is handy when you want to undo your last addition or simply trim your list. You can call it as many times as you need, and each time it removes just the last item.

## Returning values from array methods

Both `push()` and `pop()` not only change the array but also return something useful.

- `push()` returns the new length of the array after the items are added.
- `pop()` returns the item that was removed.

Let's take a closer look.

### Example: What push() returns

```javascript
let numbers = [1, 2];
let newLength = numbers.push(3);
console.log(newLength);  // 3
```

After adding `3`, the new length of the numbers array is `3`.

### Example: What pop() returns

```javascript
let fruits = ["apple", "banana", "cherry"];
let lastFruit = fruits.pop();
console.log(lastFruit); // "cherry"
```

After calling `pop()`, the method gives back "cherry" – the item it just removed.

This can be helpful when you want to know exactly what was removed from your list.

## Hands-on coding: Implementing push() and pop() in a dynamic task list scenario

Now, let's put what we've learned into practice by managing a dynamic "To-Do" list. Imagine you're tracking your daily tasks and want to add new tasks as you remember them, and check off (remove) tasks as you finish them.

### Activity: Building your dynamic to-do list

**Instructions:**

1. Open your JavaScript editor or online tool (for example, repl.it, JSFiddle, or your browser's developer console).
2. Create an array to represent your current task list. Start with at least two things you need to do today.
3. Use `push()` to add a new task to the end of your task list. Print the updated list to the console.
4. Use `push()` again to add another task. Print the updated list and observe the new length returned by `push()`.
5. Decide that you've finished the most recent task. Use `pop()` to remove this from your task list. Save the removed task in a variable and print out both the updated list and the name of the removed task.
6. Challenge yourself: Try adding and removing tasks a few more times, experimenting with how the list changes and what each method returns.

**Deliverable:**  
Share your code and output with a classmate, in the chat, or in a group discussion area. Be ready to explain how you used `push()` and `pop()` to change your task list and what each method returned.

**Discussion prompt:**  
Think about a real-world scenario where managing a list with `push()` and `pop()` could save you time or make a repetitive process easier. How could you apply these methods outside of a to-do list, such as in work, home projects, or other daily routines? Share your ideas and discuss possible use cases with your peers.