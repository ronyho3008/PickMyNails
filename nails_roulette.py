import tkinter as tk
from tkinter import messagebox
import random
import os

# Separate categories
COLORS = [
    "Baby Pink",
    "Deep Red",
    "Milky White",
    "Lavender",
    "Nude",
    "Black",
    "Sky Blue",
]

SHAPES = [
    "Square",
    "Round",
    "Coffin",
    "Almond",
    "Stiletto",
]

DECORATIONS = [
    "Glitter",
    "Chrome",
    "French Tips",
    "Flakes",
    "Minimalist Line",
]

class NailRouletteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Nail Art Roulette")
        self.root.geometry("450x520")
        self.root.configure(bg="#F5F5F5")

        # paths
        self.base_dir = os.path.dirname(__file__)
        self.images_dir = os.path.join(self.base_dir, "images")

        # Title
        self.title_label = tk.Label(
            root,
            text="💅 Nail Art Roulette",
            font=("Arial", 20, "bold"),
            bg="#F5F5F5"
        )
        self.title_label.pack(pady=20)

        # Image Display
        self.image_label = tk.Label(root, bg="#F5F5F5")
        self.image_label.pack(pady=10)

        # Result Display
        self.result_var = tk.StringVar()
        self.result_label = tk.Label(
            root,
            textvariable=self.result_var,
            font=("Arial", 14),
            bg="#F5F5F5"
        )
        self.result_label.pack(pady=10)

        # Buttons
        self.full_spin_button = tk.Button(
            root,
            text="Full Set Spin",
            font=("Arial", 14, "bold"),
            command=self.full_spin,
            bg="#FFE8A6",
            width=15
        )
        self.full_spin_button.pack(pady=10)

        self.color_button = tk.Button(
            root,
            text="Spin Color",
            font=("Arial", 12),
            command=self.spin_color,
            bg="#FFD6E8"
        )
        self.color_button.pack(pady=5)

        self.shape_button = tk.Button(
            root,
            text="Spin Shape",
            font=("Arial", 12),
            command=self.spin_shape,
            bg="#D6E8FF"
        )
        self.shape_button.pack(pady=5)

        self.deco_button = tk.Button(
            root,
            text="Spin Decoration",
            font=("Arial", 12),
            command=self.spin_decoration,
            bg="#E8FFD6"
        )
        self.deco_button.pack(pady=5)

        # keep reference to image
        self.current_img = None

    # ---------- IMAGE HANDLING ----------

    def show_image_by_name(self, name):
        """Loads image based on value name, like 'Baby Pink' -> baby_pink.png"""
        filename = name.lower().replace(" ", "_") + ".png"
        filepath = os.path.join(self.images_dir, filename)

        if os.path.exists(filepath):
            self.current_img = tk.PhotoImage(file=filepath)
            self.image_label.config(image=self.current_img)
        else:
            self.image_label.config(image="")

    # ---------- SPIN FUNCTIONS ----------

    def spin_color(self):
        color = random.choice(COLORS)
        self.result_var.set(f"Color: {color}")
        self.show_image_by_name(color)

    def spin_shape(self):
        shape = random.choice(SHAPES)
        self.result_var.set(f"Shape: {shape}")
        self.show_image_by_name(shape)

    def spin_decoration(self):
        deco = random.choice(DECORATIONS)
        self.result_var.set(f"Decoration: {deco}")
        self.show_image_by_name(deco)

    def full_spin(self):
        color = random.choice(COLORS)
        shape = random.choice(SHAPES)
        deco = random.choice(DECORATIONS)

        self.result_var.set(
            f"Your nails: {color} | {shape} | {deco}"
        )

        # show image based on color as main visual
        self.show_image_by_name(color)


if __name__ == "__main__":
    root = tk.Tk()
    app = NailRouletteApp(root)
    root.mainloop()
