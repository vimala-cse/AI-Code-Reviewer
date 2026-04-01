import reflex as rx
from AI_Code_Reviewer.state import AppState


class FAQState(rx.State):
    open_question: str = ""

    def toggle(self, question: str):
        if self.open_question == question:
            self.open_question = ""
        else:
            self.open_question = question


FAQ_ITEMS = [
    {
        "q": "How do I use AI Code Reviewer?",
        "a": "Go to the Analyze page, paste your Python code into the editor, and click 'Analyze Code'. In a few seconds, you'll see a Score out of 100, a list of Issues Found, AI Suggestions with improvements, and a side-by-side view of your original code vs the corrected version.",
    },
    {
        "q": "What type of code can I paste?",
        "a": "Currently the app supports Python code only. You can paste any Python script — functions, classes, loops, or simple expressions. Multi-language support (Java, JavaScript, C++) is planned for a future update.",
    },
    {
        "q": "What is the 'Try Demo' button?",
        "a": "The 'Try Demo' button on the homepage loads a sample Python code snippet that has two common issues: an unused variable 'x' and an unused import 'os'. Click it and go to Analyze to see exactly how the review works before trying your own code.",
    },
    {
        "q": "Why did I get Score 0/100?",
        "a": "A score of 0/100 means your code has a syntax error — Python cannot even read or run it. Common causes are: missing colon after if/def/for, mismatched brackets, or wrong indentation. The error message will show you the exact line number where the problem is.",
    },
    {
        "q": "Is my code stored anywhere?",
        "a": "Your code and analysis results are saved in a local database on the server — this is what powers your History page so you can revisit past analyses. Your code is not shared with anyone or sold to third parties. The Groq API processes your code to generate AI suggestions but does not store it permanently.",
    },
    {
        "q": "How long is my history saved?",
        "a": "Your analysis history is saved in the app's database as long as the server is running. You can view all past analyses on the History page, expand any entry to see full details, and delete individual records using the trash icon. History is tied to the server session.",
    },
    {
        "q": "Why is analysis taking long?",
        "a": "Analysis involves calling an external AI API (Groq) over the internet, which typically takes 2–5 seconds depending on your network and code length. The AST parsing and error detection steps are instant. If it takes longer than 15 seconds, try refreshing the page and analyzing again.",
    },
    {
        "q": "Which programming languages are supported?",
        "a": "Currently, AI Code Reviewer fully supports Python. The AST parsing, error detection, PEP8 analysis, and scoring are all Python-specific. Support for Java, JavaScript, C++, and Go is planned as a future improvement.",
    },
    {
        "q": "What if I get an error?",
        "a": "If you see an error message in the results, check that your code is valid Python first. If the app itself shows an unexpected error, try refreshing the page and pasting your code again. If the problem persists, try a smaller code snippet to identify which part causes the issue.",
    },
]


