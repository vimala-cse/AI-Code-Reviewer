import reflex as rx
from AI_Code_Reviewer.state import AppState

def signup_page():
    return rx.box(

        rx.box(
            rx.vstack(

                # Logo + Title
                rx.hstack(
                    rx.image(
                        src="Chat-bot-rafiki.png",
                        width="40px",
                        height="40px",
                    ),
                    rx.text(
                        "AI Code Reviewer",
                        font_size="1.2em",
                        font_weight="bold",
                        color=rx.cond(AppState.is_dark, "white", "#1a1a2e"),
                    ),
                    spacing="2",
                    align="center",
                ),

                rx.text(
                    "Create Account",
                    font_size="1.8em",
                    font_weight="bold",
                    color=rx.cond(AppState.is_dark, "white", "#1a1a2e"),
                ),
                rx.text(
                    "Sign up to start reviewing your code.",
                    color=rx.cond(AppState.is_dark, "#888", "#555"),
                    font_size="0.95em",
                ),

                rx.divider(border_color=rx.cond(AppState.is_dark, "#333", "#ddd")),

                # Name field
                rx.vstack(
                    rx.text(
                        "Full Name",
                        color=rx.cond(AppState.is_dark, "#aaa", "#555"),
                        font_size="0.9em",
                        font_weight="bold",
                    ),
                    rx.input(
                        placeholder="Enter your full name",
                        type="text",
                        width="100%",
                        height="45px",
                        padding="0px 12px",
                        border_radius="8px",
                        background_color=rx.cond(
                            AppState.is_dark, "#1e1e2e", "#f8f9fa"
                        ),
                        color=rx.cond(AppState.is_dark, "white", "#1a1a2e"),
                        border=rx.cond(
                            AppState.is_dark,
                            "1px solid #444",
                            "1px solid #ccc",
                        ),
                        _placeholder={"color": "#444"},
                        _focus={"border": "1px solid #60a5fa", "outline": "none"},
                    ),
                    align_items="start",
                    width="100%",
                    spacing="1",
                ),

                # Email field
                rx.vstack(
                    rx.text(
                        "Email",
                        color=rx.cond(AppState.is_dark, "#aaa", "#555"),
                        font_size="0.9em",
                        font_weight="bold",
                    ),
                    rx.input(
                        placeholder="Enter your email",
                        type="email",
                        width="100%",
                        height="45px",
                        padding="0px 12px",
                        border_radius="8px",
                        background_color=rx.cond(
                            AppState.is_dark, "#1e1e2e", "#f8f9fa"
                        ),
                        color=rx.cond(AppState.is_dark, "white", "#1a1a2e"),
                        border=rx.cond(
                            AppState.is_dark,
                            "1px solid #444",
                            "1px solid #ccc",
                        ),
                        _placeholder={"color": "#444"},
                        _focus={"border": "1px solid #60a5fa", "outline": "none"},
                    ),
                    align_items="start",
                    width="100%",
                    spacing="1",
                ),

                # Password field
                rx.vstack(
                    rx.text(
                        "Password",
                        color=rx.cond(AppState.is_dark, "#aaa", "#555"),
                        font_size="0.9em",
                        font_weight="bold",
                    ),
                    rx.input(
                        placeholder="Enter your password",
                        type="password",
                        width="100%",
                        height="45px",
                        padding="0px 12px",
                        border_radius="8px",
                        background_color=rx.cond(
                            AppState.is_dark, "#1e1e2e", "#f8f9fa"
                        ),
                        color=rx.cond(AppState.is_dark, "white", "#1a1a2e"),
                        border=rx.cond(
                            AppState.is_dark,
                            "1px solid #444",
                            "1px solid #ccc",
                        ),
                        _placeholder={"color": "#444"},
                        _focus={"border": "1px solid #60a5fa", "outline": "none"},
                    ),
                    align_items="start",
                    width="100%",
                    spacing="1",
                ),

                # Signup button
                rx.button(
                    "Create Account",
                    width="100%",
                    background_color="#60a5fa",
                    color="white",
                    height="45px",
                    border_radius="8px",
                    font_size="1em",
                    font_weight="bold",
                    _hover={"background_color": "#3b82f6"},
                ),

                # Login link
                rx.hstack(
                    rx.text(
                        "Already have an account?",
                        color=rx.cond(AppState.is_dark, "#888", "#555"),
                        font_size="0.9em",
                    ),
                    rx.link(
                        "Login",
                        href="/login",
                        color="#60a5fa",
                        font_size="0.9em",
                        font_weight="bold",
                        _hover={"color": "#3b82f6"},
                    ),
                    spacing="2",
                    align="center",
                ),

                spacing="5",
                width="100%",
                align_items="start",
            ),
            background_color=rx.cond(
                AppState.is_dark, "#13132b", "white"
            ),
            border_radius="16px",
            padding="40px",
            width="420px",
            box_shadow="0 8px 32px rgba(0,0,0,0.2)",
            border=rx.cond(
                AppState.is_dark,
                "1px solid #333",
                "1px solid #eee",
            ),
        ),

        display="flex",
        justify_content="center",
        align_items="center",
        width="100%",
        min_height="100vh",
        background_color=rx.cond(
            AppState.is_dark, "#0f0f1a", "#f0f4ff"
        ),
    )