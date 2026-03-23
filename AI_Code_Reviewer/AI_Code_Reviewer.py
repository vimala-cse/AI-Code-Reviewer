import reflex as rx
from AI_Code_Reviewer.components.navbar import navbar
from AI_Code_Reviewer.components.hero import hero
from AI_Code_Reviewer.components.footer import footer
from AI_Code_Reviewer.components.analyze import analyze_page
from AI_Code_Reviewer.components.about import about_page
from AI_Code_Reviewer.components.login import login_page
from AI_Code_Reviewer.components.signup import signup_page
from AI_Code_Reviewer.state import AppState

def home():
    return rx.box(
        navbar(),
        hero(),
        footer(),
        background_color=rx.cond(
            AppState.is_dark,
            "#0f0f1a",
            "#ffffff",
        ),
        min_height="100vh",
    )

def analyze():
    return rx.box(
        navbar(),
        analyze_page(),
        footer(),
        background_color=rx.cond(
            AppState.is_dark,
            "#0f0f1a",
            "#ffffff",
        ),
        min_height="100vh",
    )

def about():
    return rx.box(
        navbar(),
        about_page(),
        footer(),
        background_color=rx.cond(
            AppState.is_dark,
            "#0f0f1a",
            "#ffffff",
        ),
        min_height="100vh",
    )

def login():
    return rx.box(
        navbar(),
        login_page(),
        background_color=rx.cond(
            AppState.is_dark,
            "#0f0f1a",
            "#f0f4ff",
        ),
        min_height="100vh",
    )

def signup():
    return rx.box(
        navbar(),
        signup_page(),
        background_color=rx.cond(
            AppState.is_dark,
            "#0f0f1a",
            "#f0f4ff",
        ),
        min_height="100vh",
    )

app = rx.App()
app.add_page(home, route="/")
app.add_page(analyze, route="/analyze")
app.add_page(about, route="/about")
app.add_page(login, route="/login")
app.add_page(signup, route="/signup")