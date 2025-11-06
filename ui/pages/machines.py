from nicegui import ui
from ui.theme import create_frame


def render():
    """Washing machine configuration page"""
    create_frame()

    with ui.column().classes("w-full p-8"):
        with ui.row().classes("w-full items-center justify-between mb-6"):
            ui.label("Washing Machine Modes").classes("text-3xl font-bold")
            ui.button(
                "Add Mode", icon="add", on_click=lambda: add_mode_dialog.open()
            ).classes("bg-blue-600")

        # Empty state
        with ui.column().classes("w-full items-center justify-center p-16"):
            ui.icon("local_laundry_service", size="4rem").classes(
                "text-gray-300 mb-4"
            )
            ui.label("No washing modes configured").classes(
                "text-xl text-gray-400 mb-2"
            )
            ui.label("Add your washing machine modes to get started").classes(
                "text-sm text-gray-400"
            )

    # Add mode dialog
    with ui.dialog() as add_mode_dialog, ui.card().classes("w-96"):
        ui.label("Add Washing Mode").classes("text-xl font-bold mb-4")

        ui.input("Mode Name", placeholder="e.g., Cotton 60°C").classes("w-full")
        ui.number("Temperature (°C)", value=40, min=0, max=95).classes("w-full")
        ui.number("Spin Speed (RPM)", value=1200, min=0, max=1600).classes(
            "w-full"
        )
        ui.number("Duration (minutes)", value=90, min=15, max=240).classes(
            "w-full"
        )

        with ui.row().classes("w-full justify-end mt-4 gap-2"):
            ui.button("Cancel", on_click=add_mode_dialog.close).props("flat")
            ui.button(
                "Add Mode",
                on_click=lambda: [
                    ui.notify("Mode added!"),
                    add_mode_dialog.close(),
                ],
            ).classes("bg-blue-600")
