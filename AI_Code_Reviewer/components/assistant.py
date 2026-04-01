import reflex as rx
from AI_Code_Reviewer.state import AppState

PROJECT_CONTEXT = """
You are the friendly AI Assistant built into "AI Code Reviewer" — a web app by
Batch 13, Group 1, Infosys Springboard Virtual Internship 6.0 (2026).

PERSONALITY: Friendly, warm, short answers (2-5 lines), simple English, add emoji sometimes.

APP DETAILS:
- Name: AI Code Reviewer
- URL: https://ai-code-reviewer-gold-moon.reflex.run/
- Purpose: Reviews Python code → Score/100, Issues, AI Suggestions, Corrected Code
- Stack: Python, Reflex, Groq API (LLaMA 3.1 8B), LangChain, AST, SQLModel

PAGES:
- Home: Hero with Start Reviewing + Try Demo buttons
- Analyze: Paste code → Analyze Code → results
- History: All past analyses, click to expand
- About: Mission, How it works, Tech stack, Contact

HOW IT WORKS:
code_parser.py → error_detector.py → code_analyzer.py → ai_suggester.py (Groq API)
Returns: Score/100, Issues Found, 5 AI Suggestion sections, Corrected Code

SCORING:
- 100/100 = Perfect code
- 90/100  = Minor issues (unused var/import)
- 0/100   = Syntax error

TRY DEMO code:
    import os
    def calculate_sum(a, b):
        result = a + b
        x = 10
        return result
    print(calculate_sum(5, 3))
Result: Unused variable x, Unused import os → Score 90/100

AI SUGGESTIONS (5 sections): Errors, Improvements, Time Complexity, Space Complexity, PEP8 Issues

TECH: Python, Reflex (no JS needed!), AST module, Groq API, LLaMA 3.1 8B, LangChain, SQLModel

TEAM: Rohith Reddy GK, Jeevia Harshini M, Sanjenbam Motilal Singh, Rondla Naga Venkata Naveen,
Renuka Selvi K, Dreamy Havilah Duddu, Saanvi Sahoo, Anuj Avula, Vimala, Ramya S

If user asks about last analyzed code, it will be provided below.
"""


class AssistantState(rx.State):
    is_open: bool = False
    question: str = ""
    is_thinking: bool = False
    chat_history: list[dict] = []
    last_code: str = ""
    last_result: str = ""

    def toggle(self):
        self.is_open = not self.is_open

    def set_question(self, value: str):
        self.question = value

    def clear_chat(self):
        self.chat_history = []

    def set_quick(self, q: str):
        self.question = q

    def sync_last_analysis(self, code: str, result: str):
        self.last_code = code
        self.last_result = result

    async def ask(self):
        if not self.question.strip():
            return
        user_msg = self.question.strip()
        self.chat_history = self.chat_history + [{"role": "user", "text": user_msg}]
        self.question = ""
        self.is_thinking = True
        yield
        try:
            from langchain_groq import ChatGroq
            from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

            llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.4, max_tokens=400)

            system_prompt = PROJECT_CONTEXT
            if self.last_code and self.last_code.strip():
                system_prompt += f"\n\nLAST ANALYZED CODE:\n```python\n{self.last_code}\n```"
            if self.last_result and self.last_result.strip():
                system_prompt += f"\n\nANALYSIS RESULT:\n{self.last_result}"

            messages = [SystemMessage(content=system_prompt)]
            for msg in self.chat_history[:-1]:
                if msg["role"] == "user":
                    messages.append(HumanMessage(content=msg["text"]))
                else:
                    messages.append(AIMessage(content=msg["text"]))
            messages.append(HumanMessage(content=user_msg))

            response = llm.invoke(messages)
            reply = response.content
        except Exception:
            reply = "Oops! Something went wrong. Please try again 🙏"

        self.chat_history = self.chat_history + [{"role": "assistant", "text": reply}]
        self.is_thinking = False


