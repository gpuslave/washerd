from nicegui import ui
from ui.pages import home, clothes, configurator, machines


@ui.page("/")
def home_page():
    home.render()


@ui.page("/clothes")
def clothes_page():
    clothes.render()


@ui.page("/configurator")
def configurator_page():
    configurator.render()


@ui.page("/machines")
def machines_page():
    machines.render()


if __name__ in {"__main__", "__mp_main__"}:
    ui.run(
        host="127.0.0.1",
        port=8080,
        title="Washerd",
        reload=True,
        show=True,
    )
