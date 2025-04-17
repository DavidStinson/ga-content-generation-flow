# Accessing and Modifying Array Elements

**Learning Objective:** Access and modify elements within an array using square brackets.

## Accessing elements using index notation

Arrays in JavaScript are organized collections that hold multiple values. Each value—known as an element—lives in a specific position inside the array, which is identified by a number called its *index*. One of the most powerful features of arrays is that we can use these indices to retrieve any value we want, almost like picking out a numbered box from a shelf.

The index numbers in JavaScript arrays always start at 0. This means the first element is at position 0, the second at 1, and so on.

To access an element in an array, we use *square brackets* after the array name, placing the index number inside. Let's look at an example:

```javascript
let fruits = ["apple", "banana", "cherry"];
console.log(fruits[0]); // Output: "apple"
console.log(fruits[2]); // Output: "cherry"
```

In this example:
- `fruits[0]` fetches the value `"apple"`, which is the first element.
- `fruits[2]` fetches `"cherry"`, the third element.

Remember: If you try to access an index that doesn’t exist—like `fruits[3]` in this example—you’ll get `undefined` as the result.

This method lets us grab any element quickly, making arrays a flexible tool for organizing and working with lists of information.

## Modifying existing elements

Not only can we retrieve elements from an array using their indices, but we can also update them. Changing a value in an array is just as straightforward as accessing it: we specify the index within square brackets, and then use the assignment operator (`=`) to give it a new value.

Here's how it works:

```javascript
let colors = ["red", "green", "blue"];
colors[1] = "yellow"; // Replaces "green" with "yellow"
console.log(colors); // Output: ["red", "yellow", "blue"]
```

In this code:
- We access the element at index `1` (the second spot, which is `"green"`) and set it to `"yellow"`.
- This change is permanent—unless you modify it again, the second item in the `colors` array will now be `"yellow"`.

**Key point:** You can update any element in an array as long as you know its index.

Updating elements using index notation is helpful when you want to correct or refresh data, update a user’s information, or replace outdated items in your list.

## Adding new elements to specific positions

There are different ways to add elements to an array. You might already be familiar with adding an element to the end using `.push()`. But what if you want to put a new value at a particular spot?

You can assign a value directly to a specific index—even if it didn’t have a value before. If the index doesn’t already exist, JavaScript will automatically expand the array to make room for your new item, and fill any “gaps” with `undefined`.

Example:

```javascript
let numbers = [10, 20, 30];
// Add a new number at index 1
numbers[1] = 25; 
console.log(numbers); // Output: [10, 25, 30]
// Add a new value at index 5 (skipping some positions)
numbers[5] = 100;
console.log(numbers); // Output: [10, 25, 30, undefined, undefined, 100]
```

Notice what happens with `numbers[5] = 100;`:
- The array now has six elements. Indices 3 and 4 didn't exist before, so JavaScript fills them with `undefined`.
- This is generally fine, but it’s best to avoid creating large gaps unless you have a specific need.

If you want to insert an element at a chosen position and shift the other items to make room, you’ll use methods like `.splice()`. For now, focus on basic assignment, which is the most direct way to place data at a known index.

## Common pitfalls when accessing and modifying elements

As you start experimenting with arrays, a few common issues can pop up. Being aware of them now can save you some confusion later!

### Off-by-one errors (due to zero-based indexing)

It's easy to forget that arrays start at index 0. If you have an array of three items, the last item isn't at position 3—it's at position 2.

Example:
```javascript
let pets = ["cat", "dog", "parrot"];
// Trying to access pets[3] returns undefined, not "parrot"
console.log(pets[3]); // Output: undefined
```

Always double-check the length of your array (`array.length`) and remember:
- The last index is always `array.length - 1`.

### Accidentally creating undefined elements

If you assign a value to an index that's far beyond the current end of the array, JavaScript fills the skipped spots with `undefined`:

```javascript
let example = ["a"];
example[4] = "z";
console.log(example); // Output: ["a", undefined, undefined, undefined, "z"]
```

This can make your code harder to follow or lead to unexpected behavior, especially if you’re planning to loop through the array later.

### Mutability: Changes affect the original array

Arrays in JavaScript are mutable, meaning once you change an element, that change sticks. Assigning a new value to any index will update the original array directly.

## Practice exercises with various array operations

Let’s tie all these ideas together with some hands-on coding examples. Read through each snippet below and imagine what would be printed to the console or how the array would look after the change:

```javascript
let foods = ["pasta", "rice", "bread"];
foods[0] = "pizza";       // What happens to the first item?
foods[3] = "salad";       // What does the array look like now?
console.log(foods);

let animals = ["lion", "tiger", "bear"];
console.log(animals[2]);  // What gets printed?
animals[2] = "wolf";
console.log(animals);     // How has the array changed?
```

Try these out in your code environment so you can see the results for yourself. Experiment by changing different positions and adding new elements beyond the array’s current length.

## Activity: Array update mission

It’s time to practice everything we’ve covered so far. In this solo exercise, you’ll access, modify, and add elements at specific positions in an array.

### Instructions

1. Open your JavaScript editor (or use an online tool like JSFiddle, CodePen, or your browser’s JavaScript console).
2. Create an array called `favoriteBooks` that holds the titles of three books you like.
   
   Example:
   ```javascript
   let favoriteBooks = ["Dune", "1984", "The Hobbit"];
   ```

3. Access and print the second book in your array by its index.
   ```javascript
   console.log(favoriteBooks[1]); // Should print the second book
   ```

4. Change the value of the first book to a new title that you’d like to recommend.
   ```javascript
   favoriteBooks[0] = "The Name of the Wind";
   ```

5. Add a new book to the end of the array—use either the assignment with the next available index or try `.push()`.
   ```javascript
   favoriteBooks.push("The Martian");
   // OR
   // favoriteBooks[favoriteBooks.length] = "The Martian";
   ```

6. Add a new book at index 5, intentionally leaving a gap in the array. Print the whole array to see what happens.
   ```javascript
   favoriteBooks[5] = "To Kill a Mockingbird";
   console.log(favoriteBooks);
   ```

7. Print out each book in your array using their indices (from 0 to `favoriteBooks.length - 1`). Notice which indices return `undefined`.

### Deliverable

Copy and paste your array definition, all print (`console.log`) statements, and any changes you made into the chat or your group forum for review.

### Discussion Prompt

When you added a new book at index 5, how did JavaScript handle the missing spaces in your array? What do you think are the risks or benefits of having arrays with gaps or `undefined` elements, especially if you’ll be sharing or processing this data later? Share your observations and any challenges you encountered while completing the activity.