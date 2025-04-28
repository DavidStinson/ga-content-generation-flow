# Introduction to JavaScript Arrays

**Learning Objective:** Define JavaScript arrays and explain how they organize data.

## What is an array in JavaScript?

Arrays in JavaScript are special variables that hold lists of values. Imagine a row of mailboxes: each mailbox can hold one piece of mail, and the whole row lets you keep everything organized in one place. In JavaScript, arrays work the same way—they help you organize and keep track of groups of data. Instead of remembering a separate variable for each value (like a separate mailbox for each thing), you group related values into one handy container.

Arrays can store different types of values, but most often you'll see them used for storing lists of similar things—like a list of names, a collection of numbers, or even a group of colors.

Here's the basic way to create an array in JavaScript:

```javascript
let colors = ["red", "green", "blue"];
```

In this example, we're storing three color strings in one array named `colors`.

## Why use arrays: Purpose and benefits

Arrays help us manage data more efficiently and keep our code organized. Let's look at a few reasons why arrays are so useful:

- **Organization:** Instead of using a separate variable for each item, arrays let us keep all related data together.
- **Scalability:** If you collect more items (like student names in a class), you can add them to the same array without rewriting your code.
- **Iteration:** Arrays make it possible to process each item in a list using loops. For example, you could print every name in a guest list by “looping” through your array.
- **Data manipulation:** Arrays allow you to easily add, remove, or update items as your data changes.

Without arrays, working with a bunch of related values would be messy. With arrays, you can store, retrieve, and manipulate grouped information smoothly.

## Real-world examples of array usage

Arrays show up almost everywhere in programming, especially when you need to keep track of multiple pieces of related information. Here are some common scenarios:

- **Shopping Carts:** Online shopping sites use arrays to keep track of the products you want to buy. Each item you add—the t-shirt, coffee mug, or headphones—goes into an array.
- **Contact Lists:** Your phone stores your friends’ phone numbers and names in arrays so you can easily search or browse.
- **Website Navigation:** A website might have an array of all its menu items to create the navigation bar at the top.
- **Daily Planner:** You might have an array representing the tasks you want to accomplish today, like `["Check email", "Team meeting", "Lunch", "Write project draft"]`.

Here’s how a to-do list might look as an array:

```javascript
let todoList = ["Send emails", "Attend meeting", "Review report", "Plan tomorrow"];
```

## How arrays organize and store data

Arrays store data in a single variable, but they keep that data in a specific order. Each value in an array has a position called its "index". In JavaScript, array indices start at zero. This means the first item is at index 0, the second at 1, and so on.

Let's look at our previous color example:

```javascript
let colors = ["red", "green", "blue"];
```

Here's how JavaScript sees it:

- `colors[0]` is `"red"`
- `colors[1]` is `"green"`
- `colors[2]` is `"blue"`

You can access (or update) any value in the array using its index. This makes it fast to find or change specific items, even if your array gets large.

If you want to add a new color, you can do this:

```javascript
colors.push("yellow");
```

Now the array is `["red", "green", "blue", "yellow"]`.

Arrays truly shine when you need to process all their items, for example printing every color:

```javascript
for (let i = 0; i < colors.length; i++) {
  console.log(colors[i]);
}
```

This loop will print each color to the screen—no matter how many colors are in the array.



## Activity: Build your own favorite foods array

Let's get hands-on and practice what we've just learned. In this activity, you'll create and work with your own JavaScript array.

### Instructions

1. **Open a new file or sandbox:** 
   Start a new JavaScript file in your preferred code editor, or use an online sandbox like repl.it or JSFiddle.

2. **Create an array:**  
   Think of your top three favorite foods. Create a JavaScript array that stores these foods as strings.
   - Example:
     ```javascript
     let favoriteFoods = ["pizza", "sushi", "tacos"];
     ```

3. **Display the whole array:**  
   Use `console.log()` to print your entire array to the screen.
   - Example:
     ```javascript
     console.log(favoriteFoods);
     ```

4. **Access individual elements:**  
   Print just the first and last food in your array, using their index.
   - Example:
     ```javascript
     console.log(favoriteFoods[0]); // first favorite food
     console.log(favoriteFoods[2]); // third favorite food
     ```
   - If you're not sure what index to use for the last item, remember: arrays start counting at zero!

5. **Add a new favorite:**  
   Use `.push()` to add a fourth favorite food to your array, then print your array again.
   - Example:
     ```javascript
     favoriteFoods.push("ice cream");
     console.log(favoriteFoods);
     ```

6. **Deliverable:**  
   Share your code snippet with your group, or post it to the discussion board. Make sure your code includes:
   - The array definition with your favorite foods
   - Code that prints the entire array
   - Code that prints at least two individual items
   - Code that adds a fourth food and prints the updated array

### Discussion Prompt

Arrays are one way to organize groups of similar data, but there are other ways too. Why do you think using an array might be more helpful than creating a separate variable for each piece of information? Can you think of other daily-life lists or groupings that could be modeled as arrays in a program? Discuss with a partner, or share your thoughts with the group.