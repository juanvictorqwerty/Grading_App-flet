import flet as ft
from add_students import show_add_students  # Import the second view
from show_grades import show_show_grades  # Import the third view

def main(page: ft.Page):
    page.title = "Home View"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Function to navigate to the second view
    def go_to_add_students(e):
        page.clean()  # Clear the current view
        show_add_students(page)  # Show the second view
    # Button to navigate to the second view
    navigate_button = ft.ElevatedButton(
        "Add Students",
        on_click=go_to_add_students  # Call the function to navigate
    )
    
    def go_to_show_grades(e):
        page.clean()
        show_show_grades(page)
    navigate_button2 = ft.ElevatedButton(
        "Show Grades",
        on_click=go_to_show_grades
    )
    # Add the button to the main view
    page.add(navigate_button ,navigate_button2)

# Run the app
ft.app(target=main)