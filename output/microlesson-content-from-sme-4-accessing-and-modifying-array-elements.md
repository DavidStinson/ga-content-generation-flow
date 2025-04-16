# Accessing and Modifying Array Elements

## Learning Objective

By the end of this microlesson, you will be able to access and modify elements within a JavaScript array using square brackets.

---

## Accessing individual array elements

Arrays let us store lists of data—like favorite books, shopping items, or user names—in a single variable. But to use these values in our programs, we often need to grab just one out of the list. That’s where **accessing array elements** comes in.

In JavaScript, each item inside an array is called an **element**, and every element has a unique number attached to it. This number is called its **index**. 

**Indexing starts at 0.**  
That means the first element is at index 0, the second at index 1, and so on.

**How to access an element:**  
You use the array's name, followed by square brackets `[]`, and put the index number inside the brackets.

**Example:**  
Let’s use an array of movie titles:

```javascript
let movies = ["Inception", "Moana", "The Matrix"];
```

To access the second movie, "Moana":

```javascript
console.log(movies[1]); // Output: "Moana"
```

**Why [1] and not [2]?**  
Because arrays count from zero:
- `movies[0]` is "Inception"
- `movies[1]` is "Moana"
- `movies[2]` is "The Matrix"

**Analogy:**  
Think of an apartment building where room numbers start at 0 on the first floor. To get to the third apartment, you go to room 2.

---

## Modifying array elements

Arrays are not only for storing data—you can also change their elements after creating them. This is called **modifying** an array element.

**How to modify an element:**  
You use the same syntax as accessing, but this time you assign a new value.

**Example:**  
Let’s update "Moana" to "Interstellar":

```javascript
movies[1] = "Interstellar";
console.log(movies); // Output: ["Inception", "Interstellar", "The Matrix"]
```

Here’s what happens step by step:
1. `movies` was `["Inception", "Moana", "The Matrix"]`.
2. We changed the element at index 1.
3. Now, `movies` is `["Inception", "Interstellar", "The Matrix"]`.

**Why is this useful?**  
Modifying elements lets your programs react to new information or user choices. Imagine allowing a user to update their email address in a profile: you only need to change one item in the array, not rewrite the whole thing.

---

## Common pitfalls when working with array indices

While accessing and modifying array elements is straightforward, beginners often run into similar challenges. Let’s look at the two most common:

### 1. Index out of bounds

An **"index out of bounds"** happens when you use an index number that is too high (or low) for your array.

**Example:**

```javascript
let animals = ["dog", "cat", "rabbit"];
console.log(animals[3]); // Output: undefined
```

The `animals` array has indices 0, 1, and 2. `animals[3]` does not exist and so returns `undefined`—JavaScript’s way of saying "there isn’t anything here."

**Tip:**  
To safely access the last item in an array, use the array's `.length` property:

```javascript
let lastAnimal = animals[animals.length - 1]; // "rabbit"
```

### 2. Off-by-one errors

Since arrays start counting at 0, it’s easy to accidentally use the wrong index. Always double check your array’s length and indices.

**Visual Reference:**

| Index | Element      |
|-------|--------------|
|   0   | "dog"        |
|   1   | "cat"        |
|   2   | "rabbit"     |

If you have 3 elements, their indices are 0, 1, and 2—not 1, 2, and 3.

**Quick tip:**  
`array.length` tells you **how many** elements, but the last element is at `array.length - 1`.

---

## Interactive exercise: Accessing and modifying array elements in Visual Studio Code

It’s time to practice! This hands-on activity will help you reinforce how to access and update specific items in an array.

### Step-by-step instructions

1. **Open Visual Studio Code**  
   Or use an online JavaScript playground like repl.it or JSFiddle.

2. **Create an array of your three favorite foods:**

   ```javascript
   let favoriteFoods = ["pizza", "sushi", "tacos"];
   ```

3. **Print the second food to the console by accessing it through its index.**  
   (Remember: indices start at 0!)

   ```javascript
   console.log(favoriteFoods[1]); // Should output "sushi"
   ```

4. **Change the third food item to a new favorite:**  
   Assign a new value to the index for the third food.

   ```javascript
   favoriteFoods[2] = "ice cream";
   ```

5. **Print the full array to verify the change:**  

   ```javascript
   console.log(favoriteFoods); // Should output ["pizza", "sushi", "ice cream"]
   ```

6. **Try accessing an index that doesn’t exist:**  
   What happens if you try `console.log(favoriteFoods[5]);`?

7. **Deliverable:**  
   - Post your full code (steps 2–6) and the output to your class chat or discussion board.
   - In your post, briefly explain what you observed when you tried to access a non-existent index.
   - Did updating the array element work as you expected? Why or why not?

---

### Discussion prompt

Reflect and share your experience:
- When changing an array element’s value, did you find the process intuitive?  
- What happened when you tried to access an index that didn’t exist? How might this affect a larger program?
- Can you think of a real-world scenario—like managing a to-do list or editing a playlist—where accessing and modifying elements by index would be useful?

Read a classmate’s response and see if they ran into different results or insights. How might their approach help you avoid common mistakes?

---

Congratulations! You’ve now practiced accessing and modifying array elements using square brackets in JavaScript. Mastering these basics will empower you to organize and manage lists of data dynamically in your future coding projects. Up next: you’ll learn about using array methods like `push()` and `pop()` to add or remove elements, making your arrays more flexible than ever!