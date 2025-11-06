from nicegui import ui
from ui.theme import create_frame


def render():
    """Clothes database page"""
    create_frame()
    add_clothes_dialog = _create_add_clothes_dialog()

    with ui.column().classes("w-full p-8"):
        with ui.row().classes("w-full items-center justify-between mb-6"):
            ui.label("Clothes Database").classes("text-3xl font-bold")
            ui.button(
                "Add New Item",
                icon="add",
                on_click=lambda: add_clothes_dialog.open(),
            ).classes("bg-blue-600")

        # Search bar
        ui.input(
            "Search clothes...", placeholder="Search by name, fabric, or color"
        ).classes("w-full mb-4").props("outlined")

        # Empty state
        with ui.column().classes("w-full items-center justify-center p-16"):
            ui.icon("checkroom", size="4rem").classes("text-gray-300 mb-4")
            ui.label("No clothes items yet").classes(
                "text-xl text-gray-400 mb-2"
            )
            ui.label("Add your first clothing item to get started").classes(
                "text-sm text-gray-400"
            )


def _create_add_clothes_dialog():
    with ui.dialog() as add_clothes_dialog, ui.card().classes("w-96"):
        ui.label("Add New Clothes").classes("text-xl font-bold mb-4")

        ui.input("Name", placeholder="e.g., White T-Shirt").classes("w-full")
        ui.input("Fabric Type", placeholder="e.g., Cotton").classes("w-full")
        ui.input("Color", placeholder="e.g., White").classes("w-full")
        ui.textarea("Description", placeholder="Optional details...").classes(
            "w-full"
        )

        ui.separator()

        ui.label("Care Labels").classes("font-semibold mt-4 mb-2")
        ui.select([], label="Temperature", with_input=True).classes("w-full")
        ui.select([], label="Wash Cycle", with_input=True).classes("w-full")
        ui.select([], label="Drying", with_input=True).classes("w-full")

        with ui.row().classes("w-full justify-end mt-4 gap-2"):
            ui.button("Cancel", on_click=add_clothes_dialog.close).props("flat")
            ui.button(
                "Add Item",
                on_click=lambda: [
                    ui.notify("Item added!"),
                    add_clothes_dialog.close(),
                ],
            ).classes("bg-blue-600")
    return add_clothes_dialog
