# Basic Array Methods

**Learning Objective:** Use basic array methods, such as push() and pop(), to manage array data.

## Introduction to array methods

Now that you're familiar with creating arrays, accessing their elements, and even modifying values by their position, you're ready to explore one of the most powerful parts of working with arrays: array methods. 

Array methods are built-in tools JavaScript provides to make working with arrays easier. They let us add, remove, or even rearrange elements in an array—without having to worry about keeping track of exact index positions. Think of these like common actions you'd take with a list in real life, such as appending a new task to your to-do list or crossing out an item when it's done.

In this microlesson, you'll learn how to use a few important array methods for managing data, especially at the beginning and end of your arrays. These are actions you'll use almost every time you work with lists in JavaScript.

## push(): Adding elements to the end of an array

One of the most common things you'll do with arrays is add new elements. Instead of worrying about the last index number, JavaScript gives us the `.push()` method. This method lets us add new items right at the end of the array—just like sticking another note at the bottom of your grocery list.

**How does push() work?**

- It adds one or more new elements to the end of the array.
- It automatically grows the array’s length, so you don’t need to calculate where the last spot is.
- It returns the new length of the array (though most of the time, you’ll use it just for the adding part).

**Syntax:**
```javascript
array.push(element1, element2, ...);
```

**Example:**
```javascript
let colors = ['red', 'green', 'blue'];
colors.push('yellow'); // Adds 'yellow' at the end
console.log(colors); // Output: ['red', 'green', 'blue', 'yellow']
```

You can even add more than one item at a time!
```javascript
let fruits = ['apple', 'banana'];
fruits.push('cherry', 'date');
console.log(fruits); // Output: ['apple', 'banana', 'cherry', 'date']
```

**Why use push()?**  
It's efficient, easy to read, and helps keep your code clean when you want to add things to the end of an array—no more worrying about array length or messy index calculations.

## pop(): Removing elements from the end of an array

Lists often change: you add things, but you also take them off. The `.pop()` method removes the last element from your array—it's like erasing the last item on your list.

**How does pop() work?**

- It removes the last element in the array.
- It changes the length of the array (one less item than before).
- It returns the element that was removed, in case you need to know what it was.

**Syntax:**
```javascript
array.pop();
```

**Example:**
```javascript
let numbers = [10, 20, 30];
let removed = numbers.pop(); 
console.log(numbers); // Output: [10, 20]
console.log(removed); // Output: 30
```

You can use `pop()` without arguments—JavaScript just knows to remove the last item. This is great for all sorts of situations: checking off the last completed task, serving the last person in a queue, or undoing your most recent action.

**Tip:** If you try to pop from an empty array, you'll just get `undefined` and the array stays empty.

## Other useful methods: unshift() and shift()

So far, we’ve managed the end of the list—but sometimes, you need to work with the beginning. That’s where `.unshift()` and `.shift()` come in handy!

### unshift(): Adding elements to the beginning

The `.unshift()` method lets you add one or more elements right at the start of your array—just as if you were inserting new tasks at the top of your to-do list.

**Syntax:**
```javascript
array.unshift(element1, element2, ...);
```

**Example:**
```javascript
let animals = ['dog', 'cat'];
animals.unshift('hamster');
console.log(animals); // Output: ['hamster', 'dog', 'cat']
```

You can stack multiple items at the beginning all at once:
```javascript
let letters = ['b', 'c'];
letters.unshift('a');
console.log(letters); // Output: ['a', 'b', 'c']
```

### shift(): Removing elements from the beginning

The `.shift()` method removes the first element from an array—like pulling the first ticket from a queue.

**Syntax:**
```javascript
array.shift();
```

**Example:**
```javascript
let queue = ['Alice', 'Bob', 'Charlie'];
let next = queue.shift();
console.log(queue); // Output: ['Bob', 'Charlie']
console.log(next);  // Output: 'Alice'
```

`shift()` is especially helpful when you need to process or remove the oldest element in a list (for example, in a waiting list, or when reading data in order).

**A quick table to compare:**

| Method     | Action                         | Where?      |
|------------|-------------------------------|-------------|
| push()     | Adds to array's end           | End         |
| pop()      | Removes from array's end      | End         |
| unshift()  | Adds to array's start         | Beginning   |
| shift()    | Removes from array's start    | Beginning   |

## When should you use each method?

- Use **push()** and **pop()** when you’re working with the end of an array (think: stacks of plates, adding/removing from the top).
- Use **unshift()** and **shift()** for the beginning (think: queues for service—first in, first out).

These methods make managing your arrays much simpler, especially as your lists grow or change while a program is running.

## Activity: Array playbook — practice with push, pop, shift, unshift

Let’s put these methods to the test! In this exercise, you’ll create and manage a list using the array methods you just learned.

### Instructions

1. **Create a new array:** Pick a theme you like—such as your favorite snacks, places to visit, or books you want to read. Create an array with at least three items related to your theme.
2. **Add with push():** Use the `.push()` method to add a new item to the end of your array. Print the result.
3. **Remove with pop():** Use the `.pop()` method to remove the last item from your array. Print the result, and print the item you removed.
4. **Add with unshift():** Add a new item to the beginning of your array using `.unshift()`. Print the result.
5. **Remove with shift():** Use `.shift()` to remove the first item from your array. Print the result, and print the item you removed.
6. **Experiment:** Try stacking multiple items at once with `.push()` or `.unshift()`. See how your array changes.

### Deliverable

- Post your code in the virtual classroom chat or group workspace.
- Share your array after each step with printouts showing the state of the array and which items were removed.
- Be ready to explain which method you used for each operation and why.

### Discussion prompt

After using these array methods, which one did you find most intuitive for your way of thinking—adding or removing from the beginning, or the end? Think about situations in your daily life (like managing a waiting list, or a stack of books). Can you think of a real-world scenario where each method—push, pop, shift, unshift—would make sense? Let’s discuss how these operations map to familiar, everyday tasks, and why choosing the right method matters as your data grows.