import ast


def parse_code(code_string):
    """
    Parses and preprocesses Python code using AST.
    """

    try:
        tree = ast.parse(code_string)
        formatted_code = ast.unparse(tree)

        return {
            "success": True,
            "message": "Code parsed successfully.",
            "formatted_code": formatted_code,
            "tree": tree
        }

    except SyntaxError as e:
        return {
            "success": False,
            "error_type": "SyntaxError",
            "message": str(e),
            "line_number": e.lineno
        }


if __name__ == "__main__":

    sample_code = """
def add(a,b):
    return a+b
"""

    result = parse_code(sample_code)

    if result["success"]:
        print("Status:", result["message"])
        print("\nFormatted Code:\n")
        print(result["formatted_code"])

        #print("\nAST Structure:\n")
        #print(ast.dump(result["tree"], indent=4))

    else:
        print("Error Type:", result["error_type"])
        print("Line Number:", result["line_number"])
        print("Message:", result["message"])