import turtle

# Function to display a pop-up window with text
def show_popup(message):
    # Create a turtle screen
    screen = turtle.Screen()

    # Use textinput to create a pop-up window with a text input field
    user_input = turtle.textinput("Pop-up Window", message)

    # Display the user input in the console
    print("User input:", user_input)

    # Close the turtle screen
    screen.bye()

# Example usage
message = "Enter something:"
show_popup(message)
