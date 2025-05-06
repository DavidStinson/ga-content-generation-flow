# Flex Container Properties

**Learning Objective:** Learn how to use CSS Flexbox for layout design.

## Introduction

When you’re designing websites, how your content is arranged shapes every visitor’s experience. Making content flexible—so it can adapt to different screen sizes and layouts—can feel challenging at first. That’s where CSS Flexbox comes in. Flexbox offers an efficient way to align and distribute space among items in a container, even when their size or the number of items changes.

In this lesson, we’ll get hands-on with the core properties you can use on a *flex container*—the parent element—to control layout, alignment, and spacing. These properties give you predictable, responsive layouts without complicated math or media queries.

tktk asset: An introductory illustration showing a flex container with a row of changing shapes, visually representing how content can stretch and adapt.

## Flex-direction: Controlling the main axis

The `flex-direction` property defines which direction the *main axis* runs in your flex container. The *main axis* is simply the direction you want your items to flow—in a line across the page, or stacked up and down.

> 💡 Think of the *main axis* like a conveyor belt in a factory. All your items (boxes, products, or in this case, HTML elements) will line up along that conveyor belt. The direction it moves determines how your items are arranged.

**Key values:**

- `row` (default): Items are placed left to right along the line.
- `row-reverse`: Items are placed right to left.
- `column`: Items are stacked top to bottom.
- `column-reverse`: Items are stacked bottom to top.

**Code Example:**

`styles.css`
```css
.container {
  display: flex;
  flex-direction: row;
}
```
This makes your container a flex container, arranging its items side by side, left to right.

If you switch to `flex-direction: column;`, items are stacked vertically.

tktk asset: A simple diagram showing boxes arranged in a row and then in a column inside a flex container.

**Practical scenario:**

Suppose you are designing a menu for a site. If you want the menu items to sit side by side at the top, use `flex-direction: row`. If you want them to line up in a sidebar for mobile or a dashboard, use `flex-direction: column`.

## Justify-content: Aligning items along the main axis

Once you’ve set the main direction, you often need to control *how* the items fill that space. The `justify-content` property lets you manage spacing along the *main axis*.

> 📚 The *main axis* is set by `flex-direction`. *Justify-content* uses that axis to align or distribute your flex items.

**Common values:**

- `flex-start` (default): Items are packed toward the start of the main axis.
- `flex-end`: Items are packed toward the end.
- `center`: Items are centered.
- `space-between`: Items are spread out, first item at the start, last item at the end.
- `space-around`: Equal space around every item.
- `space-evenly`: Equal space between items and at the ends.

**Code Example:**

`styles.css`
```css
.container {
  display: flex;
  justify-content: space-between;
}
```
This spreads your items across the container: the first item sticks to the left edge, the last item to the right edge, with any remaining items spaced evenly between.

tktk asset: Visual of different justify-content values, showing blocks arranged with space-between, space-around, and so on, along a row.

> 💡 Think of `justify-content` like arranging books on a shelf:
> - `flex-start`: All books pushed to the left
> - `flex-end`: All books pushed to the right
> - `center`: Books grouped in the center
> - `space-between`: Books evenly spread out from edge to edge

## Align-items: Aligning items along the cross axis

While `justify-content` manages the main axis, the `align-items` property lets you decide how items align along the *cross axis*—perpendicular to your chosen direction.

> 📚 The *cross axis* runs perpendicular to the *main axis*. If your main axis is horizontal (`row`), your cross axis is vertical, and vice versa.

**Common values:**

- `stretch` (default): Items stretch to fill the container (if their size is not set).
- `flex-start`: Items align to the start of the cross axis.
- `flex-end`: Items align to the end.
- `center`: Items are centered along the cross axis.
- `baseline`: Items share the same text baseline.

**Code Example:**

`styles.css`
```css
.container {
  display: flex;
  align-items: center;
}
```
If your container has a set `height`, `align-items: center;` will vertically center all child elements inside the container.

tktk asset: Visual representation showing flex items aligned along the cross axis using different align-items values.

> 💡 Picture a row of framed photos on a gallery wall:
> - `flex-start`: Tops of all frames are aligned
> - `flex-end`: Bottoms aligned
> - `center`: Centers aligned

## Flex-wrap: Controlling item wrapping

By default, a flex container tries to keep all its items on a single line, shrinking them if necessary. Sometimes, that’s not ideal—especially for responsive designs.

The `flex-wrap` property lets you specify whether items should move onto new lines if there’s not enough space.

