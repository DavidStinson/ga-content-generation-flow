# Creating Arrays in JavaScript

**Learning Objective:** Create arrays using JavaScript literal notation.

## Introduction to array literal notation

In programming, a common task is to work with lists or collections of items—like a list of numbers, words, or objects. In JavaScript, we use something called an array to keep these items together in a single, ordered group.

To create an array in JavaScript, one of the easiest and most popular ways is called "literal notation." Literal notation is a way of writing out the exact values you want in your array, right there in your code, using special bracket symbols. This method is simple, readable, and widely used.

Think of an array as a row of boxes, each holding a value, and all lined up next to each other. The values may be numbers, words (strings), or even a mix. We'll focus on how to create these rows of item-containing boxes, using literal notation.

## Syntax for creating empty arrays

Sometimes you want to start with an empty array—meaning, no items inside—maybe because you'll add items later in your program. Creating an empty array is straightforward.

Here's what that looks like in code:

```javascript
let emptyArray = [];
```

Let's break this down:
- `let` is a keyword we use to create a new variable in JavaScript.
- `emptyArray` is the name we’ve chosen for this variable. You can choose any name that makes sense for your data.
- The `[]` are square brackets, and together, they tell JavaScript, “Hey, make an array!”
- Since there’s nothing between the brackets, this is an empty array.

You might want to create an empty array if you plan to fill it later as your program runs—like creating a shopping cart and then letting users add items one by one.

## Creating arrays with initial values

You can also start your array by putting some values in it right away. With literal notation, you list the values you want, one after another, separated by commas, all inside the square brackets.

Here's an example:

```javascript
let colors = ['red', 'blue', 'green'];
```

- This creates an array named `colors` that holds three items: the string values `'red'`, `'blue'`, and `'green'`.
- Each value in an array has a specific order, starting with 0. So in this example, `'red'` is at position 0, `'blue'` is at position 1, and `'green'` is at position 2.

Arrays can also hold other types of values, not just strings. For example:

```javascript
let numbers = [2, 4, 6, 8];
```

Or even a mix:

```javascript
let mixedArray = ['hello', 7, true];
```

Notice that we use commas to separate different items in the array, and all items stay inside the square brackets.

## Hands-on coding: Creating various arrays in Visual Studio Code

Let’s bring it all together by practicing in Visual Studio Code, a popular code editor often used for writing JavaScript.

### Activity: Create your own arrays

Let's get hands-on with creating arrays. We'll work on a short exercise to help you practice using JavaScript literal notation in Visual Studio Code.

#### Step-by-step instructions

1. **Open Visual Studio Code.**  
   If you don't have Visual Studio Code installed, download it from [code.visualstudio.com](https://code.visualstudio.com/). Open the application.

2. **Create a new file and name it `arraysPractice.js`.**

3. **Write code to create the following:**
    - An empty array called `myList`.
    - An array called `fruits` containing three fruit names (for example, `'apple'`, `'banana'`, `'orange'`).
    - An array called `luckyNumbers` with four numbers of your choice.
    - An array called `favorites` with at least one string, one number, and one boolean value (e.g., `['pizza', 42, false]`).

    Example:

    ```javascript
    let myList = [];
    let fruits = ['apple', 'banana', 'orange'];
    let luckyNumbers = [7, 12, 22, 99];
    let favorites = ['pizza', 42, false];
    ```

4. **Save your file.**

5. **Run your code (optional):**  
   If you'd like, open the terminal in Visual Studio Code and type:
   ```
   node arraysPractice.js
   ```
   This step will run your code, but since it only creates arrays and does not output anything yet, you won't see any messages. That’s okay! The main goal here is to practice declaring arrays.

6. **Share your results:**  
   Copy and paste your array code into the class chat or discussion board.

#### Deliverable

Post your array code to the class discussion area.

#### Discussion prompt

Take a look at the arrays your classmates posted.  
- What similarities or differences do you notice in the way arrays were created?
- Did anyone include a mix of data types in their array, or did they stick to one type?
- Why might it be helpful to use arrays in your own programs, even for simple tasks?

Let's discuss together how arrays might make it easier to handle groups of related data as we build more complex programs.