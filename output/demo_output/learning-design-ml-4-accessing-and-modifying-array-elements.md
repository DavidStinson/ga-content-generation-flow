# Accessing and Modifying Array Elements

**Learning Objective:** Access and modify elements within an array using square brackets.

## Using square bracket notation to access elements

In earlier microlessons, we explored the basics of JavaScript arrays and how to create them. Now, let’s build on that foundation by learning how to access and modify values stored inside an array.

To access a specific *element* (an individual value) in a JavaScript array, you use *square bracket notation*. This simply means writing the name of your array, followed right away by a pair of square brackets. Inside the brackets, put the *index* (position number) of the element you want.

Remember: JavaScript arrays start counting from zero. So, the first element is at position 0, the second at position 1, and so on.

> 📚 An *index* is the unique position of an element in an array, always starting from zero.

Here is what it looks like in practice:

```javascript
let fruits = ['apple', 'banana', 'cherry', 'date'];
console.log(fruits[0]); // Prints: apple
console.log(fruits[2]); // Prints: cherry
```

Imagine a row of mailboxes, each with a number beneath. When you write `fruits[2]`, you are saying, “Show me what’s in the mailbox numbered 2.” Because counting begins at zero, this fetches the third item, which is `'cherry'`.

tktk asset: Visual of a row of numbered mailboxes or storage bins (numbered 0, 1, 2, 3), each holding a fruit, to illustrate zero-based indexing.

> ⚠ Arrays in JavaScript always begin with index 0; double-check your position when accessing elements!

## Modifying existing array elements

Arrays are not just storage—they are flexible collections. You can update any element at a given index.

To change a value, use the same square bracket notation, but combine it with the assignment operator `=`. Assign a new value to the index you wish to update.

```javascript
fruits[1] = 'blueberry';
console.log(fruits); // Prints: ['apple', 'blueberry', 'cherry', 'date']
```

In this code, we update the element at index 1 (the second item) from `'banana'` to `'blueberry'`.

> 💡 Just as you might relabel or swap an item in an organizer, you can update any slot in your array with a new value—no need to rewrite the whole list.

tktk asset: Animated GIF or illustration showing swapping a label on a box or organizer to a new label (“banana” swapped to “blueberry”).

## Common pitfalls when accessing and modifying elements

While array access is straightforward, it is also easy to make mistakes. Let’s explore some frequent issues:

- **Off-by-one errors:** This happens when you forget arrays start at 0. For example, an array with three elements has indices 0, 1, and 2. If you try to access index 3, you get `undefined`.

  ```javascript
  let pets = ['cat', 'bird', 'hamster'];
  console.log(pets[3]); // Prints: undefined
  ```

- **Accessing out-of-bounds indices:** Trying to access or assign to an index that doesn’t exist either gives you `undefined` (when reading) or creates empty slots (when writing):

  ```javascript
  pets[5] = 'parrot';
  console.log(pets); // Prints: ['cat', 'bird', 'hamster', empty × 2, 'parrot']
  ```

- **Mixing up data types:** Technically, JavaScript arrays can store values of any type. For clarity and fewer bugs, try to keep the data types in one array consistent.

- **Accidental overwrites:** Always confirm your index when updating! Accidentally changing the wrong index could quietly change your data in unexpected ways.

> ⚠ Double-check your intended index, especially when updating values—off-by-one errors are very common for new programmers.

tktk asset: Simple “before and after” array diagram showing what happens when assigning to an index beyond the current last element—a gap appears.

## Practical examples of element manipulation

Arrays are everywhere in real-life and digital scenarios. Here are a few relatable examples:

**Example 1: Updating a task in a to-do list**

If you’re tracking tasks for the day, you might update an entry once it’s completed.

```javascript
let todos = ['Check email', 'Join meeting', 'Write report'];
todos[1] = 'Join meeting (done)';
console.log(todos); // Prints: ['Check email', 'Join meeting (done)', 'Write report']
```

**Example 2: Fixing a typo in a list of names**

Suppose you spot and correct an error in a contact list:

```javascript
let contacts = ['Amira', 'Bo', 'Jonh'];
contacts[2] = 'John';
console.log(contacts); // Prints: ['Amira', 'Bo', 'John']
```

**Example 3: Showing first and last items in a shopping cart**

Knowing how to access the last item (no matter the array’s length) is especially useful:

```javascript
let cart = ['Tablet', 'Headphones', 'Charger'];
console.log(cart[0]); // Prints: Tablet
console.log(cart[cart.length - 1]); // Prints: Charger
```

> 🧠 Remember, `array.length - 1` gives you the last valid index, even if the array grows or shrinks.

tktk asset: Callout graphic showing an online shopping cart with a visual of both the first and last items highlighted.

## Activity: Practice with accessing and modifying array elements

### Purpose

Applying what you’ve learned solidifies your understanding of how to access and update array elements—skills critical for any coding involving lists or collections.

### Instructions

1. **Open Visual Studio Code or another JavaScript editor.**
2. **Create an array named `favoriteBooks` with four book titles you enjoy.**
   - Example:

     ```javascript
     let favoriteBooks = ['1984', 'Dune', 'Matilda', 'Pride and Prejudice'];
     ```

3. **Print the whole array to confirm it is set up.**
4. **Access and print the second and fourth books with their index positions.**
5. **Update the third book to another title (preferably one you have read or want to read).**
   - Use square bracket notation to change the value.
