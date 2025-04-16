# Creating Arrays

**Learning Objective:**  
Create arrays using JavaScript literal notation.

---

## Array literal notation syntax

Arrays are a foundational way to organize lists of related information in JavaScript. The easiest and most common way to create an array is by using **literal notation** — a special syntax that uses square brackets `[]`.

When you use array literal notation, you create a new array by simply listing the items (called **elements**) you want inside the square brackets, separated by commas. You can also use this notation to create an array that starts out empty and add items later.

**Example: Creating an array with values**

```javascript
let colors = ["red", "green", "blue"];
```

In this example:
- `colors` is a variable that stores the array.
- The array is created using square brackets.
- The elements inside the array are `"red"`, `"green"`, and `"blue"`, separated by commas.

**Example: Using an array in a practical context**

Imagine you want to keep track of your favorite types of music:

```javascript
let favoriteGenres = ["rock", "jazz", "classical", "pop"];
```

Now you have a single, organized variable holding all your favorite genres.

**How to read the syntax**

- Square brackets `[]` mean "I'm making an array."
- Each value inside the brackets (an element) is separated by a comma.
- Elements can be words (strings, in quotes), numbers, or even a mix, but it’s common to keep similar types together for simplicity.

---

## Creating empty arrays

Sometimes, you know you want an array, but you’re not sure what should go into it yet. In this case, you can create an **empty array** and fill it later.

**Syntax for an empty array**

```javascript
let todoList = [];
```

- Here, `todoList` is an array, but it starts out with zero elements inside.
- You can add data (elements) to the array later as your program needs them.

**When would you use an empty array?**

- Collecting responses to a survey as users submit them.
- Building a list of tasks as you plan your day.
- Storing items added to a cart in an online store.

**Analogy:**  
Think of an empty array like an empty egg carton. You aren't sure which eggs you'll add, but you've set up the carton to hold them.

---

## Initializing arrays with values

Often, you’ll know some or all of the values you want an array to have as soon as you create it. In this case, you can **initialize** your array with values right from the start.

**Syntax example:**

```javascript
let groceryList = ["milk", "eggs", "bread", "cheese"];
```

**Key points:**
- The array is ready to use with values already inside.
- The order matters: `"milk"` is the first item (at index 0), `"cheese"` is the last (at index 3).

**Initializing with different data types**

You can also mix data types, though it’s best for simplicity and clarity to stick with a single type (like all strings or all numbers) at first.

```javascript
let mixedArray = ["hello", 42, true];
```

- `"hello"` is a string,
- `42` is a number,
- `true` is a boolean value.

For most beginner projects, sticking to one type per array makes your code easier to read and use.

**Practical Example:**

You want to list the days of the week to build a simple calendar app:

```javascript
let daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
```

Now, you have all the day names stored in order, and you can easily access them when building your application.

---

## Activity: Build and share your own array

Let's practice creating arrays using literal notation and reinforcing the syntax you'll use regularly as a JavaScript developer.

### Solo Exercise: Your Personal Reading List

1. **Think of three books you want to read or have enjoyed recently.**
    - If books aren’t your thing, pick another category like movies, places to visit, or favorite meals.
2. **Create a JavaScript array using array literal notation to store these three items.**
    - Example:
      ```javascript
      let readingList = ["The Great Gatsby", "Sapiens", "Atomic Habits"];
      ```
3. **Now create an empty array for things you want to add later.**
    - Example:
      ```javascript
      let futureReads = [];
      ```
4. **Write down both arrays (with and without initial values).**
    - Make sure to use the proper syntax: square brackets for arrays, double quotes for string values, and commas to separate elements.
5. **Deliverable:**
    - Post your completed arrays in the class chat or discussion forum.
    - For example:
      ```
      My readingList array: ["The Great Gatsby", "Sapiens", "Atomic Habits"]
      My futureReads array: []
      ```
    - Explain what you might use the empty array for in your own words.
6. **Optional:**  
   Try initializing an array with different data types just to see what happens, even though you’ll usually stick to one type.

---

### Discussion prompt

Arrays help us organize information before we even know what that information fully is—for example, setting up an empty list for user input or future plans.  
**Reflect and discuss:** Can you think of a real-life scenario where you would need to prepare a list without knowing what will go in it yet (like setting out bins for recycling before knowing what you’ll throw away)? How could using an empty array in a JavaScript program help you stay organized or make your job easier in that scenario? Share your thoughts in the group and consider how this capability might simplify your daily work or hobbies.

---

By practicing the steps above, you’ll become comfortable with creating both empty arrays and arrays initialized with values using literal notation—the essential first step in working with array data in JavaScript.