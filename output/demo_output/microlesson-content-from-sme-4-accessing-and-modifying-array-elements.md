# Accessing and Modifying Array Elements

**Learning Objective:** Access and modify elements within an array using square brackets.

## Using square bracket notation to access elements

In previous lessons, we explored what arrays are, how they're structured with elements and index positions, and how to create arrays using literal notation. Now, let's dive deeper into how to access and work with individual elements stored in an array.

When you want to retrieve a specific item from an array, JavaScript uses **square bracket notation**. This means you write the name of the array, immediately followed by a pair of square brackets. Inside those brackets, you put the index of the element you want to access. Remember from earlier: array indices start at 0, so the first element is at position 0, the second at 1, and so on.

Let's see this in action:

```javascript
let fruits = ["apple", "banana", "cherry", "date"];
console.log(fruits[0]); // Prints "apple"
console.log(fruits[2]); // Prints "cherry"
```

If you picture the array as a row of mailboxes (like we discussed earlier), each mailbox has a number underneath. By writing `fruits[2]`, you're asking for "the item in the third mailbox," which is `"cherry"`.

It's important to use this zero-based indexing every time you access an element, so always double-check that you're using the correct number for the position you want.

## Modifying existing array elements

Arrays are flexible containers. You can not only access their contents but also **change (or update)** the value stored at any position.

To modify an array element, use the same square bracket notation, but this time, use the assignment operator (`=`) to assign a new value to that specific position.

Here's how you might update the second element in our fruits array:

```javascript
fruits[1] = "blueberry";
console.log(fruits); // Output: ["apple", "blueberry", "cherry", "date"]
```

Notice:
- We're telling JavaScript: "In the `fruits` array, at index `1`, set the value to `'blueberry'`."
- The rest of the array stays the same—only the value at index 1 is changed.

You can repeat this process for any index that exists in the array. This feature makes arrays especially useful when you need to update or correct data as a program runs.

## Common pitfalls when accessing and modifying elements

While square bracket notation is powerful, there are a few common pitfalls you'll want to avoid as you start working with arrays.

1. **Off-by-one errors:** Since indexing starts at 0, it's easy to accidentally target the wrong position. For example, if an array has three elements, their indices are 0, 1, and 2. Trying to access index 3 will not give you the third item—it will actually be `undefined` because no such position exists yet.
   ```javascript
   let pets = ["cat", "dog", "hamster"];
   console.log(pets[3]); // Prints undefined
   ```

2. **Accessing out-of-bounds indices:** If you try to access or modify an element at an index that doesn’t exist, you’ll either get `undefined` (when accessing) or create a gap in your array (when assigning). Be careful: assigning to an index much higher than the current length will add empty slots ("holes") between items.
   ```javascript
   pets[5] = "goldfish";
   console.log(pets); // Output: ["cat", "dog", "hamster", empty × 2, "goldfish"]
   ```

3. **Mixing up data types:** Arrays can hold mixed data, but for predictability, it's usually best to keep elements in an array to the same type (all strings, or all numbers, for instance).

4. **Using incorrect indices when updating:** Double-check which index you're modifying—otherwise, you could accidentally overwrite the wrong item.

## Practical examples of element manipulation

Let's look at a few real-world scenarios where accessing and modifying array elements comes in handy:

**Example 1: Updating a to-do list**

Suppose you have an array representing your daily tasks. If you've finished a task or want to change a description, just update the correct index.

```javascript
let todos = ["Check email", "Attend meeting", "Write report"];
// Mark "Attend meeting" as done by updating the element
todos[1] = "Attend meeting (done)";
console.log(todos);
// Output: ["Check email", "Attend meeting (done)", "Write report"]
```

**Example 2: Correcting a typo in contact names**

Say you have an array of contact names, but notice a mistake:

```javascript
let contacts = ["Sam", "Alex", "Jonh"];
contacts[2] = "John"; // Correct the typo
console.log(contacts); // Output: ["Sam", "Alex", "John"]
```

**Example 3: Accessing data for user display**

If you want to show the first and last items from a shopping cart array:

```javascript
let cart = ["Laptop", "Phone", "Headphones"];
console.log(cart[0]); // "Laptop"
console.log(cart[cart.length - 1]); // "Headphones"
```

Notice here, `cart.length - 1` always gives us the last item, no matter how many items are in the array. This is a handy trick for working dynamically with list data!

## Activity: Practice with accessing and modifying array elements

Let's solidify your understanding with some hands-on coding!

### Instructions

1. **Open your code editor or an online JavaScript sandbox (like repl.it or JSFiddle).**
2. **Create an array of four book titles you enjoy.**
   - Example:
     ```javascript
     let favoriteBooks = ["1984", "Dune", "Matilda", "Pride and Prejudice"];
     ```
3. **Print the entire array to confirm it's set up correctly.**
4. **Access and print the second and fourth books using index positions.**
5. **Update the third book in your array to another book you've recently read or wish to read.**
   - Use square bracket notation to change the element in place.
6. **Print the updated array to the console to confirm the change.**
7. **Try to access an index that does not exist (for example, index 10) and observe what happens. Print this value to the console.**
8. **Deliverable:** 
   - Share your code snippet that demonstrates: the original array, element access, the update, and your console output for both valid and invalid accesses. 
   - Post your work to your class discussion board or share it with a partner.

### Discussion prompt

Indexes are a crucial part of working with arrays in JavaScript. Think about a real-life scenario where you might update part of a list—maybe correcting a name in a guest list, changing the status of a task, or swapping out an item in your grocery list. What could go wrong if you accidentally use the wrong index? Share your scenario and discuss with your group how you might prevent or catch such mistakes in your code.