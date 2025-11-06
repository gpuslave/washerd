from nicegui import ui
from ui.theme import create_frame


def render():
    """Washing configurator page"""
    create_frame()

    with ui.column().classes("w-full p-8"):
        ui.label("Washing Configurator").classes("text-3xl font-bold mb-6")

        with ui.row().classes("w-full gap-8"):
            # Left panel - Clothes selection
            with ui.card().classes("flex-1"):
                ui.label("Select Dirty Clothes").classes(
                    "text-xl font-bold mb-4"
                )
                ui.label("Check the items you want to wash:").classes(
                    "text-sm text-gray-600 mb-4"
                )

                # Empty state
                with ui.column().classes("w-full items-center p-8"):
                    ui.icon("inbox", size="3rem").classes("text-gray-300 mb-2")
                    ui.label("No clothes available").classes(
                        "text-gray-400 italic"
                    )

            # Right panel - Info
            with ui.card().classes("flex-1"):
                ui.label("Selected Items").classes("text-xl font-bold mb-4")

                with ui.column().classes("w-full items-center p-8"):
                    ui.icon("check_circle_outline", size="3rem").classes(
                        "text-gray-300 mb-2"
                    )
                    ui.label("No items selected yet").classes(
                        "text-gray-400 italic"
                    )

        ui.separator().classes("my-6")

        # Analysis button
        ui.button(
            "Analyze & Generate Washing Plan",
            icon="psychology",
            on_click=lambda: ui.notify(
                "Please select items first", type="warning"
            ),
        ).classes("bg-green-600 text-lg")

        ui.separator().classes("my-6")

        # Results placeholder
        with ui.card().classes("w-full bg-gray-50"):
            with ui.column().classes("w-full items-center p-12"):
                ui.icon("pending_actions", size="4rem").classes(
                    "text-gray-300 mb-4"
                )
                ui.label("Washing plan will appear here").classes(
                    "text-xl text-gray-400 mb-2"
                )
                ui.label(
                    'Select clothes and click "Analyze" to generate a plan'
                ).classes("text-sm text-gray-400")
