import ast

class ComplexityVisitor(ast.NodeVisitor):
    def __init__(self):
        self.complexity = 0

    def increment(self):
        self.complexity += 1

    def visit_If(self, node):
        self.increment()
        self.generic_visit(node)

    def visit_For(self, node):
        self.increment()
        self.generic_visit(node)

    def visit_While(self, node):
        self.increment()
        self.generic_visit(node)

    def visit_With(self, node):
        self.increment()
        self.generic_visit(node)

    def visit_Try(self, node):
        # one for try, and one for each except block
        self.increment()
        self.complexity += len(node.handlers)
        self.generic_visit(node)

    def visit_IfExp(self, node):  # ternary operator
        self.increment()
        self.generic_visit(node)

    def visit_BoolOp(self, node):  # and/or
        self.complexity += len(node.values) - 1
        self.generic_visit(node)

    def visit_Assert(self, node):
        self.increment()
        self.generic_visit(node)

    def visit_Compare(self, node):  # multiple comparisons like a < b < c
        self.complexity += len(node.ops) - 1
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        # Do not increment here; function itself is not a decision point
        self.generic_visit(node)

    def visit_Yield(self, node):
        self.increment()
        self.generic_visit(node)

    def visit_ExceptHandler(self, node):
        self.increment()
        self.generic_visit(node)

def compute_cyclomatic_complexity(source_code: str) -> int:
    tree = ast.parse(source_code)
    visitor = ComplexityVisitor()
    visitor.visit(tree)
    return visitor.complexity + 1  # +1 for default path

