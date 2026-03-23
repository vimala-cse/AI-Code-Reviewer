import ast


class ErrorDetector(ast.NodeVisitor):

    def __init__(self):
        self.defined = set()
        self.used = set()
        self.imported = set()
        self.issues = []
        self.score = 100

    # Import Detection
    def visit_Import(self, node):
        for alias in node.names:
            self.imported.add(alias.name)
            self.defined.add(alias.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        for alias in node.names:
            self.imported.add(alias.name)
            self.defined.add(alias.name)
        self.generic_visit(node)

    # Variable Usage Detection
    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            self.defined.add(node.id)
        elif isinstance(node.ctx, ast.Load):
            self.used.add(node.id)
        self.generic_visit(node)

    # Infinite Loop Detection
    def visit_While(self, node):
        if isinstance(node.test, ast.Constant) and node.test.value is True:

            has_break = any(
                isinstance(child, ast.Break)
                for child in ast.walk(node)
            )

            if not has_break:
                self.issues.append(
                    "Infinite loop detected: 'while True' without break."
                )
                self.score -= 5

        self.generic_visit(node)

    # Function Length Check
    def visit_FunctionDef(self, node):

        if hasattr(node, "end_lineno"):
            length = node.end_lineno - node.lineno + 1
            if length > 40:
                self.issues.append(
                    f"Function '{node.name}' is too long ({length} lines)."
                )
                self.score -= 5

        self.generic_visit(node)

    # Final Report
    def generate_report(self):

        # Built-in functions ignore చేయాలి
        builtins = set(dir(__builtins__)) if isinstance(__builtins__, dict) else set(dir(__builtins__))

        # Unused variables
        unused_vars = self.defined - self.used
        for var in unused_vars:
            if var not in self.imported and var not in builtins:
                self.issues.append(f"Unused variable: '{var}'")
                self.score -= 5

        # Unused imports
        unused_imports = self.imported - self.used
        for imp in unused_imports:
            self.issues.append(f"Unused import: '{imp}'")
            self.score -= 5

        if self.score < 0:
            self.score = 0

        return {
            "issues": self.issues,
            "score": self.score
        }