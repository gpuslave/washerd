from nicegui import ui


def create_header():
    """navigation"""
    with ui.header().classes("items-center justify-between bg-blue-600"):
        ui.label("🧺 Washerd").classes("text-2xl font-bold")
        with ui.row().classes("gap-2"):
            ui.button("Home", icon="home", on_click=lambda: ui.navigate.to("/")).props(
                "flat color=white"
            )
            ui.button(
                "Clothes", icon="checkroom", on_click=lambda: ui.navigate.to("/clothes")
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


@ui.page("/")
def home_page():
    """Dashboard home page"""
    create_header()

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


@ui.page("/clothes")
def clothes_page():
    """Clothes database page"""
    create_header()

    with ui.column().classes("w-full p-8"):
        with ui.row().classes("w-full items-center justify-between mb-6"):
            ui.label("Clothes Database").classes("text-3xl font-bold")
            ui.button(
                "Add New Item", icon="add", on_click=lambda: add_clothes_dialog.open()
            ).classes("bg-blue-600")

        # Search bar
        ui.input(
            "Search clothes...", placeholder="Search by name, fabric, or color"
        ).classes("w-full mb-4").props("outlined")

        # Empty state
        with ui.column().classes("w-full items-center justify-center p-16"):
            ui.icon("checkroom", size="4rem").classes("text-gray-300 mb-4")
            ui.label("No clothes items yet").classes("text-xl text-gray-400 mb-2")
            ui.label("Add your first clothing item to get started").classes(
                "text-sm text-gray-400"
            )

    # Add clothes dialog
    with ui.dialog() as add_clothes_dialog, ui.card().classes("w-96"):
        ui.label("Add New Clothes").classes("text-xl font-bold mb-4")

        ui.input("Name", placeholder="e.g., White T-Shirt").classes("w-full")
        ui.input("Fabric Type", placeholder="e.g., Cotton").classes("w-full")
        ui.input("Color", placeholder="e.g., White").classes("w-full")
        ui.textarea("Description", placeholder="Optional details...").classes("w-full")

        ui.separator()

        ui.label("Care Labels").classes("font-semibold mt-4 mb-2")
        ui.select([], label="Temperature", with_input=True).classes("w-full")
        ui.select([], label="Wash Cycle", with_input=True).classes("w-full")
        ui.select([], label="Drying", with_input=True).classes("w-full")

        with ui.row().classes("w-full justify-end mt-4 gap-2"):
            ui.button("Cancel", on_click=add_clothes_dialog.close).props("flat")
            ui.button(
                "Add Item",
                on_click=lambda: [ui.notify("Item added!"), add_clothes_dialog.close()],
            ).classes("bg-blue-600")


@ui.page("/configurator")
def configurator_page():
    """Washing configurator page"""
    create_header()

    with ui.column().classes("w-full p-8"):
        ui.label("Washing Configurator").classes("text-3xl font-bold mb-6")

        with ui.row().classes("w-full gap-8"):
            # Left panel - Clothes selection
            with ui.card().classes("flex-1"):
                ui.label("Select Dirty Clothes").classes("text-xl font-bold mb-4")
                ui.label("Check the items you want to wash:").classes(
                    "text-sm text-gray-600 mb-4"
                )

                # Empty state
                with ui.column().classes("w-full items-center p-8"):
                    ui.icon("inbox", size="3rem").classes("text-gray-300 mb-2")
                    ui.label("No clothes available").classes("text-gray-400 italic")

            # Right panel - Info
            with ui.card().classes("flex-1"):
                ui.label("Selected Items").classes("text-xl font-bold mb-4")

                with ui.column().classes("w-full items-center p-8"):
                    ui.icon("check_circle_outline", size="3rem").classes(
                        "text-gray-300 mb-2"
                    )
                    ui.label("No items selected yet").classes("text-gray-400 italic")

        ui.separator().classes("my-6")

        # Analysis button
        ui.button(
            "Analyze & Generate Washing Plan",
            icon="psychology",
            on_click=lambda: ui.notify("Please select items first", type="warning"),
        ).classes("bg-green-600 text-lg")

        ui.separator().classes("my-6")

        # Results placeholder
        with ui.card().classes("w-full bg-gray-50"):
            with ui.column().classes("w-full items-center p-12"):
                ui.icon("pending_actions", size="4rem").classes("text-gray-300 mb-4")
                ui.label("Washing plan will appear here").classes(
                    "text-xl text-gray-400 mb-2"
                )
                ui.label(
                    'Select clothes and click "Analyze" to generate a plan'
                ).classes("text-sm text-gray-400")


@ui.page("/machines")
def machines_page():
    """Washing machine configuration page"""
    create_header()

    with ui.column().classes("w-full p-8"):
        with ui.row().classes("w-full items-center justify-between mb-6"):
            ui.label("Washing Machine Modes").classes("text-3xl font-bold")
            ui.button(
                "Add Mode", icon="add", on_click=lambda: add_mode_dialog.open()
            ).classes("bg-blue-600")

        # Empty state
        with ui.column().classes("w-full items-center justify-center p-16"):
            ui.icon("local_laundry_service", size="4rem").classes("text-gray-300 mb-4")
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
        ui.number("Spin Speed (RPM)", value=1200, min=0, max=1600).classes("w-full")
        ui.number("Duration (minutes)", value=90, min=15, max=240).classes("w-full")

        with ui.row().classes("w-full justify-end mt-4 gap-2"):
            ui.button("Cancel", on_click=add_mode_dialog.close).props("flat")
            ui.button(
                "Add Mode",
                on_click=lambda: [ui.notify("Mode added!"), add_mode_dialog.close()],
            ).classes("bg-blue-600")


# def main():
#   return 0

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(
        host="127.0.0.1",
        port=8080,
        title="Washerd",
        reload=True,
        show=True,
    )

    # main()
