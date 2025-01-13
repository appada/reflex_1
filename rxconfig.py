# rxconfig.py
import reflex as rx

config = rx.Config(
    app_name="chat_app",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)