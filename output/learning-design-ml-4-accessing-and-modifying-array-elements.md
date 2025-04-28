# Accessing and Modifying Array Elements

**Learning Objective:** Access and modify elements within an array using square brackets.

## Using square bracket notation to access elements

Arrays store ordered collections of values, which can be anything from numbers and strings to even other arrays. To make the most of arrays in JavaScript, you need to know how to access the data they hold. We do this using *square bracket notation*.

Every item in an array is stored at a position, which is called an *index*. In programming, it is common for the first position to be at index `0`. This means the first item is at index `0`, the second at index `1`, and so forth.

> 📚 The *index* is the position of an item in the array, starting with `0` for the first item.

Here is an example of a simple array that stores fruits:

```javascript
let fruits = ['apple', 'banana', 'cherry', 'date'];
```

To get the first fruit from the array, use its index:

```javascript
console.log(fruits[0]);
// Prints: 'apple'
```

To access the third fruit:

```javascript
console.log(fruits[2]);
// Prints: 'cherry'
```

> 💡 Think of an array as a row of boxes, each with a number starting at `0` on its label. To find what is in the box, open the box with the number that matches the position you want.

When you try to access an index that does not exist (for example, `fruits[10]`), JavaScript will give you a result of `undefined`. This means there is no item at that position in the array.

tktk asset: Illustration showing an array as a row of boxes labeled 0, 1, 2, 3, each containing a different fruit. The fifth and sixth boxes are empty to visualize `undefined` when accessing beyond the array's length.

## Modifying existing array elements

You can also use square bracket notation to change, or *modify*, an existing item in an array. This is done using an assignment operator (`=`).

Suppose you want to change `'banana'` to `'blueberry'` in our `fruits` array:

```javascript
fruits[1] = 'blueberry';
console.log(fruits);
// Prints: ['apple', 'blueberry', 'cherry', 'date']
```

Here, you access the position where `'banana'` is stored (index `1`) and assign a new value to that position.

You can also change the last fruit in the array:

```javascript
fruits[3] = 'dragonfruit';
console.log(fruits);
// Prints: ['apple', 'blueberry', 'cherry', 'dragonfruit']
```

> 💡 Imagine updating an item in a shopping list: Instead of rewriting the whole list, you only change one item. Arrays in JavaScript work the same way; you update just the spot you want.

> 🧠 Modifying an array updates the original array itself. Other elements remain untouched.

## Common pitfalls when accessing/modifying arrays

Square bracket notation is powerful, but a few frequent mistakes can lead to bugs. Let us look at these and how to avoid them.

### Off-by-one errors

Because arrays begin counting at zero, it is easy to miscount and accidentally access the wrong element. For example, the second item is at index `1`.

```javascript
console.log(fruits[0]); // First item: 'apple'
console.log(fruits[1]); // Second item: 'blueberry'
```

### Using indexes that don’t exist

If you try to read from, or write to, an index past the array’s length, JavaScript will not give an error, but you may get `undefined`, or unintentionally create empty slots:

```javascript
console.log(fruits[10]); 
// Prints: undefined

fruits[6] = 'kiwi';
console.log(fruits);
// Prints: ['apple', 'blueberry', 'cherry', 'dragonfruit', undefined, undefined, 'kiwi']
```

Notice how spaces 4 and 5 are now empty (`undefined`). This can make your data harder to handle.

> ⚠ Be careful when setting values at indexes beyond the current array length; you may accidentally introduce empty elements, which can cause problems when processing your data later.

### Assignment vs. reference

When you assign a new value to an element in an array, only that element changes. The others remain as they are. Also, arrays in JavaScript are a type of *object*—modifying the array updates it directly.

> 📚 A JavaScript *object* is a special data structure that can store collections of data and more complex entities.

## Demonstration: Accessing and modifying arrays in Visual Studio Code

Let us walk through a real-world workflow using Visual Studio Code, a widely used code editor. Here you will create an array, access its elements, and make some changes.

1. Open Visual Studio Code and create a new file named <code class="filepath">arrays-demo.js</code>.
2. Enter this code to define an array of colors:

   <code class="filepath">arrays-demo.js</code>
   ```javascript
   let colors = ['red', 'green', 'blue', 'yellow'];
   ```

3. Access the second color and print it:

   ```javascript
   console.log(colors[1]);
   // Prints: 'green'
   ```

4. Change `'yellow'` to `'orange'`:

   ```javascript
   colors[3] = 'orange';
   console.log(colors);
   // Prints: ['red', 'green', 'blue', 'orange']
   ```

5. Try to access an element beyond the array’s length:

   ```javascript
   console.log(colors[10]);
   // Prints: undefined
   ```

6. Save your file and run it using Node.js:

   ```
   node arrays-demo.js
   ```

tktk asset: Screenshot sequence of Visual Studio Code showing how to enter the code and view the output in a terminal.

