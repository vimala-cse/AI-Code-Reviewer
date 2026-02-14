import ast

def parse_code(code_string):
    try:
        tree = ast.parse(code_string)
        return {
            "success": True,
            "message": "Code parsed successfully"
        }

    except SyntaxError as e:
        return {
            "success": False,
            "error_type": "Syntax Error",
            "message": e.msg,
            "line_number": e.lineno
        }


# ---- Test 1 (Correct Code) ----
student_code1 = """
def add(a,b):
    return a+b
"""

result1 = parse_code(student_code1)
print("Test 1:", result1)


# ---- Test 2 (Syntax Error Code) ----
student_code2 = """
def add(a,b)
    return a+b
"""

result2 = parse_code(student_code2)
print("Test 2:", result2)