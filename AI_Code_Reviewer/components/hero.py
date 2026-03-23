import reflex as rx
from AI_Code_Reviewer.state import AppState

def hero():
    return rx.box(

        # 🔹 Background image
        rx.box(
            position="absolute",
            top="0",
            left="0",
            width="100%",
            height="100%",
            background_image="url('/hero-bg.jpeg')",
            background_size="cover",
            background_position="center right",
            background_repeat="no-repeat",
        ),

        # 🔹 Dark overlay
        rx.box(
            position="absolute",
            top="0",
            left="0",
            width="100%",
            height="100%",
            background_color="rgba(0, 0, 0, 0.3)",
        ),

        # 🔹 White card
        rx.box(
            rx.vstack(
                rx.heading(
                    "Review Your",
                    size="8",
                    color="#1a1a2e",
                ),
                rx.heading(
                    "Code with AI",
                    size="8",
                    color="#60a5fa",
                ),
                rx.text(
                    "Detect bugs, improve code quality, and get instant suggestions.",
                    color="#555",
                    font_size="1em",
                ),
                rx.hstack(
                    # Start Reviewing — empty page కి
                    rx.link(
                        rx.button(
                            "Start Reviewing",
                            background_color="#60a5fa",
                            color="white",
                            padding="12px 24px",
                            border_radius="8px",
                            _hover={"background_color": "#3b82f6"},
                        ),
                        href="/analyze",
                    ),
                    # Try Demo — demo code తో
                    rx.link(
                        rx.button(
                            "Try Demo",
                            on_click=AppState.load_demo,
                            background_color="transparent",
                            color="#1a1a2e",
                            border="2px solid #1a1a2e",
                            padding="12px 24px",
                            border_radius="8px",
                            _hover={"opacity": "0.7"},
                        ),
                        href="/analyze",
                    ),
                    spacing="4",
                ),
                align_items="start",
                spacing="4",
                padding="40px",
            ),
            background_color="rgba(255, 255, 255, 0.98)",
            border_radius="16px",
            box_shadow="0 8px 32px rgba(0,0,0,0.3)",
            max_width="600px",
            width="600px",
            position="relative",
            z_index="1",
            style={
                "animation": "fadeIn 0.8s ease-out",
                "@keyframes fadeIn": {
                    "from": {"opacity": "0", "transform": "translateY(20px)"},
                    "to": {"opacity": "1", "transform": "translateY(0)"},
                },
            },
        ),

        position="relative",
        width="100%",
        min_height="90vh",
        display="flex",
        align_items="flex-end",
        justify_content="flex-start",
        padding="40px",
        overflow="hidden",
    )