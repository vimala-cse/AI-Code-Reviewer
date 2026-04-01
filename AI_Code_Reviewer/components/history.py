import reflex as rx
from AI_Code_Reviewer.state import AppState
from AI_Code_Reviewer.models import AnalysisHistory


class HistoryState(rx.State):
    records: list[dict] = []
    selected_id: str = ""
    is_loading: bool = False

    async def load_history(self):
        # Show loading immediately
        self.is_loading = True
        yield  # ← UI updates instantly

        try:
            with rx.session() as session:
                history = session.exec(
                    AnalysisHistory.select()
                ).all()
                self.records = [
                    {
                        "id": str(h.id),
                        "code": (
                            h.code[:50] + "..."
                            if len(h.code) > 50
                            else h.code
                        ),
                        "full_code": h.code,
                        "score": h.score,
                        "issues": h.issues,
                        "ai_suggestions": h.ai_suggestions,
                        "timestamp": h.timestamp,
                    }
                    for h in reversed(history)  # newest first
                ]
        except Exception:
            self.records = []

        self.is_loading = False
        yield  # ← UI updates with records

    def toggle_details(self, record_id: str):
        if self.selected_id == record_id:
            self.selected_id = ""
        else:
            self.selected_id = record_id

    def delete_record(self, record_id: str):
        with rx.session() as session:
            record = session.get(AnalysisHistory, int(record_id))
            if record:
                session.delete(record)
                session.commit()
        self.selected_id = ""
        # Reload after delete
        return HistoryState.load_history


