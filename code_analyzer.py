from code_parser import parse_code
from error_detector import ErrorDetector
from ai_suggester import get_ai_suggestion
import ast


def analyze_code_pipeline(code):

    # Step 1: Syntax check
    syntax_result = parse_code(code)

    if not syntax_result["success"]:
        return {
            "syntax_error": syntax_result["error"]["message"],
            "line_number": syntax_result["error"]["line_number"],
            "score": 0,
            "issues": [],
            "ai_suggestions": ""
        }

    # Step 2: Get parsed tree
    tree = syntax_result["tree"]

    # Step 3: Detect errors
    detector = ErrorDetector()
    detector.visit(tree)
    report = detector.generate_report()

    # Step 4: AI suggestions
    ai_result = get_ai_suggestion(code)

    # Step 5: Final result
    return {
        "syntax_error": None,
        "score": report["score"],
        "issues": report["issues"],
        "ai_suggestions": ai_result.content if hasattr(ai_result, 'content') else str(ai_result)
    }