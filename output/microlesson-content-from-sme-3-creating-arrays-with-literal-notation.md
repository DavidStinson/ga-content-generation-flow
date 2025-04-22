# Creating Arrays with Literal Notation

**Learning Objective:** Create arrays using JavaScript literal notation.

## Syntax for array literal notation

Let’s expand on what we’ve already learned about arrays. In earlier lessons, you saw how JavaScript uses arrays to organize groups of data, like a row of mailboxes where each spot holds a value.

The most common and straightforward way to create a new array in JavaScript is with **array literal notation**. This simply means writing out the array directly, listing its values between square brackets (`[` and `]`), and separating each value with a comma.

Here’s what the syntax looks like:

```javascript
let colors = ["red", "green", "blue"];
```

Let’s break this down:
- The `let` keyword starts a new variable, just like with any JavaScript value.
- The variable name `colors` can be anything you want, as long as you follow JavaScript’s rules for naming.
- The array itself is created using the square brackets. Inside, each value (like `"red"`, `"green"`, `"blue"`) is separated by a comma.

This form of **literal notation** is popular because it’s simple, quick, and clear for both short and long lists.

### Key points to remember
- Arrays always use square brackets `[ ]`.
- Elements (the data items) are separated by commas.
- You can declare an array with `let` or `const`. Use `const` if you don’t plan to reassign the variable to a whole new array.

## Creating arrays with different data types

While many of your first examples will have arrays filled with strings or numbers, JavaScript is flexible. Arrays can hold any data type—even mixed types! This includes strings, numbers, booleans (`true` or `false`), and even other arrays or objects.

Here are some examples:

**Array of numbers:**

```javascript
let ages = [22, 34, 28, 41];
```

**Array of strings:**

```javascript
let pets = ["cat", "dog", "hamster"];
```

**Array with mixed data types:**

```javascript
let randomThings = [42, "hello", true, null];
```

**Array with objects or arrays inside (advanced):**

```javascript
let nestedArray = [[1, 2], [3, 4]];
let personDetails = ["Sam", 31, true];
```

In real-world code, it’s usually best to keep arrays filled with similar types of information, especially as you build more complex programs. But knowing that JavaScript arrays can be flexible is helpful when you want to experiment.

## Empty arrays and their uses

You don’t always know all the items you want in your array when you start. You might want to add values later, such as collecting answers from a user or gathering a list one item at a time.

JavaScript lets you create an empty array using literal notation—just use square brackets with nothing inside:

```javascript
let emptyList = [];
```

This creates an array with zero elements. You can add items to it using array methods (like `.push()`), which you’ll see in practice as you code.

**Common uses for empty arrays:**  
- Storing user inputs as they come in (imagine a registration form or poll responses)
- Setting up a “to-do” list that grows as tasks are added
- Collecting data inside a loop or function

Here’s an example of adding to an empty array:

```javascript
let numbers = [];
numbers.push(5);
numbers.push(10);
console.log(numbers); // Output: [5, 10]
```

## Practical examples of array creation

Let’s connect array literal notation to tangible, real-life scenarios:

**Example 1: To-do list**

You want to keep track of some tasks you need to complete today.

```javascript
let todoList = ["Check email", "Attend team meeting", "Write report"];
```

**Example 2: Favorite movies**

Suppose you want to store the titles of movies you love.

```javascript
let favoriteMovies = ["Inception", "The Matrix", "Finding Nemo"];
```

**Example 3: Collecting survey answers**

You’re building a survey and want to put each person’s response into an array as they answer.

```javascript
let responses = [];
// As people reply, you add their responses:
responses.push("Yes");
responses.push("No");
console.log(responses); // Output: ["Yes", "No"]
```

The power of literal notation is its simplicity. You can see all your data at a glance, set up new arrays quickly, and build flexible structures to store whatever you need.

## Activity: Hands-on with array literal notation

Now it’s your turn to get comfortable with creating arrays. This solo exercise will help reinforce how array literal notation works.

### Instructions

1. **Open your code editor or sandbox**  
   Use your preferred code editor, or try an online JavaScript environment like repl.it or JSFiddle.

2. **Create an array of your top three travel destinations**  
   - Think of three places you’d love to visit.
   - Use array literal notation to create an array named `travelDestinations` containing those three places as strings.
   - Example:  
     ```javascript
     let travelDestinations = ["Paris", "Tokyo", "New York"];
     ```

3. **Print your array to the console**  
   - Use `console.log()` to display your entire `travelDestinations` array.

4. **Create an empty array for future trips**  
   - Declare an empty array called `futureTrips`.
   - Use `console.log()` to print it and confirm it’s empty.

5. **Add a destination to your empty array**  
   - Use the `.push()` method to add a new place to `futureTrips`.
   - Print `futureTrips` again to see how it’s updated.

6. **Deliverable**  
   - Your final code should include:
     - The array of your top three destinations
     - The empty `futureTrips` array
     - At least one example of adding a new item and printing the result
   - Post your code snippet (or a screenshot of your output) to the class discussion board or share with your group.

### Discussion prompt

When might you want to start with an empty array instead of one filled with items? How could an empty array be useful in a real-world application you use or would like to create—for example, planning a trip, shopping online, or collecting survey answers? Share your ideas with your learning group and discuss different scenarios where starting with an empty array makes your program more flexible or user-friendly.