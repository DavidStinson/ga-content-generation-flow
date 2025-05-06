# Introduction to Flexbox

**Learning Objective:** Learn how to use CSS Flexbox for layout design.

## What is Flexbox and why does it matter?

Designing layouts on the web can feel a lot like organizing storage boxes in a room of unpredictable size. Imagine you need to arrange boxes of different shapes and sizes within a suitcase so they fit snugly, no matter how many items you add or remove, or how you turn the suitcase. Flexbox, short for Flexible Box Layout, is the CSS tool that empowers us to do just that – arranging items efficiently, neatly, and flexibly inside a container, even when their sizes change or when the screen size is unknown.

With earlier CSS techniques, web designers often needed complicated workarounds to line elements up or make them responsive to different device screens. Flexbox takes away that complexity, providing a modern system for reliable and adaptable layouts. You can organize content in rows or columns, allowing items to expand, shrink, or shift automatically. This means sites look and work well whether they're viewed on a mobile phone or a large monitor.

> 💡 Flexbox is like having an adjustable shelf that changes its shape for the things you want to store, instead of forcing every object to fit into rigid, fixed spaces.

tktk asset: An illustration of boxes expanding and shrinking within a flexible container, adapting to container size changes.

## Why Flexbox is better than traditional layout methods

Before Flexbox, designers relied on floats, inline-blocks, or using tables for layouts. These approaches often required a series of CSS "hacks," such as clearing floats or adding invisible elements, just to achieve basic alignment.

Flexbox was introduced to address these struggles by making layout control more intuitive. Here’s what sets it apart:

- **Direction control:** Easily set elements in a row or a column, without fiddling with complex code or markup.
- **Alignment:** Centering items both vertically and horizontally becomes direct and straightforward.
- **Reordering:** Visually rearrange content on the page without reordering the underlying HTML.
- **Space distribution:** Items expand, shrink, or space themselves out automatically in the available space.

> 🧠 Imagine creating a navigation bar where menu items stay centered, adjust their size as the window gets smaller, and make space for a new menu item without pushing everything out of alignment. Flexbox makes all of this possible in just a few lines of CSS.

tktk asset: Before-and-after visual comparing a float-based row versus a Flexbox row that adapts gracefully.

## Basic Flexbox terminology

Understanding Flexbox is simpler when you learn its building blocks:

### Flex container

A *flex container* is any element that you apply Flexbox to. When you set `display: flex;` on an element, you turn it into a flex container. Its direct children become *flex items* and follow Flexbox layout rules.

**Example:**

`index.html`
```html
<div class="flex-container">
  <div>Item 1</div>
  <div>Item 2</div>
  <div>Item 3</div>
</div>
```

> 📚 A *flex container* is the parent element that defines the context for Flexbox layout.

### Flex items

*Flex items* are the direct children of a flex container. Flexbox aligns, sizes, and spaces these items based on the rules you set.

In the example above, "Item 1", "Item 2", and "Item 3" are all flex items inside `.flex-container`.

> 📚 A *flex item* is a direct child element within a flex container.

tktk asset: Diagram showing a container (outlined) with labeled flex items inside.

### Main axis and cross axis

Flexbox uses two axes to position and align items:

- **Main axis:** The direction flex items are placed (defaults to left-to-right in a row).
- **Cross axis:** Runs perpendicular to the main axis (top-to-bottom by default).

> 💡 Think of the main axis as the expressway where your items travel side by side, and the cross axis as the road crossing it at a right angle.

tktk asset: Visual with arrows over a flex container demonstrating main and cross axes.

## How to activate Flexbox: using `display: flex`

To start using Flexbox, add `display: flex;` to your container’s CSS. This single line changes the layout behavior for all its direct children.

`style.css`
```css
.flex-container {
  display: flex;
}
```

`index.html`
```html
<div class="flex-container">
  <div>Item 1</div>
  <div>Item 2</div>
  <div>Item 3</div>
</div>
```

Right away, the child elements line up in a row and respond to available space, making layout management much simpler.

> 💡 With only one CSS property, your layout becomes flexible and responsive.

## Activity: Create your first Flexbox row

Let's experience Flexbox in a real scenario. You will use Flexbox to quickly build a row of boxes that adapt to changes in content or container size.

### Instructions

1. Open your preferred code editor (or an online tool such as CodePen or JSFiddle).
2. Create an `<code class="filepath">index.html</code>` file and add the following starter HTML:

   ```html
   <div class="flex-container">
     <div>Box 1</div>
     <div>Box 2</div>
     <div>Box 3</div>
   </div>
   ```

3. In your `<code class="filepath">style.css</code>` file, add the following styles:

   ```css
   .flex-container {
     display: flex;
     border: 2px solid #444;
     padding: 12px;
     background-color: #f8f9fa;
   }
   .flex-container > div {
     background: #e3e7eb;
     border: 1px solid #b0bfcf;
     padding: 20px;
     margin: 4px;
     font-size: 1.1em;
     text-align: center;
     flex: 1;
   }
   ```

4. Open `<code class="filepath">index.html</code>` in a web browser.

**Purpose:**  
This activity helps you directly observe how Flexbox manages layout and adapts to changes, reinforcing its value over older layout methods.

**Deliverable:**  
- Share your code snippet (both HTML and CSS) via chat or with a peer.
- As an optional challenge, try adding more or fewer boxes inside the container. Observe how Flexbox responds when you adjust the number of boxes, or even when you add more text in a box.

**Discussion prompt:**  
How do you think using Flexbox could change the way you design page layouts compared to floats or other earlier CSS techniques? If you have experience with earlier methods, share a challenge that Flexbox could solve. If you’re new to CSS layouts, imagine a design problem (like equally sized cards or a navigation bar) where Flexbox’s features might make your life easier.

tktk asset: Screenshot of the activity’s result showing three flexible boxes in a row, with arrows indicating their ability to grow or shrink if more are added.

---

## Instructor Guide

### Delivery tips

- Emphasize the real-world analogy of organizing items flexibly in a space, like packing a suitcase, to ground the concept.
- Highlight how Flexbox simplifies common layout headaches, reinforcing its practical benefit.
- Encourage learners to interact hands-on with the provided code, make small changes (such as adding or removing boxes), and discuss what they see.
- Use visuals (real or described assets) to reinforce concepts like axes and the flex container-item relationship.
- For remote sessions, allow learners to share screens or code links for collaborative observation.

### Activity solution

Example of a correct outcome:

- The three boxes appear in a row within the container, each expanding to fill the space evenly. When more boxes are added, the layout remains consistent and the boxes adjust their widths automatically.

### Knowledge check answers

1. Which property activates Flexbox on a container?  
   - Correct answer: `display: flex;`

2. In Flexbox, what are the direct children of a flex container called?  
   - Correct answer: flex items