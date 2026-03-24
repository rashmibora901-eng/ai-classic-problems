import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("🐒 Monkey Banana Game 🍌")
root.geometry("900x500")

# ---------------- LOAD IMAGES ----------------
bg_img = ImageTk.PhotoImage(Image.open("background.png").resize((900, 400)))
monkey_img = ImageTk.PhotoImage(Image.open("monkey.png").resize((120, 120)))
box_img = ImageTk.PhotoImage(Image.open("box.png").resize((120, 80)))
banana_img = ImageTk.PhotoImage(Image.open("banana.png").resize((80, 80)))

# ---------------- CANVAS ----------------
canvas = tk.Canvas(root, width=900, height=400)
canvas.pack()

# Background
canvas.create_image(0, 0, image=bg_img, anchor="nw")

# Positions
positions = {"door": 150, "middle": 450, "window": 750}

monkey_pos = "door"
box_pos = "middle"
banana_pos = "window"
monkey_on_box = False

# ---------------- OBJECTS ----------------
banana = canvas.create_image(positions[banana_pos], 100, image=banana_img)
box = canvas.create_image(positions[box_pos], 300, image=box_img)
monkey = canvas.create_image(positions[monkey_pos], 300, image=monkey_img)

# ✅ FIX: bring objects to front
canvas.tag_raise(monkey)
canvas.tag_raise(box)
canvas.tag_raise(banana)

# ---------------- STATUS ----------------
status = tk.Label(root, text="Use buttons to play!", font=("Arial", 12, "bold"))
status.pack()

# ---------------- SMOOTH MOVE (FIXED) ----------------
def smooth_move(item, dx, dy):
    steps = 25
    for _ in range(steps):
        canvas.move(item, dx/steps, dy/steps)

        # ✅ KEEP OBJECTS ALWAYS VISIBLE
        canvas.tag_raise(monkey)
        canvas.tag_raise(box)
        canvas.tag_raise(banana)

        root.update()
        time.sleep(0.01)

# ---------------- MOVE FUNCTION ----------------
def move(direction):
    global monkey_pos

    if direction == "right":
        smooth_move(monkey, 300, 0)
    elif direction == "left":
        smooth_move(monkey, -300, 0)

    current_x = canvas.coords(monkey)[0]

    if abs(current_x - positions["door"]) < 50:
        monkey_pos = "door"
    elif abs(current_x - positions["middle"]) < 50:
        monkey_pos = "middle"
    elif abs(current_x - positions["window"]) < 50:
        monkey_pos = "window"

    status.config(text=f"Monkey at {monkey_pos}")

# ---------------- PUSH FUNCTION ----------------
def push_box():
    global box_pos, monkey_pos

    monkey_x = canvas.coords(monkey)[0]
    box_x = canvas.coords(box)[0]

    if abs(monkey_x - box_x) < 60:
        dist = positions[banana_pos] - box_x

        smooth_move(box, dist, 0)
        smooth_move(monkey, dist, 0)

        box_pos = banana_pos
        monkey_pos = banana_pos

        status.config(text="Box moved under banana!")
    else:
        status.config(text="Go to box first!")

# ---------------- CLIMB ----------------
def climb():
    global monkey_on_box
    if monkey_pos == box_pos and not monkey_on_box:
        smooth_move(monkey, 0, -120)
        monkey_on_box = True
        status.config(text="Monkey climbed!")
    else:
        status.config(text="Can't climb now!")

# ---------------- GRAB ----------------
def grab():
    if monkey_pos == banana_pos and monkey_on_box:
        canvas.delete(banana)
        status.config(text="🎉 Monkey got the banana!")
        messagebox.showinfo("Success", "Monkey grabbed the banana 🍌")
    else:
        status.config(text="Not ready to grab!")

# ---------------- BUTTONS ----------------
frame = tk.Frame(root)
frame.pack(pady=10)

btn = {"width": 14, "font": ("Arial", 10, "bold")}

tk.Button(frame, text="⬅ Move Left", bg="#ffd966", command=lambda: move("left"), **btn).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Move Right ➡", bg="#ffd966", command=lambda: move("right"), **btn).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Push Box", bg="#ffb366", command=push_box, **btn).grid(row=0, column=2, padx=5)
tk.Button(frame, text="Climb", bg="#ff944d", command=climb, **btn).grid(row=0, column=3, padx=5)
tk.Button(frame, text="Grab Banana", bg="#66cc66", command=grab, **btn).grid(row=0, column=4, padx=5)

root.mainloop()