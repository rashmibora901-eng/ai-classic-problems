# MONKEY BANANA PROBLEM

print("========== MONKEY BANANA PROBLEM ==========\n")

# Initial Inputs from User
monkey_position = input("Enter Monkey Position (door/middle/window): ").lower()
box_position = input("Enter Box Position (door/middle/window): ").lower()
banana_position = input("Enter Banana Position (door/middle/window): ").lower()
monkey_on_box = input("Is Monkey on the box? (yes/no): ").lower()

print("\n----- INITIAL STATE -----")
print("Monkey Position :", monkey_position)
print("Box Position    :", box_position)
print("Banana Position :", banana_position)
print("Monkey on Box   :", monkey_on_box)

print("\n----- STEPS TO ACHIEVE GOAL -----")

# Step 1: Move Monkey to Box
if monkey_position != box_position:
    print("\nStep 1: Monkey moves from", monkey_position, "to", box_position)
    monkey_position = box_position
else:
    print("\nStep 1: Monkey is already near the box")

# Step 2: Push Box to Banana
if box_position != banana_position:
    print("Step 2: Monkey pushes the box from", box_position, "to", banana_position)
    box_position = banana_position
    monkey_position = banana_position
else:
    print("Step 2: Box is already under the banana")

# Step 3: Climb the Box
if monkey_on_box == "no":
    print("Step 3: Monkey climbs onto the box")
    monkey_on_box = "yes"
else:
    print("Step 3: Monkey is already on the box")

# Step 4: Grab the Banana
print("\n----- FINAL STATE -----")

if monkey_position == banana_position and monkey_on_box == "yes":
    print("Goal Achieved 🎉")
    print("Monkey successfully grabs the banana 🍌")
else:
    print("Goal Not Achieved ❌")
    print("Monkey could not get the banana")
