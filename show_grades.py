import flet as ft
import openpyxl
import os


def show_show_grades(page: ft.Page):
    page.title = "Grades View"
    
    def go_back_home(e):
        page.views.pop()  # Remove the current view (Second View)
        # Instead of importing, we will set up the home view directly
        page.clean()  # Clear the current view
        page.title = "Home View"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        # Button to navigate to the second view
        navigate_button = ft.ElevatedButton(
            "See grades",
            on_click=lambda e: show_show_grades(page)  # Call the function to navigate
        )

        # Add the button to the main view
        page.add(navigate_button)
        print("Navigated back to Home View")

    show_grades = ft.View(
        route="/second",
        controls=[
            ft.Text("This is the Second View!", size=20),
            ft.ElevatedButton("Go Back to Home", on_click=go_back_home)
        ]
    )

    page.views.append(show_grades)
    page.go("/second")