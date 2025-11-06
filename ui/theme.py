from nicegui import ui


def create_frame():
    """navigation"""
    with ui.header().classes("items-center justify-between bg-blue-600"):
        ui.label("🧺 Washerd").classes("text-2xl font-bold")
        with ui.row().classes("gap-2"):
            ui.button(
                "Home", icon="home", on_click=lambda: ui.navigate.to("/")
            ).props("flat color=white")
            ui.button(
                "Clothes",
                icon="checkroom",
                on_click=lambda: ui.navigate.to("/clothes"),
            ).props("flat color=white")
            ui.button(
                "Configurator",
                icon="settings",
                on_click=lambda: ui.navigate.to("/configurator"),
            ).props("flat color=white")
            ui.button(
                "Machines",
                icon="local_laundry_service",
                on_click=lambda: ui.navigate.to("/machines"),
            ).props("flat color=white")