def faq_item(item: dict) -> rx.Component:
    is_open = FAQState.open_question == item["q"]
    return rx.box(
        # Question row
        rx.hstack(
            rx.text(
                item["q"],
                font_size="0.97em",
                font_weight="600",
                color=rx.cond(
                    is_open,
                    "#60a5fa",
                    rx.cond(AppState.is_dark, "#E3F2FD", "#1F3864"),
                ),
                flex="1",
                line_height="1.5",
            ),
            rx.icon(
                rx.cond(is_open, "chevron-up", "chevron-down"),
                size=18,
                color=rx.cond(
                    is_open,
                    "#60a5fa",
                    rx.cond(AppState.is_dark, "#546E7A", "#90A4AE"),
                ),
                flex_shrink="0",
            ),
            justify="between",
            align="center",
            width="100%",
            padding="18px 20px",
            cursor="pointer",
            on_click=FAQState.toggle(item["q"]),
            _hover={"opacity": "0.85"},
        ),
        # Answer
        rx.cond(
            is_open,
            rx.box(
                rx.text(
                    item["a"],
                    font_size="0.92em",
                    line_height="1.8",
                    color=rx.cond(AppState.is_dark, "#90A4AE", "#546E7A"),
                ),
                padding="0 20px 18px 20px",
                border_top="1px solid",
                border_color=rx.cond(AppState.is_dark, "#2d2d44", "#E3F2FD"),
                padding_top="14px",
            ),
        ),
        background=rx.cond(
            is_open,
            rx.cond(AppState.is_dark, "#13132b", "#F0F6FF"),
            rx.cond(AppState.is_dark, "#1e1e3a", "#FFFFFF"),
        ),
        border="1px solid",
        border_color=rx.cond(
            is_open,
            "#2E75B6",
            rx.cond(AppState.is_dark, "#2d2d44", "#E8F0FE"),
        ),
        border_radius="12px",
        overflow="hidden",
        width="100%",
        transition="all 0.2s ease",
        box_shadow=rx.cond(
            is_open,
            "0 4px 16px rgba(21,101,192,0.12)",
            "0 1px 3px rgba(0,0,0,0.04)",
        ),
        _hover={
            "border_color": "#60a5fa",
            "box_shadow": "0 2px 8px rgba(96,165,250,0.1)",
        },
    )


def faq_page() -> rx.Component:
    return rx.box(
        rx.vstack(
            # Header
            rx.vstack(
                rx.text(
                    "HELP CENTER",
                    font_size="0.75em",
                    font_weight="bold",
                    color="#60a5fa",
                    letter_spacing="3px",
                ),
                rx.heading(
                    "Frequently Asked Questions",
                    size="8",
                    color=rx.cond(AppState.is_dark, "white", "#1F3864"),
                    text_align="center",
                ),
                rx.text(
                    "Everything you need to know about AI Code Reviewer.",
                    color=rx.cond(AppState.is_dark, "#90A4AE", "#546E7A"),
                    font_size="1.05em",
                    text_align="center",
                ),
                align_items="center",
                spacing="3",
                width="100%",
            ),

            # FAQ list
            rx.vstack(
                *[faq_item(item) for item in FAQ_ITEMS],
                spacing="3",
                width="100%",
                align_items="start",
            ),

            # Bottom CTA
            rx.box(
                rx.vstack(
                    rx.text(
                        "Still have questions?",
                        font_size="1.1em",
                        font_weight="bold",
                        color=rx.cond(AppState.is_dark, "white", "#1F3864"),
                    ),
                    rx.text(
                        "Ask our AI Assistant — click the 🤖 button at the bottom right of any page.",
                        font_size="0.92em",
                        color=rx.cond(AppState.is_dark, "#90A4AE", "#546E7A"),
                        text_align="center",
                    ),
                    rx.link(
                        rx.button(
                            "Start Analyzing Code",
                            background="linear-gradient(135deg, #1565C0, #2E75B6)",
                            color="white",
                            border_radius="10px",
                            padding="11px 28px",
                            font_size="0.95em",
                            font_weight="bold",
                            cursor="pointer",
                            border="none",
                            _hover={"opacity": "0.9", "transform": "translateY(-1px)"},
                            transition="all 0.15s ease",
                        ),
                        href="/analyze",
                    ),
                    align_items="center",
                    spacing="4",
                ),
                background=rx.cond(AppState.is_dark, "#1e1e3a", "#F0F6FF"),
                border="1px solid",
                border_color=rx.cond(AppState.is_dark, "#2d2d44", "#BBDEFB"),
                border_radius="16px",
                padding="32px",
                width="100%",
                text_align="center",
            ),

            width="100%",
            max_width="760px",
            spacing="6",
            padding="48px 20px",
            align_items="center",
        ),
        display="flex",
        justify_content="center",
        width="100%",
        background_color=rx.cond(AppState.is_dark, "#0f0f1a", "#F8FBFF"),
        min_height="100vh",
    )