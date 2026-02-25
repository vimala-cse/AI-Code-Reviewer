import ast


def parse_code(code_string):
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


# Testing Block

# if __name__ == "__main__":

#     sample_code = """
# def calculate_sum(a, b):
#     result = a + b
#     if result > 10:
#         print("Greater than 10")
#     return result
# """

#     result = parse_code(sample_code)

#     print("\n--- Parser Output ---\n")

#     if result["success"]:
#         print(result["message"])
#     else:
#         print("Error Type:", result["error"]["type"])
#         print("Line Number:", result["error"]["line_number"])
#         print("Message:", result["error"]["message"])