def history_item(record: dict) -> rx.Component:
    is_selected = HistoryState.selected_id == record["id"]
    return rx.vstack(
        # ── Record row ──────────────────────────────────
        rx.box(
            rx.hstack(
                rx.vstack(
                    rx.text(
                        record["code"],
                        font_family="monospace",
                        font_size="0.85em",
                        color=rx.cond(AppState.is_dark, "white", "#1a1a2e"),
                        no_of_lines=1,
                    ),
                    rx.text(
                        record["timestamp"],
                        font_size="0.75em",
                        color="#888",
                    ),
                    align_items="start",
                    spacing="1",
                    flex="1",
                    min_width="0",
                ),
                rx.hstack(
                    rx.text(
                        f"Score: {record['score']}/100",
                        font_weight="bold",
                        color="#60a5fa",
                        font_size="0.9em",
                        white_space="nowrap",
                    ),
                    rx.button(
                        rx.icon("trash-2", size=14),
                        on_click=HistoryState.delete_record(record["id"]),
                        background_color="transparent",
                        color="#f87171",
                        border="1px solid #f87171",
                        border_radius="6px",
                        padding="4px 8px",
                        cursor="pointer",
                        _hover={
                            "background_color": "#f87171",
                            "color": "white",
                        },
                    ),
                    rx.cond(
                        is_selected,
                        rx.icon("chevron-up", size=16, color="#60a5fa"),
                        rx.icon("chevron-down", size=16, color="#60a5fa"),
                    ),
                    spacing="2",
                    align="center",
                    flex_shrink="0",
                ),
                justify="between",
                align="center",
                width="100%",
                gap="8px",
            ),
            on_click=HistoryState.toggle_details(record["id"]),
            width="100%",
            padding="16px",
            background_color=rx.cond(AppState.is_dark, "#2d2d44", "#f8f9fa"),
            border_radius=rx.cond(is_selected, "8px 8px 0 0", "8px"),
            border=rx.cond(
                AppState.is_dark,
                "1px solid #444",
                "1px solid #ddd",
            ),
            cursor="pointer",
            _hover={"opacity": "0.85"},
            transition="all 0.15s ease",
        ),

        # ── Expanded details ─────────────────────────────
        rx.cond(
            is_selected,
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.text(
                            f"Score: {record['score']}/100",
                            font_weight="bold",
                            color="#60a5fa",
                            font_size="1.1em",
                        ),
                        rx.text(
                            record["timestamp"],
                            color="#888",
                            font_size="0.85em",
                        ),
                        rx.link(
                            rx.button(
                                "Edit in Analyzer",
                                on_click=AppState.set_code_from_history(
                                    record["full_code"]
                                ),
                                background_color="#60a5fa",
                                color="white",
                                border_radius="8px",
                                padding="6px 16px",
                                font_size="0.85em",
                                cursor="pointer",
                                _hover={"background_color": "#3b82f6"},
                            ),
                            href="/analyze",
                        ),
                        justify="between",
                        align="center",
                        width="100%",
                        flex_wrap="wrap",
                        spacing="2",
                    ),
                    rx.text(
                        "Code:",
                        font_weight="bold",
                        color=rx.cond(AppState.is_dark, "white", "#1a1a2e"),
                        font_size="0.9em",
                    ),
                    rx.box(
                        rx.text(
                            record["full_code"],
                            font_family="monospace",
                            font_size="0.85em",
                            white_space="pre-wrap",
                            color=rx.cond(
                                AppState.is_dark, "#c3e88d", "#1a1a2e"
                            ),
                        ),
                        background_color=rx.cond(
                            AppState.is_dark, "#1a2d1a", "#f0fff0"
                        ),
                        border_radius="8px",
                        padding="12px",
                        width="100%",
                    ),
                    rx.text(
                        "Issues:",
                        font_weight="bold",
                        color=rx.cond(AppState.is_dark, "white", "#1a1a2e"),
                        font_size="0.9em",
                    ),
                    rx.text(
                        record["issues"],
                        color=rx.cond(AppState.is_dark, "#aaa", "#555"),
                        font_size="0.85em",
                        white_space="pre-wrap",
                    ),
                    rx.text(
                        "AI Suggestions:",
                        font_weight="bold",
                        color=rx.cond(AppState.is_dark, "white", "#1a1a2e"),
                        font_size="0.9em",
                    ),
                    rx.text(
                        record["ai_suggestions"],
                        color=rx.cond(AppState.is_dark, "#aaa", "#555"),
                        font_size="0.85em",
                        white_space="pre-wrap",
                    ),
                    align_items="start",
                    spacing="3",
                    width="100%",
                ),
                width="100%",
                padding="16px",
                background_color=rx.cond(
                    AppState.is_dark, "#1e1e3a", "#ffffff"
                ),
                border_radius="0 0 8px 8px",
                border=rx.cond(
                    AppState.is_dark,
                    "1px solid #444",
                    "1px solid #ddd",
                ),
                border_top="none",
            ),
        ),
        width="100%",
        spacing="0",
    )


def history_page() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Analysis History",
                size="8",
                color=rx.cond(AppState.is_dark, "white", "#1a1a2e"),
            ),
            rx.text(
                "All your previous code analyses. Click to expand.",
                color=rx.cond(AppState.is_dark, "#aaa", "#555"),
            ),

            # Loading state
            rx.cond(
                HistoryState.is_loading,
                rx.vstack(
                    rx.spinner(size="3", color="#60a5fa"),
                    rx.text(
                        "Loading history...",
                        color="#60a5fa",
                        font_size="0.95em",
                    ),
                    align="center",
                    spacing="3",
                    padding="40px",
                    width="100%",
                ),
                # Records or empty state
                rx.cond(
                    HistoryState.records.length() == 0,
                    rx.box(
                        rx.text(
                            "No history yet — analyze some code first!",
                            color=rx.cond(AppState.is_dark, "#888", "#555"),
                            font_size="1em",
                        ),
                        padding="20px",
                    ),
                    rx.vstack(
                        rx.foreach(
                            HistoryState.records,
                            history_item,
                        ),
                        width="100%",
                        spacing="3",
                    ),
                ),
            ),

            width="100%",
            max_width="800px",
            spacing="5",
            padding="40px 20px",
            align_items="start",
        ),
        on_mount=HistoryState.load_history,
        display="flex",
        justify_content="center",
        width="100%",
        background_color=rx.cond(
            AppState.is_dark, "#0f0f1a", "#ffffff"
        ),
        min_height="100vh",
    )