def render_message(msg: dict) -> rx.Component:
    is_user = msg["role"] == "user"
    return rx.box(
        rx.text(
            msg["text"],
            font_size="0.83em",
            line_height="1.55",
            white_space="pre-wrap",
            color=rx.cond(
                is_user,
                "white",
                rx.cond(AppState.is_dark, "#E3F2FD", "#1a1a2e"),
            ),
        ),
        background=rx.cond(
            is_user,
            "linear-gradient(135deg, #1565C0, #2E75B6)",
            rx.cond(AppState.is_dark, "#1a2d40", "#EBF5FB"),
        ),
        border_radius=rx.cond(
            is_user,
            "18px 18px 4px 18px",
            "18px 18px 18px 4px",
        ),
        padding="10px 14px",
        max_width="86%",
        align_self=rx.cond(is_user, "flex-end", "flex-start"),
        box_shadow=rx.cond(
            is_user,
            "0 2px 8px rgba(21,101,192,0.3)",
            "0 1px 4px rgba(0,0,0,0.06)",
        ),
    )


def thinking_dots() -> rx.Component:
    return rx.hstack(
        rx.box(
            width="8px",
            height="8px",
            border_radius="50%",
            background_color="#2E75B6",
            style={"animation": "dot-bounce 1.2s ease-in-out 0s infinite"},
        ),
        rx.box(
            width="8px",
            height="8px",
            border_radius="50%",
            background_color="#2E75B6",
            style={"animation": "dot-bounce 1.2s ease-in-out 0.2s infinite"},
        ),
        rx.box(
            width="8px",
            height="8px",
            border_radius="50%",
            background_color="#2E75B6",
            style={"animation": "dot-bounce 1.2s ease-in-out 0.4s infinite"},
        ),
        background=rx.cond(AppState.is_dark, "#1a2d40", "#EBF5FB"),
        border_radius="18px 18px 18px 4px",
        padding="12px 16px",
        spacing="1",
        align="center",
        align_self="flex-start",
    )


def welcome_chips() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text(
                "Explain my last code",
                font_size="0.72em",
                color=rx.cond(AppState.is_dark, "#90CAF9", "#1565C0"),
            ),
            background=rx.cond(AppState.is_dark, "#0d1b2a", "#DBEAFE"),
            border="1px solid",
            border_color=rx.cond(AppState.is_dark, "#1e3a5f", "#93C5FD"),
            border_radius="14px",
            padding="5px 11px",
            cursor="pointer",
            on_click=AssistantState.set_quick("Explain my last code"),
            _hover={"opacity": "0.75"},
        ),
        rx.box(
            rx.text(
                "What does score mean?",
                font_size="0.72em",
                color=rx.cond(AppState.is_dark, "#90CAF9", "#1565C0"),
            ),
            background=rx.cond(AppState.is_dark, "#0d1b2a", "#DBEAFE"),
            border="1px solid",
            border_color=rx.cond(AppState.is_dark, "#1e3a5f", "#93C5FD"),
            border_radius="14px",
            padding="5px 11px",
            cursor="pointer",
            on_click=AssistantState.set_quick("What does score mean?"),
            _hover={"opacity": "0.75"},
        ),
        rx.box(
            rx.text(
                "What is PEP8?",
                font_size="0.72em",
                color=rx.cond(AppState.is_dark, "#90CAF9", "#1565C0"),
            ),
            background=rx.cond(AppState.is_dark, "#0d1b2a", "#DBEAFE"),
            border="1px solid",
            border_color=rx.cond(AppState.is_dark, "#1e3a5f", "#93C5FD"),
            border_radius="14px",
            padding="5px 11px",
            cursor="pointer",
            on_click=AssistantState.set_quick("What is PEP8?"),
            _hover={"opacity": "0.75"},
        ),
        flex_wrap="wrap",
        spacing="2",
    )


