import reflex as rx

class AnalysisHistory(rx.Model, table=True):
    code: str
    score: int
    issues: str
    ai_suggestions: str
    timestamp: str