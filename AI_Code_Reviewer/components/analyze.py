import reflex as rx
from AI_Code_Reviewer.state import AppState

def analyze_page():
    return rx.box(
        rx.vstack(

            # 🔹 Page title
            rx.heading(
                "Analyze Your Code",
                size="8",
                color=rx.cond(AppState.is_dark, "white", "#1a1a2e"),
            ),
            rx.text(
                "Paste your code below and get instant AI feedback.",
                color=rx.cond(AppState.is_dark, "#aaa", "#555"),
                font_size="1em",
            ),

            # 🔹 Code input area
            rx.text_area(
                value=AppState.code_input,
                on_change=AppState.set_code,
                placeholder="Paste your code here...",
                _placeholder={"color": "#aaa"},
                width="100%",
                height="300px",
                font_family="monospace",
                font_size="0.95em",
                background_color=rx.cond(
                    AppState.is_dark, "#2d2d44", "#f8f9fa"
                ),
                color=rx.cond(AppState.is_dark, "#ffffff", "#1a1a2e"),
                border=rx.cond(
                    AppState.is_dark,
                    "1px solid #444",
                    "1px solid #ddd",
                ),
                border_radius="8px",
                padding="16px",
            ),

            # 🔹 Analyze button
            rx.hstack(
                rx.button(
                    rx.text("Analyze Code"),
                    on_click=AppState.analyze_code,
                    background_color="#60a5fa",
                    color="white",
                    padding="12px 32px",
                    border_radius="8px",
                    font_size="1em",
                    _hover={"background_color": "#3b82f6"},
                ),
                spacing="4",
                align="center",
            ),

            # 🔹 Loading animation
            rx.cond(
                AppState.is_loading,
                rx.box(
                    rx.vstack(
                        rx.spinner(size="3", color="#60a5fa"),
                        rx.text(
                            "Analyzing your code...",
                            color="#60a5fa",
                            font_size="1em",
                        ),
                        align="center",
                        spacing="3",
                    ),
                    width="100%",
                    padding="20px",
                    display="flex",
                    justify_content="center",
                ),
            ),

            # 🔹 Results box
            rx.cond(
                AppState.result != "",
                rx.box(
                    rx.text(
                        AppState.result,
                        color=rx.cond(AppState.is_dark, "#aaa", "#555"),
                        font_size="1em",
                        white_space="pre-wrap",
                    ),
                    width="100%",
                    padding="20px",
                    background_color=rx.cond(
                        AppState.is_dark, "#2d2d44", "#f8f9fa"
                    ),
                    border_radius="8px",
                    border=rx.cond(
                        AppState.is_dark,
                        "1px solid #444",
                        "1px solid #ddd",
                    ),
                    min_height="100px",
                ),
            ),

            # 🔹 2 Column layout
            rx.cond(
                AppState.result != "",
                rx.flex(

                    # Left - Your Code
                    rx.vstack(
                        rx.text(
                            "Your Code",
                            font_weight="bold",
                            color=rx.cond(AppState.is_dark, "white", "#1a1a2e"),
                            font_size="1em",
                        ),
                        rx.box(
                            rx.text(
                                AppState.code_input,
                                font_family="monospace",
                                font_size="0.9em",
                                color=rx.cond(AppState.is_dark, "#ffffff", "#1a1a2e"),
                                white_space="pre-wrap",
                            ),
                            width="100%",
                            padding="16px",
                            background_color=rx.cond(
                                AppState.is_dark, "#2d2d44", "#f8f9fa"
                            ),
                            border_radius="8px",
                            border=rx.cond(
                                AppState.is_dark,
                                "1px solid #444",
                                "1px solid #ddd",
                            ),
                            min_height="200px",
                        ),
                        width="48%",
                        align_items="start",
                        spacing="2",
                    ),

                    # Right - Corrected Code + Copy button
                    rx.vstack(
                        rx.hstack(
                            rx.text(
                                "Corrected Code",
                                font_weight="bold",
                                color="#60a5fa",
                                font_size="1em",
                            ),
                            rx.cond(
                                AppState.corrected_code != "",
                                rx.button(
                                    rx.hstack(
                                        rx.icon("copy", size=14),
                                        rx.text("Copy", font_size="0.8em"),
                                        spacing="1",
                                        align="center",
                                    ),
                                    on_click=rx.set_clipboard(AppState.corrected_code),
                                    background_color="transparent",
                                    border="1px solid #60a5fa",
                                    color="#60a5fa",
                                    border_radius="6px",
                                    padding="4px 10px",
                                    _hover={"background_color": "#60a5fa", "color": "white"},
                                ),
                            ),
                            justify="between",
                            width="100%",
                            align="center",
                        ),
                        rx.box(
                            rx.text(
                                rx.cond(
                                    AppState.corrected_code != "",
                                    AppState.corrected_code,
                                    "Corrected code will appear here...",
                                ),
                                font_family="monospace",
                                font_size="0.9em",
                                color=rx.cond(AppState.is_dark, "#c3e88d", "#1a1a2e"),
                                white_space="pre-wrap",
                            ),
                            width="100%",
                            padding="16px",
                            background_color=rx.cond(
                                AppState.is_dark, "#1a2d1a", "#f0fff0"
                            ),
                            border_radius="8px",
                            border=rx.cond(
                                AppState.is_dark,
                                "1px solid #3a5a3a",
                                "1px solid #90ee90",
                            ),
                            min_height="200px",
                        ),
                        width="48%",
                        align_items="start",
                        spacing="2",
                    ),

                    justify="between",
                    width="100%",
                    spacing="4",
                ),
            ),

            width="100%",
            max_width="1000px",
            spacing="5",
            padding="40px 20px",
            align_items="start",
        ),
        display="flex",
        justify_content="center",
        width="100%",
        background_color=rx.cond(
            AppState.is_dark, "#0f0f1a", "#ffffff"
        ),
        min_height="100vh",
    )