def welcome_view() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.text(
                "👋  Hi! How can I help you?",
                font_size="0.88em",
                font_weight="bold",
                color=rx.cond(AppState.is_dark, "#E3F2FD", "#1F3864"),
            ),
            rx.text(
                "Ask me about your code review, this app, or Python!",
                font_size="0.78em",
                color=rx.cond(AppState.is_dark, "#90A4AE", "#546E7A"),
                margin_top="4px",
                line_height="1.5",
            ),
            background=rx.cond(AppState.is_dark, "#1a2d40", "#EBF5FB"),
            border_radius="18px 18px 18px 4px",
            padding="12px 16px",
            align_self="flex-start",
        ),
        welcome_chips(),
        align_items="start",
        spacing="3",
        width="100%",
    )


def assistant_panel() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.box(
                    rx.text("🤖", font_size="1.1em"),
                    background="linear-gradient(135deg, #1565C0, #00B4D8)",
                    border_radius="50%",
                    width="34px",
                    height="34px",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    flex_shrink="0",
                ),
                rx.vstack(
                    rx.text(
                        "Assistant",
                        font_weight="bold",
                        font_size="0.92em",
                        color="white",
                    ),
                    rx.hstack(
                        rx.box(
                            width="7px",
                            height="7px",
                            border_radius="50%",
                            background_color="#00E676",
                            style={"animation": "pulse-dot 2s ease-in-out infinite"},
                        ),
                        rx.text("Online", font_size="0.72em", color="#80CBC4"),
                        spacing="1",
                        align="center",
                    ),
                    spacing="0",
                    align_items="start",
                ),
                spacing="2",
                align="center",
            ),
            rx.hstack(
                rx.button(
                    rx.icon("trash-2", size=13, color="#90CAF9"),
                    on_click=AssistantState.clear_chat,
                    background_color="transparent",
                    border="none",
                    cursor="pointer",
                    padding="5px",
                    border_radius="8px",
                    title="Clear chat",
                    _hover={"background_color": "rgba(255,255,255,0.12)"},
                ),
                rx.button(
                    rx.icon("x", size=16, color="white"),
                    on_click=AssistantState.toggle,
                    background_color="transparent",
                    border="none",
                    cursor="pointer",
                    padding="5px",
                    border_radius="8px",
                    _hover={"background_color": "rgba(255,255,255,0.12)"},
                ),
                spacing="1",
            ),
            justify="between",
            align="center",
            width="100%",
            padding="13px 16px",
            background="linear-gradient(135deg, #0A1628 0%, #1F3864 100%)",
            border_radius="20px 20px 0 0",
        ),
        rx.box(
            rx.vstack(
                rx.cond(
                    AssistantState.chat_history.length() == 0,
                    welcome_view(),
                    rx.foreach(AssistantState.chat_history, render_message),
                ),
                rx.cond(
                    AssistantState.is_thinking,
                    thinking_dots(),
                    rx.box(),
                ),
                spacing="3",
                width="100%",
                align_items="stretch",
                padding="14px",
            ),
            height="300px",
            overflow_y="auto",
            background=rx.cond(AppState.is_dark, "#0d1520", "#F8FBFF"),
            css={
                "&::-webkit-scrollbar": {"width": "3px"},
                "&::-webkit-scrollbar-thumb": {
                    "background": "#2E75B6",
                    "border_radius": "4px",
                },
            },
        ),
        rx.hstack(
            rx.input(
                value=AssistantState.question,
                on_change=AssistantState.set_question,
                placeholder="Ask anything...",
                flex="1",
                border="1.5px solid",
                border_color=rx.cond(AppState.is_dark, "#1e3a5f", "#BBDEFB"),
                border_radius="24px",
                padding="10px 18px",
                font_size="0.84em",
                background=rx.cond(AppState.is_dark, "#0d1520", "white"),
                color=rx.cond(AppState.is_dark, "#E3F2FD", "#1a1a2e"),
                _focus={
                    "outline": "none",
                    "border_color": "#2E75B6",
                    "box_shadow": "0 0 0 3px rgba(46,117,182,0.18)",
                },
                _placeholder={
                    "color": rx.cond(AppState.is_dark, "#455A64", "#90A4AE"),
                },
                on_key_down=lambda key: rx.cond(
                    key == "Enter",
                    AssistantState.ask(),
                    rx.noop(),
                ),
            ),
            rx.button(
                rx.icon("send", size=15, color="white"),
                on_click=AssistantState.ask,
                background="linear-gradient(135deg, #1565C0, #2E75B6)",
                border_radius="50%",
                width="40px",
                height="40px",
                min_width="40px",
                padding="0",
                cursor="pointer",
                border="none",
                box_shadow="0 3px 10px rgba(21,101,192,0.4)",
                _hover={
                    "background": "linear-gradient(135deg, #0D47A1, #1565C0)",
                    "transform": "scale(1.08)",
                },
                disabled=AssistantState.is_thinking,
            ),
            spacing="2",
            align="center",
            padding="12px 14px",
            background=rx.cond(AppState.is_dark, "#0d1520", "white"),
            border_top="1px solid",
            border_color=rx.cond(AppState.is_dark, "#1a2d40", "#E3F2FD"),
            border_radius="0 0 20px 20px",
        ),
        position="fixed",
        bottom="96px",
        right="24px",
        width="340px",
        border_radius="20px",
        overflow="hidden",
        box_shadow=rx.cond(
            AppState.is_dark,
            "0 16px 56px rgba(0,0,0,0.6), 0 0 0 1px rgba(46,117,182,0.2)",
            "0 16px 56px rgba(0,0,0,0.12), 0 0 0 1px rgba(46,117,182,0.1)",
        ),
        z_index="1000",
        display=rx.cond(AssistantState.is_open, "flex", "none"),
        flex_direction="column",
        style={"animation": "slide-up 0.22s ease-out"},
    )