> 💡 Each step helps you see instantly how arrays can be updated and queried, just like making quick changes in a list or spreadsheet.

## Activity: Manipulating array data based on given instructions

Now it is your turn to practice what you have learned—just like you might edit a list of contacts on your phone, or update available products in an online shop.

tktk asset: Sample output screenshot showing a `playlist` array and changes highlighted.

### Instructions

- Open a new file in Visual Studio Code called <code class="filepath">playlist.js</code>.
- At the top of the file, create an array named `playlist` with these five song names (as strings): `'Shape of You'`, `'Uptown Funk'`, `'Despacito'`, `'Blinding Lights'`, and `'Bad Guy'`.

- Using `console.log`, print the third song in your array.

- Change the fifth song in the array from `'Bad Guy'` to `'Levitating'`.

- Print the entire `playlist` array to view the update.

- Try to access an index that does not exist in the array (for example, index `10`). Print the result.

- Save and run the file using Node.js in your terminal.

#### Deliverable

Copy and paste your final code and the output from running it into the learning platform’s chat or your designated classroom discussion board.

tktk asset: Downloadable starter code for <code class="filepath">playlist.js</code>.

### Discussion prompt

Arrays help organize and update groups of related values efficiently. Think about a daily scenario where you need to quickly update a single item in a list—such as correcting a delivery address in an online order system, or changing the seat assignment in an event booking. Share an example in the chat or be ready to discuss why fast, direct updates to a collection matter in software you use or build.

## Knowledge check

1. What index would you use to access the fourth element in an array?
   - A) 4
   - B) 3
   - C) 0
   - D) The last element

2. What happens if you assign a value to an index beyond the end of the array?
   - A) JavaScript will throw an error
   - B) The array will fill any skipped positions with `undefined`
   - C) It overwrites the last element in the array
   - D) The assignment will be ignored

---

## Instructor guide

- **Best practices for delivery:**
  - Use visuals and analogies to reinforce the zero-based indexing concept.
  - Encourage learners to narrate their thought process when accessing or updating elements.
  - Highlight array mutations in real time by modifying variables in live code.
  - Emphasize practical scenarios (such as editing a contact list) for real-world connection.
  - Remind learners to watch for `undefined` values and the consequences of skipping elements.
- **Remote adaptation:** Prompt students to share their code or outputs via chat or screen share for immediate feedback.

- **Answers to knowledge checks:**
  - 1: B) 3
  - 2: B) The array will fill any skipped positions with `undefined`

- **Suggested solution to the activity:**

  <code class="filepath">playlist.js</code>
  ```javascript
  let playlist = ['Shape of You', 'Uptown Funk', 'Despacito', 'Blinding Lights', 'Bad Guy'];

  console.log(playlist[2]);
  // Prints: 'Despacito'

  playlist[4] = 'Levitating';

  console.log(playlist);
  // Prints: ['Shape of You', 'Uptown Funk', 'Despacito', 'Blinding Lights', 'Levitating']

  console.log(playlist[10]);
  // Prints: undefined
  ```

---

## Reasoning for Changes

- **Explanations and definitions:** Clarified terms like *index* and *object* using in-line callouts for better comprehension, especially for beginners new to programming concepts.
- **Analogy and relatable narrative:** Used the “row of boxes/shopping list” and “contact list” analogies to make array access and updates concrete and relatable for global learners.
- **Formatting revision:** Adjusted headings and included blank lines for clarity per markdown guidelines. Calls out code file paths before relevant blocks for easy conversion to slides.
- **Practicality and application:** Maintained a strong connection to learners’ daily experiences and focused activity prompts on scenarios relevant worldwide.
- **Inclusive code samples:** Chose neutral, globally popular song names for the activity array.
- **Clear impacts of mistakes:** Highlighted consequences of common pitfalls (such as `undefined` values and off-by-one errors) in beginner-friendly callouts.
- **Interaction opportunities:** Added a discussion prompt directly connecting back to typical real-world list updating, supporting collaborative conversation or chat.
- **Asset suggestions:** Placed tktk asset notes for slide designers to create supporting visuals, code demos, and screenshots. These anchor the lesson content for visual learners and help bridge abstract concepts.
- **Knowledge checks:** Embedded short, culturally neutral multiple choice checks to reinforce understanding and apply the lesson in a low-stakes fashion.
- **Instructor guidance:** Provided facilitation notes for remote and live delivery, addressing potential confusions and suggesting real-time feedback methods.
- **Modular build:** Deliberately avoided references to other lessons; instead layered on concepts stepwise, establishing independence.
- **Cultural neutrality:** Avoided American or regional idioms, and examples are universally accessible. All code and context are globally relevant.

This approach transforms the original technical draft into an accessible, modular, and engaging learning experience aligned with General Assembly’s philosophy and documentation standards, without diluting the technical rigor necessary for understanding JavaScript arrays.