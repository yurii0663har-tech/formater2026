import ast


class FormatterEngine(ast.NodeVisitor):

    def __init__(self, indent_size=4):
        self.indent_size = indent_size
        self.level = 0
        self.lines = []


    def format(self, tree):

        self.lines = []
        self.level = 0

        self.visit(tree)

        return "\n".join(self.lines)


    def write(self, text):

        indent = " " * (
            self.level * self.indent_size
        )

        self.lines.append(
            indent + text
        )


    # -------------------------
    # MODULE
    # -------------------------

    def visit_Module(self, node):

        for item in node.body:
            self.visit(item)


    # -------------------------
    # CLASS
    # -------------------------

    def visit_ClassDef(self, node):

        if node.bases:

            bases = ", ".join(
                ast.unparse(base)
                for base in node.bases
            )

            header = f"class {node.name}({bases}):"

        else:

            header = f"class {node.name}:"


        self.write(header)

        self.level += 1

        for item in node.body:
            self.visit(item)

        self.level -= 1


    # -------------------------
    # FUNCTION
    # -------------------------

    def visit_FunctionDef(self, node):

    # decorators
        for decorator in node.decorator_list:
            self.write(
                "@" + ast.unparse(decorator)
            )

        args = ast.unparse(node.args)

        self.write(
            f"def {node.name}({args}):"
        )

        self.level += 1

        for item in node.body:
            self.visit(item)

        self.level -= 1

    def visit_AsyncFunctionDef(self, node):

        for decorator in node.decorator_list:
            self.write(
                "@" + ast.unparse(decorator)
            )

        args = ast.unparse(node.args)

        self.write(
            f"async def {node.name}({args}):"
        )

        self.level += 1

        for item in node.body:
            self.visit(item)

        self.level -= 1
        
    def visit_Await(self, node):

        self.write(
            "await " + ast.unparse(node.value)
        )
    # -------------------------
    # RETURN
    # -------------------------

    def visit_Return(self, node):

        if node.value:

            self.write(
                f"return {ast.unparse(node.value)}"
            )

        else:

            self.write("return")


    # -------------------------
    # EXPRESSIONS
    # -------------------------

    def visit_Expr(self, node):

        self.write(
            ast.unparse(node.value)
        )


    # -------------------------
    # IF
    # -------------------------

    def visit_If(self, node):

        self.write(
            f"if {ast.unparse(node.test)}:"
        )

        self.level += 1

        for item in node.body:
            self.visit(item)

        self.level -= 1


        if node.orelse:

            self.write("else:")

            self.level += 1

            for item in node.orelse:
                self.visit(item)

            self.level -= 1


    # -------------------------
    # FOR
    # -------------------------

    def visit_For(self, node):

        self.write(
            f"for {ast.unparse(node.target)} in {ast.unparse(node.iter)}:"
        )

        self.level += 1

        for item in node.body:
            self.visit(item)

        self.level -= 1


    # -------------------------
    # WHILE
    # -------------------------

    def visit_While(self, node):

        self.write(
            f"while {ast.unparse(node.test)}:"
        )

        self.level += 1

        for item in node.body:
            self.visit(item)

        self.level -= 1


    # -------------------------
    # TRY
    # -------------------------

    def visit_Try(self, node):

        self.write("try:")

        self.level += 1

        for item in node.body:
            self.visit(item)

        self.level -= 1


        for handler in node.handlers:

            self.write(
                f"except {ast.unparse(handler.type)}:"
            )

            self.level += 1

            for item in handler.body:
                self.visit(item)

            self.level -= 1


        if node.finalbody:

            self.write("finally:")

            self.level += 1

            for item in node.finalbody:
                self.visit(item)

            self.level -= 1


    # -------------------------
    # WITH
    # -------------------------

    def visit_With(self, node):

        items = []

        for item in node.items:

            text = ast.unparse(item.context_expr)

            if item.optional_vars:

                text += f" as {ast.unparse(item.optional_vars)}"

            items.append(text)


        self.write(
            f"with {', '.join(items)}:"
        )

        self.level += 1

        for item in node.body:
            self.visit(item)

        self.level -= 1


    # -------------------------
    # IMPORTS
    # -------------------------

    def visit_Import(self, node):

        self.write(
            ast.unparse(node)
        )


    def visit_ImportFrom(self, node):

        self.write(
            ast.unparse(node)
        )

        # -------------------------
    # ASSIGN
    # -------------------------

    def visit_Assign(self, node):

        self.write(
            ast.unparse(node)
        )
    # -------------------------
    # PASS
    # -------------------------

    def visit_Pass(self, node):

        self.write("pass")
        