def floating_assistant_button() -> rx.Component:
    return rx.box(
        rx.html(
            """<style>
@keyframes pulse-glow {
  0%   { box-shadow: 0 0 0 0px  rgba(0,180,216,0.65), 0 6px 24px rgba(21,101,192,0.5); }
  60%  { box-shadow: 0 0 0 14px rgba(0,180,216,0),    0 6px 24px rgba(21,101,192,0.5); }
  100% { box-shadow: 0 0 0 0px  rgba(0,180,216,0),    0 6px 24px rgba(21,101,192,0.5); }
}
@keyframes slide-up {
  from { opacity: 0; transform: translateY(14px) scale(0.97); }
  to   { opacity: 1; transform: translateY(0px)  scale(1);    }
}
@keyframes dot-bounce {
  0%, 80%, 100% { transform: scale(0.7); opacity: 0.5; }
  40%           { transform: scale(1.1); opacity: 1.0; }
}
@keyframes pulse-dot {
  0%,  100% { opacity: 1.0; transform: scale(1.0); }
  50%        { opacity: 0.4; transform: scale(0.7); }
}
</style>"""
        ),
        assistant_panel(),
        rx.button(
            rx.cond(
                AssistantState.is_open,
                rx.icon("x", size=24, color="white"),
                rx.text("🤖", font_size="1.7em"),
            ),
            on_click=AssistantState.toggle,
            background="linear-gradient(135deg, #0A1628 0%, #1F3864 50%, #2E75B6 100%)",
            border_radius="50%",
            width="60px",
            height="60px",
            min_width="60px",
            padding="0",
            cursor="pointer",
            border="none",
            position="fixed",
            bottom="24px",
            right="24px",
            z_index="1001",
            display="flex",
            align_items="center",
            justify_content="center",
            transition="all 0.22s cubic-bezier(0.4,0,0.2,1)",
            _hover={
                "background": "linear-gradient(135deg, #1F3864, #2E75B6, #00B4D8)",
                "transform": "scale(1.1)",
            },
            style={"animation": "pulse-glow 2.8s ease-in-out infinite"},
        ),
    )