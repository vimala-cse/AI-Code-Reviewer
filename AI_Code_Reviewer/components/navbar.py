import reflex as rx
from AI_Code_Reviewer.state import AppState

def nav_link(text: str, href: str) -> rx.Component:
    return rx.link(
        text,
        href=href,
        color=rx.cond(
            rx.State.router.page.path == href,
            "#60a5fa",
            rx.cond(AppState.is_dark, "white", "#1a1a2e"),
        ),
        font_weight=rx.cond(
            rx.State.router.page.path == href,
            "bold",
            "normal",
        ),
        text_decoration="none",
        _hover={"color": "#60a5fa"},
    )

def navbar():
    return rx.flex(

        # 🔹 Left - Logo
        rx.link(
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
            href="/",
            text_decoration="none",
        ),

        # 🔹 Right - Nav links + Login + Signup + Toggle
        rx.hstack(
            nav_link("Home", "/"),
            nav_link("Analyze", "/analyze"),
            nav_link("History", "/history"),
            nav_link("About", "/about"),

            # Divider
            rx.divider(
                orientation="vertical",
                height="20px",
                border_color=rx.cond(AppState.is_dark, "#444", "#ccc"),
            ),

            # Login button
            rx.link(
                rx.button(
                    "Login",
                    background_color="transparent",
                    color=rx.cond(AppState.is_dark, "white", "#1a1a2e"),
                    border=rx.cond(
                        AppState.is_dark,
                        "1px solid #444",
                        "1px solid #ccc",
                    ),
                    border_radius="8px",
                    padding="6px 16px",
                    font_size="0.9em",
                    _hover={"border_color": "#60a5fa", "color": "#60a5fa"},
                ),
                href="/login",
                text_decoration="none",
            ),

            # Sign Up button
            rx.link(
                rx.button(
                    "Sign Up",
                    background_color="#60a5fa",
                    color="white",
                    border_radius="8px",
                    padding="6px 16px",
                    font_size="0.9em",
                    _hover={"background_color": "#3b82f6"},
                ),
                href="/signup",
                text_decoration="none",
            ),

            # 🌙☀️ Toggle button
            rx.button(
                rx.cond(
                    AppState.is_dark,
                    rx.icon("sun", color="white", size=20),
                    rx.icon("moon", color="#1a1a2e", size=20),
                ),
                on_click=AppState.toggle_theme,
                background_color="transparent",
                border="none",
                cursor="pointer",
                padding="4px",
                _hover={"opacity": "0.7"},
            ),

            spacing="6",
            align="center",
        ),

        justify="between",
        align="center",
        width="100%",
        padding="16px 32px",
        background_color=rx.cond(
            AppState.is_dark,
            "rgba(26, 26, 46, 0.95)",
            "rgba(240, 244, 255, 0.95)",
        ),
    )