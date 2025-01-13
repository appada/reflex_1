import reflex as rx


class State(rx.State):
    todo = ["씻기", "아침먹기", "옷입기", "출근하기"]



def render_fn(item):
    return rx.hstack(
        rx.icon_button("circle_check_big", size="1", bg="tomato"),
        rx.text(item),
    )

def index():
    return rx.container(
        rx.foreach(State.todo, render_fn)
    )


app = rx.App()
app.add_page(index)
