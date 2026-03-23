import reflex as rx
from AI_Code_Reviewer.state import AppState

def footer():
    return rx.box(

        # 🔹 Top - 3 columns
        rx.flex(

            # Column 1 - Logo + tagline
            rx.vstack(
                rx.hstack(
                    rx.image(
                        src="Chat-bot-rafiki.png",
                        width="35px",
                        height="35px",
                    ),
                    rx.text(
                        "AI Code Reviewer",
                        font_weight="bold",
                        color="white",
                        font_size="1.1em",
                    ),
                    align="center",
                    spacing="2",
                ),
                rx.text(
                    "Making code review smarter,",
                    color="#888",
                    font_size="0.85em",
                ),
                rx.text(
                    "faster, and more efficient.",
                    color="#888",
                    font_size="0.85em",
                ),
                align_items="start",
                spacing="2",
            ),

            # Column 2 - Product
            rx.vstack(
                rx.text(
                    "Product",
                    color="white",
                    font_weight="bold",
                    font_size="1em",
                    margin_bottom="8px",
                ),
                rx.link("Analyze", href="/analyze", color="#888", _hover={"color": "#60a5fa"}),
                rx.link("About", href="/about", color="#888", _hover={"color": "#60a5fa"}),
                rx.link("History", href="/history", color="#888", _hover={"color": "#60a5fa"}),
                align_items="start",
                spacing="2",
            ),

            # Column 3 - Connect
            rx.vstack(
                rx.text(
                    "Connect",
                    color="white",
                    font_weight="bold",
                    font_size="1em",
                    margin_bottom="8px",
                ),
                rx.link(
                    "GitHub",
                    href="https://github.com/vimala-cse",
                    color="#888",
                    is_external=True,
                    _hover={"color": "#60a5fa"},
                ),
                rx.link(
                    "LinkedIn",
                    href="https://www.linkedin.com/in/vimala-avula-bb5427329",
                    color="#888",
                    is_external=True,
                    _hover={"color": "#60a5fa"},
                ),
                rx.link(
                    "YouTube",
                    href="https://youtube.com/@cseforyou_18",
                    color="#888",
                    is_external=True,
                    _hover={"color": "#60a5fa"},
                ),
                rx.link(
                    "Email",
                    href="mailto:vimalaavula18@gmail.com",
                    color="#888",
                    _hover={"color": "#60a5fa"},
                ),
                align_items="start",
                spacing="2",
            ),

            justify="start",
            gap="150px",
            width="100%",
            padding="50px 60px 30px 60px",
        ),

        # 🔹 Divider
        rx.divider(border_color="#333"),

        # 🔹 Middle - Follow us + icons
        rx.flex(
            rx.text(
                "Follow us:",
                color="white",
                font_size="0.9em",
                font_weight="bold",
            ),
            rx.link(
                rx.image(
                    src="https://cdn.simpleicons.org/github/ffffff",
                    width="22px",
                    height="22px",
                ),
                href="https://github.com/vimala-cse",
                is_external=True,
                _hover={"opacity": "0.7"},
            ),
            rx.link(
                rx.icon("linkedin", color="white", size=22),
                href="https://www.linkedin.com/in/vimala-avula-bb5427329",
                is_external=True,
                _hover={"opacity": "0.7"},
            ),
            rx.link(
                rx.image(
                    src="https://cdn.simpleicons.org/youtube/FF0000",
                    width="22px",
                    height="22px",
                ),
                href="https://youtube.com/@cseforyou_18",
                is_external=True,
                _hover={"opacity": "0.7"},
            ),
            spacing="4",
            align="center",
            padding="20px 60px",
        ),

        # 🔹 Divider
        rx.divider(border_color="#333"),

        # 🔹 Bottom - Copyright + Terms + Privacy
        rx.flex(
            rx.text(
                "© 2026 AI Code Reviewer. All rights reserved.",
                color="#666",
                font_size="0.85em",
            ),
            rx.hstack(
                rx.link(
                    "Terms",
                    href="#",
                    color="#666",
                    font_size="0.85em",
                    _hover={"color": "#60a5fa"},
                ),
                rx.link(
                    "Privacy",
                    href="#",
                    color="#666",
                    font_size="0.85em",
                    _hover={"color": "#60a5fa"},
                ),
                spacing="4",
            ),
            justify="between",
            align="center",
            width="100%",
            padding="16px 60px",
        ),

        background_color="#080810",
        width="100%",
        border_top="1px solid #222",
    )