6. **Print the updated array to see your changes.**
7. **Attempt to access an index that does not exist, such as index 10. Print that value.**
8. **Deliverable:**  
   - Share your code snippet showing: the original array, element access, the update, and the output for both valid and invalid accesses.

tktk asset: Screenshot of Visual Studio Code or online editor showing correctly formatted output and comments.

## Discussion prompt

Indexes are essential when working with JavaScript arrays. Think of a real-life scenario—correcting a name in a class roster, updating a checklist, or changing an item in a menu. What could go wrong if you change the wrong spot? Share an example scenario with your group and discuss how you might prevent or catch such mistakes in your code.

## Knowledge checks

**Question 1:**  
What is the correct way of updating the third element in an array named `cities`?

- A) `cities[3] = 'Lagos';`
- B) `cities[2] = 'Lagos';`
- C) `cities['3'] = 'Lagos';`
- D) `cities['2'] = 'Lagos';`

**Question 2:**  
What will happen if you try to print `colors[10]` when `colors` contains only five items?

- A) It prints the last color in the array.
- B) It prints `'undefined'`.
- C) It prints an error message.
- D) It prints all colors up to index 10.

## Instructor guide

**Delivery tips:**

- Encourage learners to draw on their own hobbies, reading interests, or local experiences to make the array examples more personally meaningful.
- Use the mailbox or storage bin analogy, as well as callout visuals, to reinforce the concept of zero-based indexing visually and conceptually.
- When facilitating the activity, remind students to verbalize or comment on what outcome they expect after each update or access operation.
- During discussion, prompt learners to think about how arrays relate to spreadsheets, lists, or collections they use in everyday digital life.
- If working remotely, suggest that learners share their code screencasts or screenshots for peer support and feedback on the deliverable piece.

**Knowledge check answers:**

1. B) `cities[2] = 'Lagos';`
2. B) It prints `'undefined'`.

**Suggested solution to the activity:**

```javascript
let favoriteBooks = ['1984', 'Dune', 'Matilda', 'Pride and Prejudice'];
console.log(favoriteBooks);
// Prints: ['1984', 'Dune', 'Matilda', 'Pride and Prejudice']

console.log(favoriteBooks[1]); // Prints: Dune
console.log(favoriteBooks[3]); // Prints: Pride and Prejudice

favoriteBooks[2] = 'Ikigai';
console.log(favoriteBooks);
// Prints: ['1984', 'Dune', 'Ikigai', 'Pride and Prejudice']

console.log(favoriteBooks[10]); // Prints: undefined
```

> 💡 Reinforce the zero-based indexing and dynamic updating process to help learners internalize the access and modification pattern.

## Reasoning for Changes

1. **Narrative introduction and connections:** Added introductory language to bridge from previous microlessons, explicitly referencing foundational concepts and the learner’s prior experience.

2. **Definition callouts and jargon explanations:** Further defined *element* and *index* within callout boxes, providing accessible explanations of new terms for beginners.

3. **Globally relatable analogies and examples:** Maintained and clarified the familiar mailbox/storage bin analogy, consistent with earlier microlessons. Replaced any examples or references with potential regional limits (such as specific Western-centric foods or names) with inclusive, global, or neutral content. Examples (such as a task list, shopping cart, or contact list) are universally relatable.

4. **Visual and asset suggestions:** Included `tktk asset:` markers at key moments for visuals (e.g., zero-based index mailboxes, array updates, code screenshots) to facilitate visual learning and slide conversion in keeping with the Markdown Document Structure guidelines.

5. **Practical application and activity design:** Expanded the hands-on activity with an explicit purpose, clear step-by-step instructions, and a request for a concrete deliverable. Connected the activity directly to practical, daily-life tasks (book lists, checklists) to reinforce real-world relevance, referencing Exercise Instruction Guidelines for clarity and role as a stand-alone exercise.

6. **Explicit knowledge checks:** Developed two culturally neutral, directly relevant multiple-choice knowledge checks that focus on zero-based indexing and out-of-bounds access—both common areas of confusion. Structured question wording for clarity, ease of translation, and inclusivity.

7. **Discussion prompt:** Crafted a discussion prompt tying code errors (wrong index) to real scenarios (e.g., class lists, menus), inviting learners to contextualize mistakes and error prevention authentically in global contexts.

8. **Instructor guide:** Added concise, actionable delivery tips (encouraging personal and cultural relevance in examples), clarification on remote/peer learning adaptations, and model solutions for both activity and knowledge checks, per guidance in Instructor Guide and Exercise Instruction Guidelines.

9. **Markdown formatting and modularity:** Used consistent spacing, module-conforming headings, and clear formatting for easy slide conversion and scan-ability, meeting the standards from the Markdown Document Structure and Modular Writing guidelines.

10. **Emphasis on inclusivity and accessibility:** Ensured that names, examples, data, and analogies throughout would resonate with all learners—avoiding any culturally loaded, idiomatic, or region-specific content. Maintained clarity for non-native English speakers and coding beginners.

11. **Maintaining technical accuracy:** Retained and clarified SME-provided code snippets for accuracy, reinforced best practices, and elaborated on subtle code pitfalls to help learners avoid common mistakes.

These changes result in a microlesson that supports practical understanding, accessibility, and inclusive engagement while meeting the technical, structural, and narrative expectations for enriching modular content.
