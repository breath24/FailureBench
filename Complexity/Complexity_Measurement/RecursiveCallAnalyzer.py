import ast
from typing import Optional

class RecursiveCallAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.recursive_calls: int = 0
        self.function_stack: list[str] = []
        self.class_stack: list[str] = []

    def visit_ClassDef(self, node: ast.ClassDef):
        self.class_stack.append(node.name)
        self.generic_visit(node)
        self.class_stack.pop()

    def visit_FunctionDef(self, node: ast.FunctionDef):
        self.function_stack.append(node.name)
        self.generic_visit(node)
        self.function_stack.pop()

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        self.function_stack.append(node.name)
        self.generic_visit(node)
        self.function_stack.pop()

    def visit_Call(self, node: ast.Call):
        # Determine the called function's simple name (if available)
        called_name: Optional[str] = None
        if isinstance(node.func, ast.Name):
            called_name = node.func.id
        elif isinstance(node.func, ast.Attribute):
            # Handles cases like self.foo(), cls.foo(), ClassName.foo()
            called_name = node.func.attr

        # If we are inside a function and the called simple name matches
        # the current function name, count as a recursive call site
        if self.function_stack and called_name == self.function_stack[-1]:
            self.recursive_calls += 1

        self.generic_visit(node)

def count_recursive_calls(code: str) -> int:
    """
    Count the number of recursive call sites in the given Python code.
    
    Args:
        code: Python source code as a string
        
    Returns:
        int: Number of recursive call sites in the code
    """
    try:
        tree = ast.parse(code)
        analyzer = RecursiveCallAnalyzer()
        analyzer.visit(tree)
        return analyzer.recursive_calls
    except Exception as e:
        print(f"Error analyzing recursive calls: {e}")
        return 0

# Example usage:
if __name__ == "__main__":
    with open(__file__, 'r') as f:
        code = f.read()
    count = count_recursive_calls(code)
    print(f"Found {count} recursive call(s) in this file.")
