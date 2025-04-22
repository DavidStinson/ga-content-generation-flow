# Creating arrays with literal notation

**Learning Objective:** Create arrays using JavaScript literal notation.

## Syntax for array literal notation

So far, you’ve learned that arrays are like organizers for groups of information, similar to a row of cubbyholes or storage boxes—each box holds an item, all together in one neat row.

The most common way to create an array in JavaScript is with *array literal notation*. This means writing the array directly into your code, placing your values inside square brackets (`[ ]`), separated by commas.

Here’s what that looks like:

```javascript
let colors = ['red', 'green', 'blue'];
```

Let’s break this down step by step:

- The `let` keyword declares a new variable (a named container for your data).
- The variable name `colors` describes what the array will store.
- The square brackets define the array. Each value inside (like `'red'`, `'green'`, and `'blue'`) is called an *element*, and elements are separated by commas.

> 📚 An *element* is an individual item stored at a specific position in an array.

tktk asset: Visual showing a row of labeled boxes, each representing an array element inside square brackets.

### Key points to remember

- Arrays are defined with square brackets `[ ]`.
- Elements in the array are separated by commas.
- You can use either `let` or `const` to declare an array. Use `const` if the variable will not be reassigned to a different array.

> 🏆 Best practice: Pick clear, descriptive names for your arrays so you (and others) will quickly understand what each group of data represents.

## Creating arrays with different data types

You might notice that arrays aren’t limited to only words (strings). JavaScript arrays can hold any type of value—even mixing different types in one array. This flexibility helps you experiment and solve a variety of challenges.

Here are some practical examples:

**Array of numbers**

```javascript
let ages = [22, 34, 28, 41];
```

**Array of strings**

```javascript
let pets = ['cat', 'bird', 'hamster'];
```

**Array with mixed data types**

```javascript
let randomThings = [42, 'hello', true, null];
```

**Arrays containing other arrays or objects (for advanced use cases)**

```javascript
let nestedArray = [['apple', 'banana'], ['carrot', 'pea']];
let personDetails = ['Amira', 29, false];
```

> 💡 While it’s possible to mix data types in a single array, in most programs, it’s best to store similar kinds of information together to keep your code clean and easy to work with.

tktk asset: Diagram showing side-by-side arrays with numbers, strings, and a mixed array, highlighting the different element types.

## Empty arrays and their uses

Often when building programs, you might not know every item your array should hold right away. You might need to collect data from users, or grow a list over time as your program runs.

To do this, you can start with an *empty array* using literal notation—just two square brackets with nothing inside:

```javascript
let emptyList = [];
```

> 📚 An *empty array* is an array with zero elements, ready to have items added later.

You can add elements to your array as your program runs. For example:

```javascript
let numbers = [];
numbers.push(5);
numbers.push(10);
console.log(numbers);
// Prints: [5, 10]
```

> 💡 The `.push()` method adds a new element to the end of an array.

**Real-world uses for empty arrays:**

- Collecting user responses over time (like survey answers or registrations)
- Building a task list as new tasks arrive
- Tracking items added to a shopping cart

tktk asset: Side-by-side code-to-concept visual showing an empty array that grows as elements are added via `.push()`.

## Practical examples of array creation

Let’s look at a few scenarios you might encounter in day-to-day life or work:

**Example 1: To-do list**

Suppose you want to make a checklist of tasks for the day.

```javascript
let todoList = ['Check messages', 'Plan schedule', 'Write summary'];
```

**Example 2: List of favorite movies**

Imagine keeping a simple catalog of films you enjoy.

```javascript
let favoriteMovies = ['Song of the Sea', 'Spirited Away', 'The Lunchbox'];
```

**Example 3: Collecting survey answers**

If you’re building a quick survey, you may want to store each person’s answer as they respond.

```javascript
let responses = [];
responses.push('Yes');
responses.push('No');
console.log(responses);
// Prints: ['Yes', 'No']
```

> 💡 Arrays, especially those created with literal notation, are your digital notepads—flexible, organized, and always ready for new data.

tktk asset: Three simple scenario cards (to-do, movies, survey) with matching code snippets and real-life visuals.

## Activity: Hands-on with array literal notation

### Purpose

Practice creating arrays using literal notation, adding to arrays, and connecting code to relatable, real-world ideas. This helps you become comfortable using one of JavaScript’s most common data structures.

### Instructions

1. **Open your code editor**

   - Use Visual Studio Code or an online JavaScript editor such as repl.it or JSFiddle.

   tktk asset: Screenshot highlighting how to open a new JavaScript file in Visual Studio Code.

2. **Create an array of your top three travel destinations**

   - Think of three places you would love to visit from anywhere in the world.
   - Use array literal notation to create an array named `travelDestinations`, placing each destination as a string.

   Example:

   ```javascript
   let travelDestinations = ['Cairo', 'Rio de Janeiro', 'Kyoto'];
   ```

3. **Print your array to the console**

   - Use `console.log()` to show your `travelDestinations` array.

   ```javascript
   console.log(travelDestinations);
   // Prints: ['Cairo', 'Rio de Janeiro', 'Kyoto']
   ```

4. **Create an empty array for future trips**

   - Declare an empty array named `futureTrips`.
   - Print it to confirm it is empty.

   ```javascript
   let futureTrips = [];
   console.log(futureTrips);
   // Prints: []
   ```

