import reflex as rx
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))

from AI_Code_Reviewer.code_analyzer import analyze_code_pipeline

class AppState(rx.State):
    is_dark: bool = True
    code_input: str = ""
    result: str = ""
    corrected_code: str = ""
    is_loading: bool = False

    def set_code(self, value: str):
        self.code_input = value

    def toggle_theme(self):
        self.is_dark = not self.is_dark

    def load_demo(self):
        self.code_input = """import os

def calculate_sum(a, b):
    result = a + b
    x = 10
    return result

print(calculate_sum(5, 3))"""

    @rx.event(background=True)
    async def analyze_code(self):
        if not self.code_input.strip():
            async with self:
                self.result = "Please paste some code first!"
                self.corrected_code = ""
            return

        async with self:
            self.is_loading = True
            self.result = "Analyzing..."
            self.corrected_code = ""

        try:
            output = analyze_code_pipeline(self.code_input)

            if output.get("syntax_error"):
                async with self:
                    self.result = f"❌ Syntax Error: {output['syntax_error']}\nLine: {output['line_number']}"
                    self.corrected_code = ""
            else:
                issues_text = ""
                if output["issues"]:
                    issues_text = "\n⚠️ Issues Found:\n"
                    for issue in output["issues"]:
                        issues_text += f"  • {issue}\n"
                else:
                    issues_text = "\n✅ No issues found!\n"

                ai_text = output["ai_suggestions"]

                if "CORRECTED_CODE:" in ai_text:
                    parts = ai_text.split("CORRECTED_CODE:")
                    analysis = parts[0].replace("ANALYSIS:", "").strip()
                    corrected = parts[1].strip()
                elif "CORRECTED CODE:" in ai_text:
                    parts = ai_text.split("CORRECTED CODE:")
                    analysis = parts[0].replace("ANALYSIS:", "").strip()
                    corrected = parts[1].strip()
                else:
                    analysis = ai_text.replace("ANALYSIS:", "").strip()
                    corrected = ""

                async with self:
                    self.result = f"📊 Score: {output['score']}/100\n{issues_text}\n💡 AI Suggestions:\n{analysis}"
                    self.corrected_code = corrected

        except Exception as e:
            async with self:
                self.result = f"Error: {str(e)}"
                self.corrected_code = ""

        async with self:
            self.is_loading = False