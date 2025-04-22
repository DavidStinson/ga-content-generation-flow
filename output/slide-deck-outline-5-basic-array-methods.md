**Slide 1**
# Basic array methods

- Arrays store lists of data in JavaScript
- Methods help add and remove items easily
- We’ll focus on: push(), pop(), shift(), unshift()
- No advanced coding required—perfect for beginners

PURPOSE:
Introduce the topics, set expectations, and reassure learners about skill level.

TALKING POINTS
- Why arrays are important for storing lists
- Real-life connection: to-do lists, objects, groceries
- Preview today’s key methods and hands-on activity

TEACHING TIPS
- Relate array methods to daily list management
- Encourage questions about any confusing concepts

---

**Slide 2**
## What are array methods?

- Built-in tools provided by JavaScript
- Make working with lists faster and simpler
- Let you add, remove, or rearrange items
- No need to know exact position or length
- Like adding, crossing off, or reordering real-life lists

PURPOSE:
Clarify the overall role and ease of array methods using analogies.

TALKING POINTS
- “Methods” as helpers for common list tasks
- Array position vs. everyday list management
- Emphasize not needing advanced math to use methods

TEACHING TIPS
- Use physical list props to illustrate
- Address “method” = “built-in feature”

---

**Slide 3**
## push(): Add items to the end

- Adds one or more elements at the end
- Automatically increases array length
- Returns new array length
- Syntax: array.push(item1, item2, ...)

Example:
```javascript
let colors = ['red', 'green', 'blue'];
colors.push('yellow');
console.log(colors); // ['red', 'green', 'blue', 'yellow']
```

- Can add several items at once:
```javascript
let fruits = ['apple', 'banana'];
fruits.push('cherry', 'date');
// ['apple', 'banana', 'cherry', 'date']
```

PURPOSE:
Explain push(), its purpose, syntax, and provide concrete examples.

TALKING POINTS
- Adding to the “bottom” of the list
- No need to count locations/indexes
- push() is clear and readable

TEACHING TIPS
- Analogize to adding groceries to end of a list
- Let learners try adding more than one item

---

**Slide 4**
## pop(): Remove items from the end

- Removes last element from the array
- Changes array length (one less)
- Returns the item removed
- Syntax: array.pop()

Example:
```javascript
let numbers = [10, 20, 30];
let removed = numbers.pop();
console.log(numbers); // [10, 20]
console.log(removed); // 30
```

- If array is empty, returns undefined

PURPOSE:
Demonstrate the pop() method with examples and set expectations.

TALKING POINTS
- Like erasing the last item on a to-do list
- Focus on array’s “end” position
- pop() works silently if there’s nothing left

TEACHING TIPS
- Model on whiteboard: crossing out a finished task
- Prepare for questions: “What if the list is empty?”

---

**Slide 5**
## unshift(): Add items to the beginning

- Adds one or more items at the start
- Shifts existing elements to the right
- Returns new length
- Syntax: array.unshift(item1, item2, ...)

Example:
```javascript
let animals = ['dog', 'cat'];
animals.unshift('hamster');
console.log(animals); // ['hamster', 'dog', 'cat']
```

- Multiple items at once:
```javascript
let letters = ['b', 'c'];
letters.unshift('a');
// ['a', 'b', 'c']
```

PURPOSE:
Make clear that unshift() targets the array start and show simple code.

TALKING POINTS
- Add at the “top” of the list
- Use case: highest priority first
- No index math needed

TEACHING TIPS
- Relate to adding urgent tasks at start
- Emphasize shifting of all items

---

**Slide 6**
## shift(): Remove items from the beginning

- Removes first element from the array
- All other elements shift left
- Returns the item removed
- Syntax: array.shift()

Example:
```javascript
let queue = ['Alice', 'Bob', 'Charlie'];
let next = queue.shift();
console.log(queue); // ['Bob', 'Charlie']
console.log(next); // 'Alice'
```

PURPOSE:
Describe shift()’s role and give direct usage examples.

TALKING POINTS
- Removes oldest, or first-in-line
- Perfect for queues or processing in order
- Handy for “first come, first served” scenarios

TEACHING TIPS
- Use line/queue examples from real life
- Explain impact of shift on remaining order

---

**Slide 7**
## Comparing array methods: Quick reference

| Method     | Action                   | Where?      |
|------------|--------------------------|-------------|
| push()     | Adds to array's end      | End         |
| pop()      | Removes from array's end | End         |
| unshift()  | Adds to array's start    | Beginning   |
| shift()    | Removes from array's start| Beginning  |

- push/pop: end of list (stack—last in, first out)
- unshift/shift: start of list (queue—first in, first out)

PURPOSE:
Help learners compare methods visually and conceptually.

TALKING POINTS
- Side-by-side summary for quick recall
- Relate each “end” to familiar real-world scenarios
- Emphasize list growth vs. shrinkage

TEACHING TIPS
- Reinforce with hand signals or props
- Let learners “act out” push/pop vs. shift/unshift

---

**Slide 8**
## When to use each array method

- push()/pop(): Use for stack-like operations
- unshift()/shift(): Use for queue-like operations
- Choose based on where you want to add/remove
- Using the right method keeps code simple and clear

Examples:
- Stack of plates: push() to add, pop() to remove top
- Waiting line: unshift() for new arrival, shift() to serve next

PURPOSE:
Guide learners to recognize the best method for a scenario.

TALKING POINTS
- Stack = add/remove from same side (end)
- Queue = add at start, remove from start
- Right method = cleaner, safer code

TEACHING TIPS
- Use physical objects for stack and queue demos
- Provide everyday examples for each approach

---

**Slide 9**
## Array playbook: Practice with array methods

- Create an array (your favorite theme)
- Add to the end with push()
- Remove from the end with pop()
- Add to start with unshift()
- Remove from start with shift()
- Try adding multiple items with push() or unshift()
- Print array after each step

PURPOSE:
Structure a guided, hands-on activity for skill building.

TALKING POINTS
- Each step uses a real method, not manual edits
- Printing helps track changes
- Multiple additions show method flexibility

TEACHING TIPS
- Encourage creative themes (snacks, cities, hobbies)
- Offer starter code for nervous learners

---

**Slide 10**
## Share your results and reflect

- Post your code and results to the group workspace
- Show how your array changed after each method
- Describe which method felt most natural to you
- Connect each method to a real-world task

PURPOSE:
Promote sharing, reflection, and peer learning.

TALKING POINTS
- Everyone’s code will look a bit different
- Reflecting builds deeper understanding
- Real-life examples aid memory

TEACHING TIPS
- Encourage group discussion and comparisons
- Praise all attempts; focus on process, not perfection

---