from matplotlib.pyplot import title
import streamlit as st


class MultaApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.app.append({"title": title, "function": func})

    def run(self):
        app = st.sidebar.radio("Go To", self.apps, format_func=lambda app: app["title"])
        app["function"]()
