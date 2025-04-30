# Accessing and Modifying Array Elements

**Learning Objective:** Access and modify elements within an array using square brackets.

## Using square bracket notation to access elements

Arrays store ordered collections of values, and in JavaScript, we access or reference the items inside an array using what’s called “square bracket notation.” Let’s look closely at how this works.

Every item in an array has a location, called an “index.” JavaScript starts counting these positions at 0, not 1. So the first element is at index 0, the second is at index 1, and so on.

Here’s an example array:

```javascript
let fruits = ['apple', 'banana', 'cherry', 'date'];
```

If we want to get the first fruit, we use its index—`0`:

```javascript
console.log(fruits[0]); // Output: apple
```

Similarly, to get the third fruit:

```javascript
console.log(fruits[2]); // Output: cherry
```

Notice that the index in the brackets tells JavaScript which “slot” in the array to give us. If you ask for an index that doesn’t exist, like `fruits[10]`, you’ll get `undefined` as a result, since that slot hasn’t been filled.

## Modifying existing array elements

Just as we can access elements with square brackets, we can also use square brackets along with an assignment (`=`) to change the value stored at a specific position in the array.

Let’s suppose we want to change 'banana' to 'blueberry' in our `fruits` array above:

```javascript
fruits[1] = 'blueberry';
console.log(fruits);
// Output: ['apple', 'blueberry', 'cherry', 'date']
```

We point to index `1` (which is where 'banana' lives) and assign a new value to that spot.

It’s important to remember that when we assign a new value to a specific index, we don’t change the other elements—just the one we’re pointing to. Here’s another example, changing the last item:

```javascript
fruits[3] = 'dragonfruit';
console.log(fruits);
// Output: ['apple', 'blueberry', 'cherry', 'dragonfruit']
```

## Common pitfalls when accessing/modifying arrays

Let’s talk about some common mistakes new programmers make when working with arrays:

### Off-by-one errors

Since arrays in JavaScript start at index 0, it’s easy to accidentally try to access the “first” item by using index 1. Always remember, the first element is at index 0.

```javascript
console.log(fruits[0]); // First item
console.log(fruits[1]); // Second item
```

### Using indexes that don’t exist

If you try to get or set an index past the end of the array, JavaScript doesn’t throw an error, but you’ll either read `undefined` or create an empty slot in your array.

```javascript
console.log(fruits[10]); // Output: undefined

fruits[6] = 'kiwi';
console.log(fruits);
// Output: ['apple', 'blueberry', 'cherry', 'dragonfruit', undefined, undefined, 'kiwi']
```

Notice how two blank slots (undefined) appear in the middle if we assign to index 6. This might cause confusion or bugs, so it’s important to keep track of your array’s length.

### Assignment vs. Reference

When you reassign an element in the array, only that element changes; the rest of the array stays the same. Also, mutating an array changes the original array itself, since arrays are objects.

## Demonstration: Accessing and modifying arrays in Visual Studio Code

Let’s walk through a common workflow using Visual Studio Code (VS Code), a popular code editor. We’ll create an array, access its elements, and then make some modifications.

1. Open VS Code and create a new file called `arrays-demo.js`.
2. Add this code to define the array:

    ```javascript
    let colors = ['red', 'green', 'blue', 'yellow'];
    ```

3. Access the second color and display it:

    ```javascript
    console.log(colors[1]); // Output: green
    ```

4. Change 'yellow' to 'orange':

    ```javascript
    colors[3] = 'orange';
    console.log(colors);
    // Output: ['red', 'green', 'blue', 'orange']
    ```

5. Try to access an element beyond the array’s length:

    ```javascript
    console.log(colors[10]); // Output: undefined
    ```

6. Save and run your script using Node.js in the terminal:

    ```
    node arrays-demo.js
    ```

Notice how your access and modification happen instantly with the familiar square brackets.

## Activity: Manipulating array data based on given instructions

Let’s put your new knowledge into practice. This activity is designed for you to work on your own or with a partner.

### Instructions

1. Open a new file in your code editor called `playlist.js`.
2. At the top of the file, create an array named `playlist` that has these five song names (as strings): `'Shape of You'`, `'Uptown Funk'`, `'Despacito'`, `'Blinding Lights'`, and `'Bad Guy'`.
3. Using `console.log`, print out the third song in your array.
4. Change the fifth song in the array from `'Bad Guy'` to `'Levitating'`.
5. Print out the entire `playlist` array so you can see the updated list.
6. Try to access an index that doesn’t exist in the array (for example, index `10`). Print the result.
7. Save your file and run it using Node.js in the terminal.

### Deliverable

Copy and paste your final code (and the output from running it) into the learning platform’s chat or designated classroom discussion board.

### Discussion prompt

Arrays help us organize and update collections of related values efficiently. Think about a real-world scenario where quickly modifying a single item in a collection (like updating a contact's number in your phone’s contact list or changing a booked seat in a flight’s manifest) would be important. Share an example in the chat or be ready to talk about why fast, direct changes to an array might matter in software you use or build.