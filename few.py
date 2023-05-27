# Import the required libraries
import pyautogui
import random
import time

# Function to generate a random float each time and type the given text.
def type_with_random_interval(text):
    time.sleep(3)
    for char in text:
        pyautogui.press(char)
        interval = random.uniform(0.02, 0.45)
        pyautogui.PAUSE = interval


# Get the text from the user
user_input = input("Enter the text to be typed: ")

# Call the function
type_with_random_interval(user_input)
