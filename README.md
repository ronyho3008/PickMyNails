# 💅🏻 PickMyNails 
## Nail Art Roulette
A fun and simple tool to help you choose your next nail design!
Choosing a nail design can be overwhelming. There are too many colors, styles, shapes, and trends.
PickMyNails is a lightweight Python application with a simple GUI that selects a nail design specificaly for you.
Perfect when you're on your way to your appointment and can’t decide what to pick 👍

## Project Overview 📌 
PickMyNails is a simple graphical application that randomly selects a nail style for the user.
The app helps people who struggle to choose their nail design by generating a random combination of:

* **Color** 🎨 
* **Shape** 💅 
* **Decoration** ✨ 

The user can either spin each category individually or generate a **Full Set Spin** which picks all three at once.
An image representing the selected option is displayed when possible.

---

## What This Project Does 🎯 

* Provides a roulette-like randomizer for nail designs.
* Displays matching images for styles (color/shape/decor).
* Helps indecisive users pick a full nail design quickly.
* Allows flexible future extension such as more categories, images, saving selections etc.
  
---

## Input 📥 

The program does **not** require user-provided files.
Input is via the GUI and includes only:

* Clicking buttons to trigger a random “spin”.
* Optionally: adding more colors/shapes/decorations by u`.png` files to the `images/` directory with matching filenames.

---

## Output 📤 

* The GUI displays:

  * The selected color / shape / decoration
  * A preview image that corresponds to the selection
* For a full spin, the output is a combined text result such as:

  ```
  Your nails: Baby Pink | Almond | Glitter
  ```
* If a matching image exists (based on filename), it is shown in the app.

---

## Image Handling 🖼 

Each option corresponds to a filename.
For example:

| Option    | Filename        |
| --------- | --------------- |
| Baby Pink | `baby_pink.png` |
| Almond    | `almond.png`    |
| Glitter   | `glitter.png`   |

Images must be placed inside the folder:

```
PickMyNails/images/
```

---

## Installation Instructions 🛠️ 

### 1. Clone the repository

```
git clone https://github.com/ronyho3008/PickMyNails
cd PickMyNails
```

### 2. Install dependencies

This project uses only the **built-in** Tkinter and standard library.
No external packages are required.

### 3. Run the application

```
python .\PickMyNails\nails_roulette.py
```

---

## Tests 🧪 

* Random selection functions
* File handling for images
* GUI components logic

---

## Technical Details 🔧 

* Language: **Python 3**
* GUI: **Tkinter**
* Image support: `.png` files
* Designed with modularity and future extensibility

---

## More Improvements 🌱 

* Combined image preview (overlay of color + shape + decoration)
* Saving favorite sets
* Allow users to add styles directly from the GUI
* Animated spinning wheel
* More nail categories (length, finish, art style)

---

## 📚 Course Information

This project was created as part of the **Python Programming Course - 20263071**,
under the final project assignment.

©️Rony Holdengreber
