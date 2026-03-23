import ast


def parse_code(code_string, language="Python"):
    """
    This function checks Python code for syntax errors.

    Parameters:
        code_string (str): Python code given as string

    Returns:
        dict: Contains success status and error details (if any)
    """

    try:
        # Try to convert code into AST (check syntax)
        tree = ast.parse(code_string)

        return {
            "success": True,
            "message": "Code parsed successfully.",
            "tree": tree
        }

    except SyntaxError as e:
        return {
            "success": False,
            "error": {
                "type": "SyntaxError",
                "message": str(e),
                "line_number": e.lineno
            }
        }