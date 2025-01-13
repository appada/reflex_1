"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    #todos = ['test1','투두를 만든다', '내일 위센터', '아침930까지도착']
    num: int
    num_list = [3, 2, 1]

    def add_num(self):
        self.num_list.insert(0, self.num_list[0] + 1)

    def set_num(self):
        self.num_list.insert(0, self.num)
        self.update_state()

    def pop_num(self, idx):
        self.num_list.pop(idx)


def index():

    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.form(
            rx.input(on_change=State.set_num),
            on_submit=lambda x: State.add_num(),
            reset_on_submit=True
        ),
        rx.hstack(
            rx.icon_button("plus", on_click=State.add_num),
            rx.foreach(State.num_list, render_delete)
        ),

        #rx.foreach(State.todos, render_fn),
    )

def render_fn(item):
    return rx.hstack(
        rx.icon_button("album", size = '1', bg='tomato' ),
        rx.text(item),
    )

def render_delete(item, idx):
    return rx.text(item, on_click=lambda: State.pop_num(idx))

app = rx.App()
app.add_page(index)
#
# rx.vstack(
#     rx.heading("Welcome to Reflex!", size="9"),
#     rx.text(State.todos),
#     rx.link(
#         rx.button("Check out our docs!"),
#         href="https://reflex.dev/docs/getting-started/introduction/",
#         is_external=True,
#     ),
#     spacing="5",
#     justify="center",
#     min_height="85vh",
# ),
# rx.logo(),
