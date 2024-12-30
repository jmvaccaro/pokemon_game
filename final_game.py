import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np

# Create the main window
screen = tk.Tk()
screen.title("Pokémon Rock, Paper, Scissors")
screen.geometry("700x800")
screen.config(bg="#006400")  # Dark green background

# Global variables
rival_choice = ""
your_choice = ""
types = ["Fire", "Water", "Leaf"]
player1_score = 0
player2_score = 0
round_counter = 1
max_victories = 3  # Number of victories needed to win


# Function to show the victory message
def show_winner():
    global round_counter
    # Show the Pokémon images before ending the game
    update_rival_image()
    if player1_score >= max_victories:
        messagebox.showinfo("Winner", "Player 1 wins the game!")
    elif player2_score >= max_victories:
        messagebox.showinfo("Winner", "Player 2 wins the game!")
    else:
        messagebox.showinfo("Result", "It's a tie!")
    # Stop the game
    continue_button.config(state="disabled")


# Functions for each type choice
def choose_fire():
    global your_choice, rival_choice, player1_score, player2_score
    your_choice = "Fire"
    rival_choice = types[np.random.randint(0, 3)]
    if rival_choice == "Water":
        player2_score += 1
    elif rival_choice == "Leaf":
        player1_score += 1
    update_scores()


def choose_water():
    global your_choice, rival_choice, player1_score, player2_score
    your_choice = "Water"
    rival_choice = types[np.random.randint(0, 3)]
    if rival_choice == "Leaf":
        player2_score += 1
    elif rival_choice == "Fire":
        player1_score += 1
    update_scores()


def choose_leaf():
    global your_choice, rival_choice, player1_score, player2_score
    your_choice = "Leaf"
    rival_choice = types[np.random.randint(0, 3)]
    if rival_choice == "Fire":
        player2_score += 1
    elif rival_choice == "Water":
        player1_score += 1
    update_scores()


# Function to update the scores, rounds, and show the rival Pokémon
def update_scores():
    global round_counter
    player1_label.config(text="Player 1: " + "★" * player1_score)
    player2_label.config(text="Player 2: " + "★" * player2_score)

    round_label.config(text=f"Round {round_counter}: Choose your Pokémon")

    if player1_score >= max_victories or player2_score >= max_victories:
        show_winner()
    else:
        # Show the rival's image
        update_rival_image()
        # Disable choice buttons until "Continue" is pressed
        disable_choice_buttons(True)
        # Enable the "Continue" button
        continue_button.config(state="normal")


# Function to update the rival's image based on their choice
def update_rival_image():
    # Clear images before the new round
    rival_image_label.config(image="")
    your_image_label.config(image="")

    if your_choice == "Fire":
        your_image_label.config(image=fire_image)
    elif your_choice == "Water":
        your_image_label.config(image=water_image)
    elif your_choice == "Leaf":
        your_image_label.config(image=leaf_image)

    if rival_choice == "Fire":
        rival_image_label.config(image=fire_image)
    elif rival_choice == "Water":
        rival_image_label.config(image=water_image)
    elif rival_choice == "Leaf":
        rival_image_label.config(image=leaf_image)


# Resize images to fit the button size
def resize_image(image_path, size=(100, 100)):
    img = Image.open(image_path)
    img = img.resize(size, Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)


# Resize the images
fire_image = resize_image("charmander.png")  # Replace with the image path
water_image = resize_image("squirtle.png")
leaf_image = resize_image("bulbasaur.png")
pokemon_title_image = resize_image("pokemon_title.png", size=(200, 70))  # Title image

# Create a top frame for the buttons and title
top_frame = tk.Frame(screen, bg="#006400")
top_frame.grid(row=0, column=0, padx=20, pady=20)

# Title image
title_label = tk.Label(top_frame, image=pokemon_title_image, bg="#006400")
title_label.grid(row=0, column=0, pady=10, columnspan=3)

# Choice buttons with images (making them smaller)
fire_button = tk.Button(top_frame, text="Fire", image=fire_image, compound=tk.TOP, command=choose_fire,
                        relief="raised", bg="orange", font=("Arial", 14), width=150, height=150)
fire_button.grid(row=1, column=0, padx=20, pady=10)

water_button = tk.Button(top_frame, text="Water", image=water_image, compound=tk.TOP, command=choose_water,
                         relief="raised", bg="lightblue", font=("Arial", 14), width=150, height=150)
water_button.grid(row=1, column=1, padx=20, pady=10)

leaf_button = tk.Button(top_frame, text="Leaf", image=leaf_image, compound=tk.TOP, command=choose_leaf,
                        relief="raised", bg="lightgreen", font=("Arial", 14), width=150, height=150)
leaf_button.grid(row=1, column=2, padx=20, pady=10)

# Create a bottom frame for the round elements, scores, and continue button (fixed)
bottom_frame = tk.Frame(screen, bg="#006400")
bottom_frame.grid(row=4, column=0, padx=20, pady=20, sticky="s")  # Ensures it stays at the bottom

# Label to show the player's chosen Pokémon (top)
your_image_label = tk.Label(bottom_frame, bg="#006400")
your_image_label.grid(row=3, column=3, pady=5)

# Label to show the rival's chosen Pokémon (bottom)
rival_image_label = tk.Label(bottom_frame, bg="#006400")
rival_image_label.grid(row=4, column=3, pady=5)

# Label to show the current round
round_label = tk.Label(bottom_frame, text=f"Round {round_counter}: Choose your Pokémon", font=("Arial", 16), bg="#006400",
                       fg="white")
round_label.grid(row=2, column=0, columnspan=2, pady=10)

# Score labels (one above the other)
player1_label = tk.Label(bottom_frame, text="Player 1: " + "★" * player1_score, font=("Arial", 16), bg="#006400",
                         fg="white")
player1_label.grid(row=3, column=0, pady=5)

player2_label = tk.Label(bottom_frame, text="Player 2: " + "★" * player2_score, font=("Arial", 16), bg="#006400",
                         fg="white")
player2_label.grid(row=4, column=0, pady=5)


# Function to continue to the next round
def continue_round():
    global round_counter
    # Clear images and re-enable choice buttons
    rival_image_label.config(image="")
    your_image_label.config(image="")
    continue_button.config(state="disabled")
    disable_choice_buttons(False)
    round_counter += 1
    round_label.config(text=f"Round {round_counter}: Choose your Pokémon")


# Function to enable or disable the choice buttons
def disable_choice_buttons(state):
    fire_button.config(state="disabled" if state else "normal")
    water_button.config(state="disabled" if state else "normal")
    leaf_button.config(state="disabled" if state else "normal")


# Button to continue to the next round
continue_button = tk.Button(screen, text="Continue", command=continue_round, state="disabled", font=("Arial", 14))
continue_button.grid(row=2, column=0, columnspan=2, pady=20)

# Run the interface
screen.mainloop()