5. **Add a destination to your empty array**

   - Use the `.push()` method to add a new place to `futureTrips`.
   - Print `futureTrips` again to watch it change.

   ```javascript
   futureTrips.push('Seoul');
   console.log(futureTrips);
   // Prints: ['Seoul']
   ```

6. **Deliverable**

   - Share your code snippet (or a screenshot of your code and output) with your learning group.

> 🏆 Best practice: Use personal and diverse examples for your arrays, reflecting interests, backgrounds, or places that inspire you.

## Discussion prompt

When would you want to start with an empty array rather than one filled with items? Share ways an empty array is useful for a real-world application you use or would like to create—for example, trip planning, a shopping cart for online purchases, or storing responses to a quiz. Share your thoughts with your group and discuss how empty arrays make programs more adaptable and user-friendly.

tktk asset: Discussion forum screenshot or sample group discussion slide with “When and why to use empty arrays?” at the top.

## Knowledge checks

**Question 1:**  
Which of the following is the correct way to create an array of fruits using literal notation?

- A) `let fruits = 'apple', 'banana', 'kiwi';`
- B) `let fruits = ["apple", "banana", "kiwi"];`
- C) `let fruits = ('apple', 'banana', 'kiwi');`
- D) `let fruits = { 'apple', 'banana', 'kiwi' };`

**Question 2:**  
What is the result of running this code?

```javascript
let responses = [];
responses.push('Yes');
responses.push('No');
console.log(responses);
```

- A) `['Yes', 'No']`
- B) `'Yes', 'No'`
- C) `[[], ['Yes', 'No']]`
- D) `['No', 'Yes']`

## Instructor guide

**Delivery tips:**

- Use examples and scenarios that connect to a wide variety of cultural backgrounds, hobbies, and interests to ensure all learners feel represented.
- Guide learners to use array names and elements that are meaningful to them, reinforcing the idea that array data can reflect their actual goals and experiences.
- Visually demonstrate how arrays grow when using `.push()`, either through live coding or by referencing provided visuals.
- For the activity, invite sharing of code snippets and encourage peer feedback during the discussion prompt.

**Knowledge check answers:**

1. B) `let fruits = ["apple", "banana", "kiwi"];`
2. A) `['Yes', 'No']`

**Suggested solution to the activity:**

```javascript
let travelDestinations = ['Cairo', 'Rio de Janeiro', 'Kyoto'];
console.log(travelDestinations);
// Prints: ['Cairo', 'Rio de Janeiro', 'Kyoto']

let futureTrips = [];
console.log(futureTrips);
// Prints: []

futureTrips.push('Seoul');
console.log(futureTrips);
// Prints: ['Seoul']
```

---

## Reasoning for Changes

1. **Formatting and structure:**  
   - Headings, spacing, and callouts were reformatted to align with the Markdown Document Structure guidelines, enhancing readability and ensuring slide conversion readiness.

2. **Expanded narrative and practical connections:**  
   - Added introductory analogies (storage boxes, notepads) to reinforce concepts in a globally relatable way.
   - Practical examples were made more diverse, using city and film names from multiple regions to avoid region-specific references.
   - Encouraged personal relevance in activity prompts to deepen engagement and inclusion.

3. **Explicit definitions and terminology:**  
   - Introduced concise callouts to define *element* and *empty array* for learners without prior coding experience, per Technical Voice guidance.

4. **Global inclusivity:**  
   - Array and variable names, as well as sample content, were chosen for global resonance (e.g., omitting regionally charged city names, avoiding restricted themes such as dogs or pork).
   - No culturally specific language, idioms, or region-centric analogies were used, as per GA Inclusivity Guidelines.

5. **Clarity in code and comments:**  
   - All code blocks use single quotes for strings in line with JavaScript best practices, except where `" "` might appear in a knowledge check, matching correct output expectations.
   - Code snippets include comments showing expected output, using the "Prints:" convention.
   - Names and examples encourage brevity and inclusivity per Crafting Modular Code.

6. **Alignment with learning objectives:**  
   - All narrative and activities directly reinforce the objective: understanding and using JavaScript array literal notation in practical scenarios.

7. **Activity redesign:**  
   - Steps were clearly broken down with purposeful, location-neutral instructions referencing Visual Studio Code and accessible online editors, supporting both in-person and remote learners.
   - Instructions were structured to follow the Exercise Instruction Guidelines, detailing purpose, expected deliverables, and step-by-step breakdown.

8. **Asset suggestions:**  
   - Embedded "tktk asset" markers at relevant points to suggest visuals that reinforce learning and support both instructor delivery and visual learners.

9. **Strategic interaction:**  
   - Activity and discussion prompts placed to facilitate group engagement and reflection, drawing connections to real-world applications.

10. **Knowledge checks:**  
    - Multiple-choice questions test key concepts of array literal syntax and the use of `.push()` in a globally understandable way, per GA Learning Philosophy and Technical Voice.

11. **Instructor guide:**  
    - Expanded with facilitation strategies that encourage personal relevance and inclusivity, as well as practical delivery tips and clearly marked knowledge check answers.

These changes preserve technical accuracy, build narrative context, and provide a richer, more engaging experience that centers learner understanding, confidence, and practical application.
