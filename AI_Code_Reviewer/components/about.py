import reflex as rx
from AI_Code_Reviewer.state import AppState

def about_page():
    return rx.box(
        rx.vstack(

            # 🔹 Mission
            rx.vstack(
                rx.text(
                    "Our Mission",
                    font_size="0.9em",
                    font_weight="bold",
                    color="#60a5fa",
                    text_transform="uppercase",
                    letter_spacing="2px",
                ),
                rx.heading(
                    "Making Code Review Accessible",
                    size="8",
                    color=rx.cond(AppState.is_dark, "white", "#1a1a2e"),
                    text_align="center",
                ),
                rx.text(
                    "AI Code Reviewer helps every developer write better code — "
                    "faster, smarter, and with instant AI-powered feedback.",
                    color=rx.cond(AppState.is_dark, "#888", "#555"),
                    font_size="1.1em",
                    text_align="center",
                    max_width="600px",
                ),
                align_items="center",
                spacing="3",
                width="100%",
            ),

            rx.divider(border_color=rx.cond(AppState.is_dark, "#333", "#ddd"), width="100%"),

            # 🔹 Stats - 3 boxes
            rx.flex(
                # Stat 1
                rx.vstack(
                    rx.icon("zap", color="#60a5fa", size=36),
                    rx.text(
                        "Instant",
                        font_size="1.3em",
                        font_weight="bold",
                        color=rx.cond(AppState.is_dark, "white", "#1a1a2e"),
                    ),
                    rx.text(
                        "Results in seconds",
                        color=rx.cond(AppState.is_dark, "#888", "#555"),
                        font_size="0.9em",
                    ),
                    align_items="center",
                    spacing="2",
                    padding="30px",
                    background_color=rx.cond(AppState.is_dark, "#13132b", "#f8f9fa"),
                    border_radius="12px",
                    width="200px",
                ),
                # Stat 2
                rx.vstack(
                    rx.icon("brain", color="#60a5fa", size=36),
                    rx.text(
                        "AI Powered",
                        font_size="1.3em",
                        font_weight="bold",
                        color=rx.cond(AppState.is_dark, "white", "#1a1a2e"),
                    ),
                    rx.text(
                        "Smart suggestions",
                        color=rx.cond(AppState.is_dark, "#888", "#555"),
                        font_size="0.9em",
                    ),
                    align_items="center",
                    spacing="2",
                    padding="30px",
                    background_color=rx.cond(AppState.is_dark, "#13132b", "#f8f9fa"),
                    border_radius="12px",
                    width="200px",
                ),
                # Stat 3
                rx.vstack(
                    rx.icon("shield_check", color="#60a5fa", size=36),
                    rx.text(
                        "Accurate",
                        font_size="1.3em",
                        font_weight="bold",
                        color=rx.cond(AppState.is_dark, "white", "#1a1a2e"),
                    ),
                    rx.text(
                        "Reliable results",
                        color=rx.cond(AppState.is_dark, "#888", "#555"),
                        font_size="0.9em",
                    ),
                    align_items="center",
                    spacing="2",
                    padding="30px",
                    background_color=rx.cond(AppState.is_dark, "#13132b", "#f8f9fa"),
                    border_radius="12px",
                    width="200px",
                ),
                spacing="6",
                justify="center",
                flex_wrap="wrap",
                width="100%",
            ),

            rx.divider(border_color=rx.cond(AppState.is_dark, "#333", "#ddd"), width="100%"),

            # 🔹 How it works
            rx.vstack(
                rx.heading(
                    "How It Works",
                    size="6",
                    color=rx.cond(AppState.is_dark, "white", "#1a1a2e"),
                    text_align="center",
                ),
                rx.flex(
                    # Step 1
                    rx.vstack(
                        rx.box(
                            rx.text("1", color="white", font_weight="bold", font_size="1.2em"),
                            background_color="#60a5fa",
                            border_radius="50%",
                            width="40px",
                            height="40px",
                            display="flex",
                            align_items="center",
                            justify_content="center",
                        ),
                        rx.text(
                            "Paste Code",
                            font_weight="bold",
                            color=rx.cond(AppState.is_dark, "white", "#1a1a2e"),
                        ),
                        rx.text(
                            "Copy your code into the editor",
                            color=rx.cond(AppState.is_dark, "#888", "#555"),
                            font_size="0.9em",
                            text_align="center",
                        ),
                        align_items="center",
                        spacing="2",
                        width="180px",
                    ),
                    # Step 2
                    rx.vstack(
                        rx.box(
                            rx.text("2", color="white", font_weight="bold", font_size="1.2em"),
                            background_color="#60a5fa",
                            border_radius="50%",
                            width="40px",
                            height="40px",
                            display="flex",
                            align_items="center",
                            justify_content="center",
                        ),
                        rx.text(
                            "AI Analyzes",
                            font_weight="bold",
                            color=rx.cond(AppState.is_dark, "white", "#1a1a2e"),
                        ),
                        rx.text(
                            "Our AI reviews your code instantly",
                            color=rx.cond(AppState.is_dark, "#888", "#555"),
                            font_size="0.9em",
                            text_align="center",
                        ),
                        align_items="center",
                        spacing="2",
                        width="180px",
                    ),
                    # Step 3
                    rx.vstack(
                        rx.box(
                            rx.text("3", color="white", font_weight="bold", font_size="1.2em"),
                            background_color="#60a5fa",
                            border_radius="50%",
                            width="40px",
                            height="40px",
                            display="flex",
                            align_items="center",
                            justify_content="center",
                        ),
                        rx.text(
                            "Get Suggestions",
                            font_weight="bold",
                            color=rx.cond(AppState.is_dark, "white", "#1a1a2e"),
                        ),
                        rx.text(
                            "Receive detailed improvements",
                            color=rx.cond(AppState.is_dark, "#888", "#555"),
                            font_size="0.9em",
                            text_align="center",
                        ),
                        align_items="center",
                        spacing="2",
                        width="180px",
                    ),
                    spacing="8",
                    justify="center",
                    flex_wrap="wrap",
                    width="100%",
                ),
                align_items="center",
                spacing="5",
                width="100%",
            ),

            rx.divider(border_color=rx.cond(AppState.is_dark, "#333", "#ddd"), width="100%"),

            # 🔹 Technologies
            rx.vstack(
                rx.heading(
                    "Technologies Used",
                    size="6",
                    color=rx.cond(AppState.is_dark, "white", "#1a1a2e"),
                ),
                rx.hstack(
                    rx.box(
                        rx.text("Python", color="white", font_weight="bold"),
                        background_color="#3776ab",
                        padding="8px 20px",
                        border_radius="20px",
                    ),
                    rx.box(
                        rx.text("Reflex", color="white", font_weight="bold"),
                        background_color="#60a5fa",
                        padding="8px 20px",
                        border_radius="20px",
                    ),
                    rx.box(
                        rx.text("AI / LLM", color="white", font_weight="bold"),
                        background_color="#7c3aed",
                        padding="8px 20px",
                        border_radius="20px",
                    ),
                    spacing="3",
                    flex_wrap="wrap",
                ),
                align_items="start",
                spacing="4",
                width="100%",
            ),

            rx.divider(border_color=rx.cond(AppState.is_dark, "#333", "#ddd"), width="100%"),

            # 🔹 Contact
            rx.vstack(
                rx.heading(
                    "Contact",
                    size="6",
                    color=rx.cond(AppState.is_dark, "white", "#1a1a2e"),
                ),
                rx.text(
                    "Have questions or feedback? Reach out!",
                    color=rx.cond(AppState.is_dark, "#888", "#555"),
                ),
                rx.hstack(
                    rx.link(
                        rx.button(
                            "Send Email",
                            background_color="#60a5fa",
                            color="white",
                            padding="10px 24px",
                            border_radius="8px",
                            _hover={"background_color": "#3b82f6"},
                        ),
                        href="mailto:vimalaavula18@gmail.com",
                    ),
                    rx.link(
                        rx.button(
                            "GitHub",
                            background_color="transparent",
                            color=rx.cond(AppState.is_dark, "white", "#1a1a2e"),
                            border=rx.cond(
                                AppState.is_dark,
                                "2px solid white",
                                "2px solid #1a1a2e",
                            ),
                            padding="10px 24px",
                            border_radius="8px",
                            _hover={"opacity": "0.7"},
                        ),
                        href="https://github.com/vimala-cse",
                        is_external=True,
                    ),
                    spacing="4",
                ),
                align_items="start",
                spacing="4",
                width="100%",
            ),

            width="100%",
            max_width="800px",
            spacing="8",
            padding="60px 20px",
            align_items="center",
        ),
        display="flex",
        justify_content="center",
        width="100%",
        background_color=rx.cond(
            AppState.is_dark, "#0f0f1a", "#ffffff"
        ),
        min_height="100vh",
    )