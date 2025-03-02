import flet as ft
import openpyxl
import os


EXCEL_FILE = "students_grades.xlsx"

def show_add_students(page: ft.Page):
    page.title = "Second View"
    
    def go_back_home(e):
        page.views.pop()  # Remove the current view (Second View)
        # Instead of importing, we will set up the home view directly
        page.clean()  # Clear the current view
        page.title = "Home View"
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        # Button to navigate to the second view
        navigate_button = ft.ElevatedButton(
            "Go to Second View",
            on_click=lambda e: show_add_students(page)  # Call the function to navigate
        )

        # Add the button to the main view
        page.add(navigate_button)
        print("Navigated back to Home View")

    add_students = ft.View(
        route="/second",
        controls=[
            ft.Text("This is the Second View!", size=20),
            ft.ElevatedButton("Go Back to Home", on_click=go_back_home)
        ]
    )

    def ensure_excel_file():
        """Ensure the Excel file exists with a proper structure."""
        if not os.path.exists(EXCEL_FILE):
            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = " Grades  "
            # Add headers for subjects in column A
            subjects = ["Matricule", "Name", "Maths", "Sciences", "Histoire", "Geo", "ECM", "Francais", "Anglais"]
            for row_num, subject in enumerate(subjects, start=1):
                ws.cell(row=row_num, column=1, value=subject)
            wb.save(EXCEL_FILE)

    page.views.append(add_students)
    page.go("/second")
