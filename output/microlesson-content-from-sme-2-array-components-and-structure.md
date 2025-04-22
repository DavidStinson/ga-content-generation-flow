# Array Components and Structure

**Learning Objective:** Identify the components of an array, including its elements and index positions.

## Elements: The items stored in an array

Arrays allow us to organize data by storing multiple pieces of information together, all in one container. Each individual piece of data in an array is called an **element**.

Think about a row of lockers at a gym. Each locker holds someone’s belongings—that’s how elements work in an array. You can store any type of value as an element—words (strings), numbers, or even other arrays.

**Example:**

```javascript
let fruits = ['apple', 'banana', 'cherry'];
```

In this array, `'apple'`, `'banana'`, and `'cherry'` are the elements. Each one is separated by a comma and placed inside square brackets.

We can mix different data types in an array, but for now, we’ll keep things simple and use arrays where each element is the same kind of thing. This makes your code neater and easier to read.

## Index positions: How elements are ordered

Every element in an array is assigned a number called its **index position**. This number shows the element’s place in the array—its address.

If you wanted to ask someone to open a specific locker for you, you’d need to give them the locker number. In arrays, you use the index to find or change elements.

Let’s look again at the `fruits` array:

```javascript
let fruits = ['apple', 'banana', 'cherry'];
```

- `fruits[0]` gives us `'apple'`
- `fruits[1]` gives us `'banana'`
- `fruits[2]` gives us `'cherry'`

The value inside the square brackets is the index position. The leftmost element starts at zero, not one. This leads us to our next important concept.

## Zero-based indexing in JavaScript

In JavaScript, arrays use **zero-based indexing**. That means the first element in an array is at index `0`, the second is at index `1`, and so on.

This can seem a bit odd if you’re used to counting from one, but it’s a programming tradition you’ll encounter in many languages. Keep in mind: if an array has 5 elements, the last one will have the index `4` (because we begin counting from zero).

**Example:**

```javascript
let colors = ['red', 'green', 'blue', 'yellow'];
console.log(colors[0]);   // 'red'
console.log(colors[3]);   // 'yellow'
```

If you try to access an index that’s not assigned (for example, `colors[4]`), JavaScript will return `undefined`, because there’s no element in that position.

## Array length and its significance

The **length** of an array tells you how many elements it contains. We can get this information using the `.length` property.

Why is this important? Knowing an array’s length helps you work with all its elements, especially when using loops or when you want to add new values.

**Example:**

```javascript
let tasks = ['Read', 'Code', 'Exercise'];
console.log(tasks.length);  // 3
```

If you needed to find the last element, you could use the length like this:

```javascript
console.log(tasks[tasks.length - 1]);
// Output: 'Exercise'
```

Subtracting 1 is key because of zero-based indexing—the last index is always one less than the length.

## Visualizing array structure

Let’s take a visual approach to drive home how arrays are structured. Imagine a table where each cell is a slot in the array:

| Index | Element   |
|-------|-----------|
|   0   | 'alpha'   |
|   1   | 'beta'    |
|   2   | 'gamma'   |

If we create an array:

```javascript
let greekLetters = ['alpha', 'beta', 'gamma'];
```

- The element at index 1: `greekLetters[1]` is `'beta'`
- The element at index 2: `greekLetters[2]` is `'gamma'`

Arrays keep your data lined up in order, and knowing the index lets you quickly find or change any element, no matter where it lives in the array.

## Activity: Map and modify — exploring array structure hands-on

Let’s put these ideas into practice so you can see array components and their structure in action.

### Instructions

1. **Create your own array:** Choose a category you’re interested in (favorite books, movies, foods, cities, etc.). In your JavaScript editor or online playground, create an array containing at least five elements (for example, the names of your favorite books).
2. **Label the index positions:** For each element in your array, use `console.log()` to print both the index and the element. For example: `Index 0: The Great Gatsby`.
3. **Find the length:** Use the `.length` property to display how many elements are in your array.
4. **Access the last element:** Using `.length - 1`, print out the last item in your array.
5. **Modify an element:** Change the value of one element (choose any except the first) and print your whole array again to see the change.

### Deliverable

- Share your code and the output in the group chat or with a partner. Your submission should clearly label each printout so others can see the index positions, the array length, and your modification.

### Discussion prompt

When you look at your array and its index positions, how do you think zero-based indexing influences the way you organize and access data? Can you think of a real-life situation where counting from zero (instead of one) would be helpful, or where it might trip someone up? Let’s discuss some examples together.