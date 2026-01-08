import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import os
import json
from PIL import Image, ImageTk

# ---------- DATA ----------

COLORS = [
    "Baby Pink","Red","Milky White","Lavender","Nude","Black","Sky Blue",
    "Espresso Brown","Peach","Mint Green","Pistachio","wine","navy blue",
    "grey","gold","dark green","dark purple","yellow","barbie pink"
]

SHAPES = ["Square", "Round", "Coffin", "Almond", "Stiletto"]

DECORATIONS = ["Glitter","Chrome","French Tips","Flakes","Minimalist Line",
               "half moon","Ombre","Marble","matte","Swirl"]

FAVORITES_FILE = "favorites.json"

# ---------- APP ----------

class NailRouletteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("💅 Nail Art Roulette")
        self.root.geometry("600x650")
        self.root.configure(bg="#F5F5F5")

        # paths
        self.base_dir = os.path.dirname(__file__)
        self.images_dir = os.path.join(self.base_dir, "images")

        # current state
        self.current_color = None
        self.current_shape = None
        self.current_deco = None
        self.current_img = None

        # ---------- UI ----------
        tk.Label(root, text="💅 Nail Art Roulette", font=("Arial", 20, "bold"), bg="#F5F5F5").pack(pady=10)

        self.image_label = tk.Label(root, bg="#F5F5F5")
        self.image_label.pack(pady=10)

        self.result_var = tk.StringVar()
        tk.Label(root, textvariable=self.result_var, font=("Arial", 14), bg="#F5F5F5").pack(pady=10)

        # Spin buttons
        tk.Button(root, text="Full Set Spin", font=("Arial", 14, "bold"), command=self.full_spin, bg="#FFE8A6", width=20).pack(pady=10)
        tk.Button(root, text="Spin Color", command=self.spin_color, bg="#FFD6E8").pack(pady=5)
        tk.Button(root, text="Spin Shape", command=self.spin_shape, bg="#D6E8FF").pack(pady=5)
        tk.Button(root, text="Spin Decoration", command=self.spin_decoration, bg="#E8FFD6").pack(pady=5)

        # Favorites
        tk.Button(root, text="Save Current Set", command=self.save_favorite, bg="#FFC0CB").pack(pady=5)
        tk.Button(root, text="Load Favorites", command=self.load_favorites, bg="#FFB347").pack(pady=5)

        # Add new option
        tk.Button(root, text="Add New Option", command=self.add_new_option, bg="#90EE90").pack(pady=5)

    # ---------- IMAGE LOGIC ----------
    def load_image(self, category, name):
        filename = name.lower().replace(" ", "_") + ".png"
        path = os.path.join(self.images_dir, category, filename)
        if not os.path.exists(path):
            return None
        return Image.open(path).convert("RGBA")

    def update_image(self):
        """Update a single image (for individual spins)"""
        base = None
        if self.current_color:
            base = self.load_image("colors", self.current_color)
        if base and self.current_shape:
            shape = self.load_image("shapes", self.current_shape)
            if shape:
                base = Image.alpha_composite(base, shape)
        if base and self.current_deco:
            deco = self.load_image("decorations", self.current_deco)
            if deco:
                base = Image.alpha_composite(base, deco)
        if base:
            self.current_img = ImageTk.PhotoImage(base)
            self.image_label.config(image=self.current_img)
        else:
            self.image_label.config(image="")

    def update_text(self):
        self.result_var.set(
            f"{self.current_color or '-'} | {self.current_shape or '-'} | {self.current_deco or '-'}"
        )

    # ---------- SPIN FUNCTIONS ----------
    def spin_color(self):
        self.current_color = random.choice(COLORS)
        self.update_image()
        self.update_text()

    def spin_shape(self):
        self.current_shape = random.choice(SHAPES)
        self.update_image()
        self.update_text()

    def spin_decoration(self):
        self.current_deco = random.choice(DECORATIONS)
        self.update_image()
        self.update_text()

    def full_spin(self):
        # animated spin
        for _ in range(10):
            self.current_color = random.choice(COLORS)
            self.current_shape = random.choice(SHAPES)
            self.current_deco = random.choice(DECORATIONS)
            self.update_text()
            self.root.update()
            self.root.after(50)
        # final selection
        self.current_color = random.choice(COLORS)
        self.current_shape = random.choice(SHAPES)
        self.current_deco = random.choice(DECORATIONS)
        self.update_text()
        self.show_combined_image()

    # ---------- COMBINED IMAGE FOR FULL SPIN ----------
    def show_combined_image(self):
        """Show color, shape, decoration images side by side"""
        imgs = []
        for category, item in [("colors", self.current_color),
                               ("shapes", self.current_shape),
                               ("decorations", self.current_deco)]:
            img = self.load_image(category, item)
            if img:
                imgs.append(img)
        if not imgs:
            self.image_label.config(image="")
            return
        # Resize all images to same height
        height = 200
        resized_imgs = []
        for img in imgs:
            ratio = height / img.height
            new_width = int(img.width * ratio)
            resized_imgs.append(img.resize((new_width, height)))
        # concatenate side by side
        total_width = sum(img.width for img in resized_imgs)
        combined = Image.new("RGBA", (total_width, height), (255,255,255,0))
        x_offset = 0
        for img in resized_imgs:
            combined.paste(img, (x_offset, 0), img)
            x_offset += img.width
        self.current_img = ImageTk.PhotoImage(combined)
        self.image_label.config(image=self.current_img)

    # ---------- FAVORITES ----------
    def save_favorite(self):
        favorite = {
            "color": self.current_color,
            "shape": self.current_shape,
            "deco": self.current_deco
        }
        favorites = []
        if os.path.exists(FAVORITES_FILE):
            with open(FAVORITES_FILE, "r") as f:
                favorites = json.load(f)
        favorites.append(favorite)
        with open(FAVORITES_FILE, "w") as f:
            json.dump(favorites, f, indent=2)
        messagebox.showinfo("Saved", "Current set saved to favorites!")

    def load_favorites(self):
        if not os.path.exists(FAVORITES_FILE):
            messagebox.showinfo("Favorites", "No favorites saved yet!")
            return
        with open(FAVORITES_FILE, "r") as f:
            favorites = json.load(f)
        fav_text = "\n".join([f"{f['color']} | {f['shape']} | {f['deco']}" for f in favorites])
        messagebox.showinfo("Favorites", fav_text or "No favorites!")

    # ---------- ADD NEW OPTION ----------
    def add_new_option(self):
        category = simpledialog.askstring("Add Option", "Category (color/shape/deco):")
        if not category:
            return
        category = category.lower()
        name = simpledialog.askstring("Add Option", "Name of new option:")
        if not name:
            return
        if category.startswith("color"):
            COLORS.append(name)
        elif category.startswith("shape"):
            SHAPES.append(name)
        elif category.startswith("deco"):
            DECORATIONS.append(name)
        else:
            messagebox.showerror("Error", "Invalid category")
            return
        messagebox.showinfo("Added", f"{name} added to {category}")

# ---------- RUN ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = NailRouletteApp(root)
    root.mainloop()
