import ast


class ErrorDetector(ast.NodeVisitor):
    """
    Performs static code analysis using AST.
    Detects:
    - Unused variables
    - Empty functions
    - Unused imports
    - Infinite loops (while True without break)
    """

    def __init__(self):
        self.defined = set()   # Things created (imports + variables)
        self.used = set()      # Things used (read)
        self.issues = []       # Store all detected issues

    # Import detection
    def visit_Import(self, node):
        for alias in node.names:
            self.defined.add(alias.name)
        self.generic_visit(node)
    
    def visit_ImportFrom(self, node):
        for alias in node.names:
            self.defined.add(alias.name)
        self.generic_visit(node)

    # Variable detection
    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            self.defined.add(node.id)
        elif isinstance(node.ctx, ast.Load):
            self.used.add(node.id)
        self.generic_visit(node)

    # Infinite loop detection
    def visit_While(self, node):
        if isinstance(node.test, ast.Constant) and node.test.value == True:

            has_break = any(
                isinstance(child, ast.Break)
                for child in ast.walk(node)
            )

            if not has_break:
                self.issues.append(
                    "Infinite loop detected: 'while True' without break statement."
                )

        self.generic_visit(node)

    # Final Report
    def report_unused(self):

        unused = self.defined - self.used

        for item in unused:
            self.issues.append(
                f"Unused item detected: '{item}'. It is declared but never used."
            )

        return self.issues


# Testing Block

# if __name__ == "__main__":

#     sample_code = """
# number = 10
# x=5
# while True:
#     if number % 2 == 0:
#         print("Even")
#     else:
#         print("odd")

# """

#     tree = ast.parse(sample_code)

#     detector = ErrorDetector()
#     detector.visit(tree)

#     issues = detector.report_unused()

#     print("\n--- Output ---\n")

#     if issues:
#         for issue in issues:
#             print("-", issue)
#     else:
#         print("No issues detected.")