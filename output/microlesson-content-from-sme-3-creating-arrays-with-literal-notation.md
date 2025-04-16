# Creating Arrays with Literal Notation

## Learning Objective

By the end of this microlesson, you will be able to create arrays using JavaScript literal notation.

---

## Understanding array literal notation

In JavaScript, an **array literal** is the most direct and widely used way to create an array. The word "literal" here means you write the array directly as it will appear in your code, using clear and easy-to-read syntax. You surround your list of items with square brackets `[ ]` and separate each item with a comma. This helps JavaScript know you are creating an array and what items should go inside it.

**Example:**

```javascript
let shoppingList = ["bread", "milk", "eggs"];
```

Here, you are telling JavaScript: “Make an array called `shoppingList` that keeps track of bread, milk, and eggs.”

### Key features of array literal notation

- Arrays are written between square brackets: `[ ]`
- Each value inside is called an **element**
- Elements are separated by commas: `value1, value2, value3`
- Array elements can be of any data type: numbers, strings, or even other arrays!

**Why use literal notation?**

Literal notation is concise, easy to read, and helps you visualize the data you are grouping together—much like writing a shopping list or a collection of favorite movies on paper.

---

## Creating arrays with different data types

Arrays in JavaScript are flexible—they can hold almost any type of data, and you can mix different types in a single array if you need to (though usually, arrays contain similar items for better organization).

### Arrays of strings

Strings are text values, often surrounded by quotes.

```javascript
let fruits = ["apple", "banana", "cherry"];
```

### Arrays of numbers

Perfect for lists like ages, prices, or rankings.

```javascript
let lotteryNumbers = [7, 14, 21, 28, 35];
```

### Arrays of mixed data types

Although less common for most real situations, JavaScript lets you do it.

```javascript
let mixedArray = ["dog", 3, true, null];
```

In `mixedArray`, we have:
- A string (`"dog"`)
- A number (`3`)
- A boolean (`true`)
- A special value (`null`—which means “no value”)

### Arrays of arrays (nested arrays)

You can create arrays that have other arrays inside. This is helpful for representing more complex data, like a grid or a table.

```javascript
let teams = [
  ["Maria", "John"],
  ["Luis", "Fatima"]
];
```

Here, `teams` contains two arrays—each representing a team.

---

## Guided practice: Creating various arrays in Visual Studio Code

Now that you have seen examples, it is time to put the concepts into action and build your confidence with hands-on practice. If you don’t have Visual Studio Code installed, you can use any online playground like repl.it or JSFiddle.

**Let’s get started by walking through a few scenarios.**

### Example 1: An array of favorite sports

```javascript
let favoriteSports = ["soccer", "tennis", "basketball"];
console.log(favoriteSports);
```

**What happens here?**  
You have created a variable called `favoriteSports`, which contains three string elements. The console will show the entire array.

### Example 2: An array of ages

```javascript
let ages = [25, 38, 42, 19];
console.log(ages);
```

**What happens here?**  
Now, the variable `ages` contains four number elements. Once again, logging the array prints all the numbers at once.

### Example 3: An array that mixes types

```javascript
let sampleList = ["hello", 2024, false, null];
console.log(sampleList);
```

**What happens here?**  
This array contains a string, a number, a boolean, and a null value all in the same array.

### What can you notice?

- Arrays make grouping, storing, and later retrieving related data much easier.
- Literal notation is quick and visual—just use square brackets and commas.
- Elements can be any JavaScript data type.

---

## Activity: Hands-on practice creating arrays in JavaScript

Now it’s your turn to create new arrays using literal notation and see your results in action.

### Step-by-step instructions

1. **Choose three different categories for arrays**  
   For example:  
   - Types of pets  
   - Lucky numbers  
   - Breakfast menu items

2. **In Visual Studio Code (or an online playground), create one array for each category:**  
   - Each array should use literal notation: `[item1, item2, item3]`
   - Give each array a clear, descriptive variable name  
   - Examples:
     ```javascript
     let pets = ["cat", "dog", "fish"];
     let luckyNumbers = [3, 8, 11];
     let breakfastMenu = ["pancakes", "coffee", "orange juice"];
     ```

3. **Print each array to the console:**  
    ```javascript
    console.log(pets);
    console.log(luckyNumbers);
    console.log(breakfastMenu);
    ```

4. **Create a new mixed data type array:**  
   - Pick a variable name (for example, `surpriseArray`)
   - Mix at least one string, one number, and one boolean value
   - Print it to the console
     ```javascript
     let surpriseArray = ["goal", 10, true];
     console.log(surpriseArray);
     ```

5. **Deliverable:**  
   - Post your code for all four arrays and the console output to the class chat, discussion board, or your instructor.  
   - Briefly explain how you decided what to name your variables and what elements you included in each array.

---

### Discussion prompt

Reflect on your experience:

- How did creating arrays with literal notation compare to how you might have stored separate variables for each value?
- Did you find it helpful to be able to store different data types in a single list? Why or why not?
- Looking at your arrays, can you imagine a web or app scenario where organizing data in arrays would be useful? (For example: managing a shopping cart, storing user preferences, or keeping track of scores)

Share your answers with the group and read a classmate’s reflections. Is there an example you hadn’t considered before? How might their approach to naming arrays or choosing elements help organize information in a professional or personal project?

---

Congratulations! By practicing array creation using literal notation, you have built an essential foundation for working with lists of data in JavaScript. Next, you'll learn how to access and modify elements in your arrays, opening the door to dynamic data management in your programs.