**Key values:**

- `nowrap` (default): All items fit on a single line, shrinking as needed.
- `wrap`: Items move to new lines as necessary.
- `wrap-reverse`: Like wrap, but new lines stack in the opposite direction.

**Code Example:**

`styles.css`
```css
.container {
  display: flex;
  flex-wrap: wrap;
}
```

With `flex-wrap: wrap;`, items will start a new line in the container if they run out of space, instead of shrinking indefinitely.

tktk asset: Animation or series of images showing a set of card elements wrapping to the next row as the container shrinks.

**Practical scenario:**

If you are listing user profile cards and want three side by side on large screens but have them appear on new lines as space runs out, enable wrapping with `flex-wrap: wrap;`.

## Practical examples of combining properties

Combining these properties makes layouts flexible and responsive—no complicated math needed.

**Example: Responsive button bar**

We want a horizontal bar of buttons that wraps onto new lines on smaller screens. The buttons should always be evenly spaced and vertically centered.

`styles.css`
```css
.button-bar {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-evenly;
  align-items: center;
  min-height: 60px;
}
```

What happens:
- On a desktop, all buttons might fit in one row, spaced evenly.
- As you shrink the window, buttons wrap onto new lines, but remain centered and evenly spaced.

tktk asset: Screenshot or diagram showing a responsive button bar at different window sizes.

> 💡 Combining these flex properties allows for layouts that automatically adapt to any screen size—a core need for modern, global web users.

## Activity: Responsive card layout challenge

Let’s put your Flexbox skills to work with a realistic and practical coding challenge.

### Purpose of the activity

Use Flexbox container properties to create a responsive and visually organized layout—just like you’d need for a gallery, a list of features, or product cards on a real website.

### Instructions

1. **Create an HTML file** with a `<div>` using the class `.card-container`. Inside, add six `<div>`s with the class `.card` to represent cards.

2. **Style `.card-container` using Flexbox:**
   - Set `display: flex;`.
   - Use `flex-direction` to arrange the cards in a row on large screens.
   - Allow cards to wrap to new lines if there’s not enough space.
   - Add spacing between cards using `justify-content`.
   - Center the cards vertically with `align-items`.

3. **Add styling to `.card`** (width, height, background color) to make wrapping obvious.

4. **Test responsiveness**: Resize your browser to see how the cards flow and wrap.

5. **Share your solution**: Post your CSS code for `.card-container` and a short summary of the flex properties you used.

tktk asset: Screenshots or mockups showing a card layout at three different window sizes: all cards in a row, wrapping onto two rows, and in a single column.

### Discussion prompt

How did changing each flex property affect the layout when you resized the browser? Which property did you find most helpful or surprising? Share your reflections and compare solutions in the discussion.

## Knowledge checks

❓ *Which property controls the direction (horizontal or vertical) that Flexbox items are arranged in a container?*

- A) align-items
- B) flex-direction
- C) justify-content
- D) flex-wrap

❓ *If you want all flex items to wrap onto a new line when there is not enough space, which property and value should you use?*

- A) flex-direction: column;
- B) align-items: center;
- C) flex-wrap: wrap;
- D) justify-content: space-evenly;

---

## Instructor guide

### Delivery tips

- **Pause at each property section** to check for understanding with visual assets and encourage learners to notice the axes (main vs. cross) in provided diagrams or demos.
- **Emphasize hands-on practice:** Encourage learners to experiment with different property values as you review each example.
- **Leverage learner discussion:** Use the practical scenarios and analogies to make the properties more memorable and relatable.
- For the **activity**, consider walking through setting up the base HTML and CSS, then give time for learners to experiment and implement the wrapping and alignment properties themselves.

### Knowledge check answers

1. B) flex-direction
2. C) flex-wrap: wrap;

### Activity solution

A starting point for `.card-container`:

`styles.css`
```css
.card-container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  min-height: 200px;
}
.card {
  width: 150px;
  height: 100px;
  background-color: #e0e0e0;
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
}
```

**Sample learner summary:**  
“I set `flex-direction` to `row` so the cards line up horizontally, `flex-wrap` to `wrap` so they drop onto a new line when there’s not enough space, used `justify-content: space-between` for even spacing, and centered the cards vertically with `align-items: center`.”

#### Remote adaptation

Encourage learners to share their code and screenshots in group chat or in a collaborative workspace. Prompt them to ask each other about the effect of different flex properties.