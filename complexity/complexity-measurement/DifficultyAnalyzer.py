import ast
from CyclomaticDifficulty import compute_cyclomatic_complexity
from RecursiveCallAnalyzer import count_recursive_calls

class DifficultyAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.structures = 0
        self.recursions = 0
        self.data_structures = set()
        self.function_calls = 0
        self.edge_case_score = 0
        self.length = 0
        self.function_name = ""
        self.nesting_depth = 0
        self._depth = 0

    def visit_FunctionDef(self, node):
        self.function_name = node.name
        self.generic_visit(node)

    def visit_If(self, node):
        self.structures += 1
        self.edge_case_score += 1  # edge condition
        self.generic_visit(node)

    def visit_For(self, node):
        self.structures += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.structures += 1
        self.generic_visit(node)

    def visit_Call(self, node):
        self.function_calls += 1
        self.generic_visit(node)

    def visit_List(self, node):
        self.data_structures.add('list')
        self.generic_visit(node)

    def visit_Dict(self, node):
        self.data_structures.add('dict')
        self.generic_visit(node)

    def visit_Set(self, node):
        self.data_structures.add('set')
        self.generic_visit(node)

    def generic_visit(self, node):
        self._depth += 1
        self.nesting_depth = max(self.nesting_depth, self._depth)
        super().generic_visit(node)
        self._depth -= 1

    def analyze(self, code):
        self.__init__()  # reset internal counters
        tree = ast.parse(code)
        self.length = len([line for line in code.splitlines() if line.strip()])
        
        # Count recursive calls using the new analyzer
        self.recursions = count_recursive_calls(code)
        
        # Still visit the tree for other metrics
        self.visit(tree)
        
        return {
            "flow_constructs": self.structures,
            "recursions": self.recursions,  # Now using the new recursive call counter
            "nesting_depth": self.nesting_depth,
            "data_structures": len(list(self.data_structures)),
            "function_calls": self.function_calls,
            "length": self.length,
            "CC": compute_cyclomatic_complexity(code)
        }
