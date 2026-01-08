# 💅🏻 PickMyNails

## Nail Art Roulette

A fun and simple tool to help you choose your next nail design!
Choosing a nail design can be overwhelming. There are too many colors, styles, shapes, and trends.
PickMyNails is a lightweight Python application with a simple GUI that selects a nail design specifically for you.
Perfect when you're on your way to your appointment and can’t decide what to pick 👍

---

## Project Overview 📌

PickMyNails is a simple graphical application that randomly selects a nail style for the user.
The app helps people who struggle to choose their nail design by generating a random combination of:

* **Color** 🎨
* **Shape** 💅
* **Decoration** ✨

The user can either spin each category individually or generate a **Full Set Spin** which picks all three at once.

* Clicking **Spin Color**, **Spin Shape**, or **Spin Decoration** will display the corresponding image only.
* The **Full Set Spin** button generates all three selections and displays the images side by side.

The app also allows users to:

* Save favorite sets for later use
* Add new colors, shapes, or decorations directly from the GUI

---

## What This Project Does 🎯

* Provides a roulette-like randomizer for nail designs.
* Displays matching images for each style (color, shape, decoration).
* Helps indecisive users pick a full nail design quickly.
* Allows flexible future extension such as more categories, images, saving selections etc.
* Users can save their favorite sets and view them later.
* Users can add new colors, shapes, or decorations through the GUI.

---

## Input 📥

The program does **not** require user-provided files.
Input is via the GUI and includes:

* Clicking buttons to trigger a random “spin”
* Adding new options through the GUI (color, shape, decoration)
* Saving favorite sets to a local JSON file

---

## Output 📤

The GUI displays:

* The selected color, shape, or decoration (depending on which spin is used)
* For a full spin, all three selections are displayed **side by side**
* Text summary of the current selection:

  ```
  Your nails: Baby Pink | Almond | Glitter
  ```
* Saved favorites can be viewed via the **Load Favorites** button

---

## Image Handling 🖼

Each option corresponds to a filename. Images must be placed in **category-specific subfolders**:

```
PickMyNails/images/colors/
PickMyNails/images/shapes/
PickMyNails/images/decorations/
```

Filenames should follow this convention:

| Option    | Filename        |
| --------- | --------------- |
| Baby Pink | `baby_pink.png` |
| Almond    | `almond.png`    |
| Glitter   | `glitter.png`   |

The program automatically loads the correct image based on the selection.
Individual spins show **one image**, while full spin shows **all three images side by side**.

---

## Installation Instructions 🛠️

### 1. Clone the repository

```bash
git clone https://github.com/ronyho3008/PickMyNails
cd PickMyNails
```

### 2. Install dependencies

This project uses only the **built-in** Tkinter and standard library.
No external packages are required.
(PIL/Pillow is used for image handling – ensure Pillow is installed: `pip install pillow`)

### 3. Run the application

```bash
python .\PickMyNails\nails_roulette.py
```

---

## Tests 🧪

* Random selection functions
* File handling for images
* GUI components logic
* Favorites saving/loading
* Adding new options

---

## Technical Details 🔧

* Language: **Python 3**
* GUI: **Tkinter**
* Image support: `.png` files
* Designed with modularity and future extensibility

---

## More Improvements 🌱

* Animated spinning wheel for full spin
* Combined image preview (overlay or side by side)
* Saving favorite sets
* Allow users to add styles directly from the GUI
* More nail categories (length, finish, art style)

---

## 📚 Course Information

This project was created as part of the **Python Programming Course - 20263071**, under the final project assignment.

©️ Rony Holdengreber
