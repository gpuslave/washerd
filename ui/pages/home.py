from nicegui import ui
from ui.theme import create_frame


def render():
    """Dashboard home page"""
    create_frame()

    with ui.column().classes("w-full p-8 items-center"):
        ui.label("Welcome to Washerd").classes("text-4xl font-bold mb-4")
        ui.label("Your smart clothes management system").classes(
            "text-xl text-gray-600 mb-8"
        )

        # Stats cards
        with ui.row().classes("gap-4 mb-8"):
            with ui.card().classes(
                "w-48 h-32 flex flex-col justify-center items-center bg-blue-50"
            ):
                ui.label("Total Clothes").classes("text-sm text-gray-600")
                ui.label("0").classes("text-4xl font-bold text-blue-600")

            with ui.card().classes(
                "w-48 h-32 flex flex-col justify-center items-center bg-green-50"
            ):
                ui.label("Washing Modes").classes("text-sm text-gray-600")
                ui.label("0").classes("text-4xl font-bold text-green-600")

            with ui.card().classes(
                "w-48 h-32 flex flex-col justify-center items-center bg-purple-50"
            ):
                ui.label("Ready to Wash").classes("text-sm text-gray-600")
                ui.label("0").classes("text-4xl font-bold text-purple-600")

        # Quick actions
        ui.label("Quick Actions").classes("text-2xl font-bold mb-4")
        with ui.row().classes("gap-4"):
            ui.button(
                "Add New Clothes",
                icon="add",
                on_click=lambda: ui.navigate.to("/clothes"),
            ).classes("bg-blue-600")
            ui.button(
                "Start Washing Session",
                icon="play_arrow",
                on_click=lambda: ui.navigate.to("/configurator"),
            ).classes("bg-green-600")
