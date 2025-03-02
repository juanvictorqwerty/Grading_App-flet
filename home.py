import flet as ft
from add_students import show_add_students  # Import the second view

def main(page: ft.Page):
    page.title = "Home View"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Function to navigate to the second view
    def go_to_second_view(e):
        page.clean()  # Clear the current view
        show_add_students(page)  # Show the second view

    # Button to navigate to the second view
    navigate_button = ft.ElevatedButton(
        "Go to Second View",
        on_click=go_to_second_view  # Call the function to navigate
    )

    # Add the button to the main view
    page.add(navigate_button)

# Run the app
ft.app(target=main)